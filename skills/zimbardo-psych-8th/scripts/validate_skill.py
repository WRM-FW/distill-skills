#!/usr/bin/env python3
"""Validation script for the zimbardo-psych-8th Agent Skill repository."""

import os
import re
import sys

try:
    import yaml
except ImportError:
    yaml = None

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    ".gitignore",
    "references/book/overview.md",
    "references/book/glossary.md",
    "references/capabilities/01-scientific-method-six-perspectives-critical-thinking.md",
    "references/capabilities/02-biopsychology-epigenetics-neuroscience-brain-layers.md",
    "references/capabilities/03-sensation-signal-detection-perceptual-organization.md",
    "references/capabilities/04-behavioral-learning-conditioning-modification.md",
    "references/capabilities/05-memory-encoding-retrieval-seven-sins-mnemonics.md",
    "references/capabilities/06-thinking-heuristics-biases-intelligence-mindset.md",
    "references/capabilities/07-lifespan-development-attachment-piaget-erikson-moral.md",
    "references/capabilities/08-consciousness-circadian-sleep-architecture-states.md",
    "references/capabilities/09-motivation-hierarchy-self-control-emotion-regulation.md",
    "references/capabilities/10-personality-big-five-ztpi-time-perspective-narratives.md",
    "references/capabilities/11-social-psychology-situational-power-lucifer-effect.md",
    "references/capabilities/12-psychopathology-dsm5-biopsychosocial-therapies-stress-coping.md",
]


def main() -> int:
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    errors = []

    for rel_path in REQUIRED_FILES:
        abs_path = os.path.join(repo_root, rel_path)
        if not os.path.isfile(abs_path):
            errors.append(f"Missing required file: {rel_path}")
        elif os.path.getsize(abs_path) == 0:
            errors.append(f"Empty file: {rel_path}")

    skill_path = os.path.join(repo_root, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            text = f.read()

        fm_match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
        if not fm_match:
            errors.append("SKILL.md is missing valid YAML frontmatter delimiters.")
        else:
            if yaml is not None:
                fm = yaml.safe_load(fm_match.group(1))
                name = fm.get("name", "")
                desc = fm.get("description", "")
                if name != "zimbardo-psych-8th":
                    errors.append(f"Unexpected skill name: {name}")
                if not (0 < len(desc) < 1024):
                    errors.append(f"Description length {len(desc)} out of bounds (1..1023).")

        lines = text.splitlines()
        if len(lines) >= 500:
            errors.append(f"SKILL.md has {len(lines)} lines (must be < 500).")

        if "\u2014" in text or "\u2013" in text:
            errors.append("SKILL.md contains prohibited em-dashes or en-dashes.")

    if errors:
        for err in errors:
            print(f"[ERROR] {err}", file=sys.stderr)
        return 1

    print(f"[OK] Verified all {len(REQUIRED_FILES)} files in zimbardo-psych-8th successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
