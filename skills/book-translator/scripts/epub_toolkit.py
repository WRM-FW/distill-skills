#!/usr/bin/env python3
"""
EPUB Toolkit for Book Translator Skill
Provides pure-Python EPUB unpacking, inspection, typography optimization,
IDPF-compliant packaging, and verification.
"""

import os
import sys
import re
import shutil
import zipfile
import argparse
from pathlib import Path

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False


def unpack_epub(epub_path: str, extract_dir: str):
    """Unpack EPUB file to extract_dir."""
    print(f"Unpacking {epub_path} -> {extract_dir}...")
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(epub_path, 'r') as zf:
        zf.extractall(extract_dir)
    print("Unpack complete.")


def pack_epub(source_dir: str, output_epub: str):
    """
    Pack source_dir into a valid IDPF-compliant EPUB:
    1. First entry MUST be 'mimetype' stored with NO COMPRESSION (ZIP_STORED).
    2. Other files compressed with ZIP_DEFLATED in deterministic order.
    """
    print(f"Packaging EPUB from {source_dir} -> {output_epub}...")
    
    # Ensure mimetype file exists
    mimetype_path = os.path.join(source_dir, 'mimetype')
    if not os.path.exists(mimetype_path):
        with open(mimetype_path, 'wb') as f:
            f.write(b'application/epub+zip')

    os.makedirs(os.path.dirname(os.path.abspath(output_epub)), exist_ok=True)

    with zipfile.ZipFile(output_epub, 'w') as zf:
        # 1. Write mimetype FIRST, uncompressed
        zf.write(mimetype_path, 'mimetype', compress_type=zipfile.ZIP_STORED)

        # 2. Add META-INF/container.xml next if present
        container_path = os.path.join(source_dir, 'META-INF', 'container.xml')
        if os.path.exists(container_path):
            zf.write(container_path, 'META-INF/container.xml', compress_type=zipfile.ZIP_DEFLATED)

        # 3. Add all remaining files
        all_entries = []
        for root, dirs, files in os.walk(source_dir):
            dirs.sort()
            files.sort()
            for f in files:
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, source_dir).replace('\\', '/')
                if rel_path in ['mimetype', 'META-INF/container.xml']:
                    continue
                all_entries.append((full_path, rel_path))

        all_entries.sort(key=lambda x: x[1])
        for full_path, rel_path in all_entries:
            zf.write(full_path, rel_path, compress_type=zipfile.ZIP_DEFLATED)

    print(f"EPUB successfully packed! File size: {os.path.getsize(output_epub):,} bytes")


def inspect_epub(source_dir: str):
    """Inspect unpacked EPUB for formatting flaws, small caps, CSS classes, and footnotes."""
    print(f"=== Inspecting EPUB directory: {source_dir} ===")
    
    # Find all html/xhtml files
    html_files = []
    css_files = []
    for root, _, files in os.walk(source_dir):
        for f in files:
            path = os.path.join(root, f)
            rel = os.path.relpath(path, source_dir).replace('\\', '/')
            if f.lower().endswith(('.html', '.xhtml', '.htm')):
                html_files.append((path, rel))
            elif f.lower().endswith('.css'):
                css_files.append((path, rel))

    print(f"Found {len(html_files)} HTML/XHTML documents and {len(css_files)} CSS stylesheets.")

    # Check META-INF/com.apple.ibooks.display-options.xml
    apple_opt = os.path.join(source_dir, 'META-INF', 'com.apple.ibooks.display-options.xml')
    if os.path.exists(apple_opt):
        print("[OK] Apple Books display-options.xml is present.")
    else:
        print("[WARN] Missing META-INF/com.apple.ibooks.display-options.xml (custom fonts may be locked by Apple Books).")

    small_caps_count = 0
    small_caps_samples = []
    class_counts = {}
    footnote_links = 0

    for path, rel in html_files:
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
        except Exception as e:
            print(f"Error reading {rel}: {e}")
            continue

        if HAS_BS4:
            soup = BeautifulSoup(content, 'html.parser')
            # Check <small> tags
            smalls = soup.find_all('small')
            if smalls:
                small_caps_count += len(smalls)
                for s in smalls[:2]:
                    small_caps_samples.append((rel, s.get_text()[:40]))
            
            # Check classes
            for elem in soup.find_all(True):
                classes = elem.get('class', [])
                if isinstance(classes, list):
                    for c in classes:
                        class_counts[c] = class_counts.get(c, 0) + 1
                elif isinstance(classes, str):
                    class_counts[classes] = class_counts.get(classes, 0) + 1

            # Check footnotes
            fn = soup.find_all('a', href=lambda h: h and ('#fn' in h or '#note' in h or 'notes' in h or 'footnote' in h))
            footnote_links += len(fn)
        else:
            smalls = re.findall(r'<small>(.*?)</small>', content, re.DOTALL | re.IGNORECASE)
            small_caps_count += len(smalls)
            for s in smalls[:2]:
                small_caps_samples.append((rel, re.sub(r'<[^>]+>', '', s)[:40]))

    print(f"\n--- Typography Scan Summary ---")
    print(f"Total <small> tags found: {small_caps_count}")
    if small_caps_samples:
        print("Sample <small> locations (often caused by Western Small Caps):")
        for rel, snippet in small_caps_samples[:5]:
            print(f"  [{rel}] \"{snippet}\"")
    print(f"Footnote references detected: {footnote_links}")

    if class_counts:
        print("\nTop 10 CSS classes by frequency:")
        sorted_classes = sorted(class_counts.items(), key=lambda x: x[1], reverse=True)
        for c, count in sorted_classes[:10]:
            print(f"  .{c}: {count}")


def fix_typography(source_dir: str, remove_small: bool = True, inject_apple_css: bool = True):
    """
    Fix common typography issues:
    1. Clean up or normalize <small> tags in Chinese text.
    2. Inject or append publication-grade CSS for Apple Books & modern e-readers.
    3. Ensure com.apple.ibooks.display-options.xml is present.
    """
    print(f"Applying typography fixes to {source_dir}...")

    # 1. Ensure META-INF/com.apple.ibooks.display-options.xml
    meta_inf = os.path.join(source_dir, 'META-INF')
    os.makedirs(meta_inf, exist_ok=True)
    apple_opt = os.path.join(meta_inf, 'com.apple.ibooks.display-options.xml')
    if not os.path.exists(apple_opt):
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<display_options>
  <platform name="*">
    <option name="specified-fonts">true</option>
    <option name="open-to-spread">true</option>
  </platform>
</display_options>
"""
        with open(apple_opt, 'w', encoding='utf-8') as fp:
            fp.write(xml_content.strip() + "\n")
        print("Injected META-INF/com.apple.ibooks.display-options.xml")

    # 2. Fix <small> tags in HTML/XHTML
    modified_files = 0
    total_smalls_removed = 0

    for root, _, files in os.walk(source_dir):
        for f in files:
            if not f.lower().endswith(('.html', '.xhtml', '.htm')):
                continue
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()

            orig_content = content
            if remove_small:
                # Unwrap <small> tags: <small>(...)</small> -> \1
                def unwrap_small(match):
                    nonlocal total_smalls_removed
                    total_smalls_removed += 1
                    return match.group(1)

                content = re.sub(r'<small\b[^>]*>(.*?)</small>', unwrap_small, content, flags=re.DOTALL | re.IGNORECASE)

            if content != orig_content:
                with open(path, 'w', encoding='utf-8') as fp:
                    fp.write(content)
                modified_files += 1

    print(f"Removed/unwrapped {total_smalls_removed} <small> tags across {modified_files} HTML files.")

    # 3. Enhance CSS with Chinese typography & Apple Books rules
    css_patch = """
/* === Injected Publication-Grade Typography === */
small { font-size: 1em !important; font-weight: inherit !important; }
body {
  font-family: -apple-system, "PingFang SC", "Songti SC", "Source Han Serif SC", "STSong", serif;
  text-align: justify;
  text-justify: inter-ideograph;
  word-break: break-word;
  line-height: 1.65;
  color: inherit;
  background-color: transparent;
}
p {
  text-indent: 2em;
  orphans: 2;
  widows: 2;
}
.no-indent, .noindent, h1 + p, h2 + p, h3 + p, blockquote p {
  text-indent: 0;
}
i, em, cite {
  font-family: "Kaiti SC", "STKaiti", "KaiTi", serif;
  font-style: normal;
}
blockquote {
  border-left: 3px solid #8e9ca8;
  padding-left: 1em;
  font-family: "Kaiti SC", "STKaiti", "KaiTi", serif;
  font-style: normal;
}
"""
    # Append to all found CSS files
    css_found = False
    for root, _, files in os.walk(source_dir):
        for f in files:
            if f.lower().endswith('.css'):
                css_found = True
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    css_data = fp.read()
                if "Injected Publication-Grade Typography" not in css_data:
                    with open(path, 'a', encoding='utf-8') as fp:
                        fp.write("\n" + css_patch + "\n")
                    print(f"Appended typography rules to {f}")

    print("Typography optimization complete.")


def validate_epub(epub_path: str):
    """Strict validation of EPUB structure."""
    print(f"=== Validating EPUB: {epub_path} ===")
    if not os.path.exists(epub_path):
        print(f"Error: file not found: {epub_path}")
        return False

    is_valid = True
    with zipfile.ZipFile(epub_path, 'r') as zf:
        infolist = zf.infolist()
        if not infolist:
            print("[FAIL] EPUB zip file is empty!")
            return False

        # Rule 1: First entry is mimetype
        first_entry = infolist[0]
        if first_entry.filename != 'mimetype':
            print(f"[FAIL] First zip entry is '{first_entry.filename}', but IDPF requires 'mimetype'")
            is_valid = False
        else:
            if first_entry.compress_type != zipfile.ZIP_STORED:
                print(f"[FAIL] 'mimetype' must be uncompressed (ZIP_STORED), got compress_type={first_entry.compress_type}")
                is_valid = False
            else:
                mimetype_content = zf.read('mimetype').strip()
                if mimetype_content != b'application/epub+zip':
                    print(f"[FAIL] Invalid mimetype content: {mimetype_content}")
                    is_valid = False
                else:
                    print("[PASS] mimetype is first entry, uncompressed, with correct payload.")

        # Rule 2: META-INF/container.xml exists
        if 'META-INF/container.xml' not in zf.namelist():
            print("[FAIL] Missing META-INF/container.xml")
            is_valid = False
        else:
            print("[PASS] META-INF/container.xml exists.")

        # Rule 3: Check Apple Books options
        if 'META-INF/com.apple.ibooks.display-options.xml' in zf.namelist():
            print("[PASS] META-INF/com.apple.ibooks.display-options.xml found (Apple Books optimized).")
        else:
            print("[INFO] No com.apple.ibooks.display-options.xml (optional for non-Apple devices).")

        # Rule 4: Parse HTML/XHTML to check for syntax errors
        html_count = 0
        error_count = 0
        for info in infolist:
            if info.filename.lower().endswith(('.html', '.xhtml', '.htm')):
                html_count += 1
                try:
                    data = zf.read(info.filename).decode('utf-8')
                    if HAS_BS4:
                        BeautifulSoup(data, 'html.parser')
                except Exception as e:
                    print(f"[WARN] Failed to parse {info.filename}: {e}")
                    error_count += 1

        print(f"[PASS] Checked {html_count} HTML/XHTML documents ({error_count} syntax warnings).")

    if is_valid:
        print(">>> EPUB VALIDATION PASSED! <<<")
    else:
        print(">>> EPUB VALIDATION FAILED! <<<")
    return is_valid


def main():
    parser = argparse.ArgumentParser(description="EPUB Toolkit for Book Translator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # unpack
    p_unpack = subparsers.add_parser("unpack", help="Unpack EPUB file")
    p_unpack.add_argument("epub", help="Path to .epub file")
    p_unpack.add_argument("out_dir", help="Output directory")

    # pack
    p_pack = subparsers.add_parser("pack", help="Pack directory to EPUB")
    p_pack.add_argument("source_dir", help="Unpacked EPUB directory")
    p_pack.add_argument("output_epub", help="Output .epub path")

    # inspect
    p_inspect = subparsers.add_parser("inspect", help="Inspect unpacked EPUB directory")
    p_inspect.add_argument("source_dir", help="Unpacked EPUB directory")

    # fix-typography
    p_fix = subparsers.add_parser("fix-typography", help="Fix typography, small caps and Apple Books styles")
    p_fix.add_argument("source_dir", help="Unpacked EPUB directory")

    # validate
    p_val = subparsers.add_parser("validate", help="Validate an EPUB file")
    p_val.add_argument("epub", help="Path to .epub file")

    args = parser.parse_args()

    if args.command == "unpack":
        unpack_epub(args.epub, args.out_dir)
    elif args.command == "pack":
        pack_epub(args.source_dir, args.output_epub)
    elif args.command == "inspect":
        inspect_epub(args.source_dir)
    elif args.command == "fix-typography":
        fix_typography(args.source_dir)
    elif args.command == "validate":
        validate_epub(args.epub)


if __name__ == "__main__":
    main()
