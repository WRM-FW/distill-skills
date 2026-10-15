---
name: nsca-5th
description: >-
  Evidence-based strength training, athletic conditioning, force-plate and VBT
  testing, RAMP/PAPE warm-up, variable and accentuated eccentric resistance,
  weightlifting derivatives, plyometrics, speed/COD/agility, periodization,
  overtraining recovery, special populations (youth PHV/AMSC, pregnant/female,
  older adults), sports nutrition/RED-S, rehabilitation (DAPRE), and facility
  management system distilled from the NSCA textbook Essentials of Strength
  Training and Conditioning (5th Edition, Haff and Triplett, 2027) using the
  Cangjie RIA-TV++ framework. Use when the user asks to design or audit
  resistance, plyometric, speed, agility, or endurance training programs,
  calculate %1RM/SRB/RIR or chain/band/AEL loads, plan periodized macrocycles,
  sequence or interpret athletic performance tests, audit exercise or spotting
  technique, calculate athlete nutrition/hydration/EA needs, or manage injury
  reconditioning and strength facilities.
---

# nsca-5th

Whole-book executable methodology router distilled from the National Strength and Conditioning Association (NSCA) flagship textbook *Essentials of Strength Training and Conditioning* (5th Edition, edited by G. Gregory Haff and N. Travis Triplett, 2027, 26 Chapters) via the Cangjie Skill RIA-TV++ pipeline.

## When to Use

Use this skill when the user asks to:

- Design or audit a resistance training program using the 7-Step Model, `%1RM`, **Set-Repetition Best (SRB)**, **Repetitions in Reserve (RIR / RPE)**, **Weightlifting Catching/Pulling/Pressing Derivatives**, **Variable Resistance (Chains/Bands)**, or **Accentuated Eccentric Loading (AEL)**.
- Tailor training prescriptions for **Youth** (`YPD` model, `% Predicted Adult Height / PHV`, `AMSC`), **Female and Pregnant/Postpartum Athletes** (trimester rules, ACL/PFPS/pelvic floor UI/SUI, menstrual cycle), or **Older Adults** (`sarcopenia`, `dynapenia`, `osteoporosis`, high-velocity power training, fall prevention).
- Plan a **RAMP Warm-Up** (`Raise -> Activate and Mobilize -> Potentiate`), **Postactivation Performance Enhancement (PAPE)** priming protocol, or flexibility session (`static`, `dynamic`, `PNF`).
- Design **Plyometric, Ballistic, or Complex/Contrast** training (`fast vs. slow SSC`, foot-contact volume by intensity, `1.0x/1.5x/2.0x BW` squat tiers, active flat-foot landing).
- Develop **Sprint Speed, Change-of-Direction (COD), Deceleration, or Reactive Agility** (`Impulse-Momentum`, `RFD`, 4-block short-to-long speed periodization, 3-block agility periodization, `COD Deficit`, sled velocity-decrement loading).
- Prescribe **Bioenergetic Intervals, HIIT, or Aerobic Endurance** (`3-zone` and `5-zone` scales, `Karvonen HRR`, `MAS`, `30-15 IFT`, `LSD/Tempo/Interval/Repetition/Fartlek`, **Altitude vs. Heat Acclimation** timelines).
- Architect **Annual Periodized Macrocycles** (`Linear`, `Daily/Weekly Undulating`, or `Block/Conjugate`), prevent or recover from **Functional/Nonfunctional Overreaching and Overtraining Syndrome (FOR/NFOR/OTS)**, or apply **Sport Psychology and 3-Step ABC Mental Health Triage** (`CMPC` vs. `Counselor/Psychologist`).
- Select, sequence, and statistically evaluate an **Athletic Performance Testing Battery** (7-stage order, `IMTP`, `CMJ/SJ/Drop/10-5 Rebound Jump RSI & mRSI`, `VBT` velocity zones, `Nordic Hamstring`, `Z-scores`, `SWC`, `Effect Size`).
- Calculate **Sports Nutrition, Hydration, and Energy Availability (`RED-S`)**, evaluate **Ergogenic Aids / Supplements / SARMs / Peptides**, structure **Injury Rehabilitation (`Tissue Healing Phases + DAPRE`)**, manage **Exertional Medical Conditions** (`Rhabdomyolysis`, `Sickle Cell Trait`, `Heatstroke`), or plan **S&C Facilities and Legal Risk Management (`EAP`)**.

Do not use this skill when:

- The user requests primary medical diagnosis, surgical intervention, psychiatric psychotherapy, or prescription drug orders (defer to a licensed physician, sports dietitian RD/CSSD, athletic trainer, physical therapist, or clinical psychologist).
- The user wants casual fitness chatting without structured exercise science parameters or actionable prescription.

## Core Principles

1. **Impulse-Momentum and SAID Specificity**: Align every prescription with the sport's movement planes (`24 movements across sagittal, frontal, transverse`), time-constrained **Net Impulse (`F x dt = m x dv`)**, **Rate of Force Development (RFD, 0-200 ms)**, and dominant bioenergetic pathway (`Phosphagen`, `Fast/Slow Glycolysis`, `Oxidative`).
2. **Fatigue-Ordered Sequencing**: Place high-skill, high-neural-demand activities first across both **Testing Batteries** (`Nonfatiguing -> Agility -> Max Power/Strength -> Sprint -> Local Muscular Endurance -> Fatiguing Anaerobic -> Aerobic`) and **Workouts** (`Power/Ballistic/Speed -> Nonpower Core -> Assistance`).
3. **Sub-Failure Autoregulation and Fitness-Fatigue Management**: Avoid chronic training to momentary failure (`0 RIR`); use **Set-Repetition Best (SRB)** 5% relative intensity ranges, **RIR/RPE**, Heavy/Light day variation (`-15% to -20%`), and `3:1` or `4:1` deload microcycles (`Figure 18.1`) to unmask supercompensation and prevent NFOR/OTS.
4. **Biomechanical and Prerequisite Gatekeeping**: Verify relative strength tiers (`1.0x`, `1.5x`, `>2.0x BW` squat for plyometrics and AEL), somatic maturity (`PHV at 91-92% adult height`), trimester constraints (no supine after Trimester 1), and tissue healing phases (`Inflammation -> Repair -> Remodeling`) before advancing mechanical loads.
5. **Holistic Athlete Safety and Scope Discipline**: Screen Energy Availability (`optimal >=45`, `RED-S <30 kcal/kg FFM/day`), hydration (`<2% BW loss`, `1.5 L/kg` rehydration), 3-step ABC mental health duration/disruption (`>=2-3 wk` clinical referral), and facility/EAP standards (`Cool first, transport second` for exertional heatstroke).

## Capability Routing and Reference Cards

Consult the corresponding RIA-TV++ capability card under `references/capabilities/` (plus `references/book/overview.md` and `references/book/glossary.md`) when executing specialized tasks:

| User Intent / Task | Primary Capability Card | Key 5th Edition Quantitative Anchors |
| :--- | :--- | :--- |
| Prescribe energy-system intervals, HIIT duty cycles, or endocrine workout variables | `references/capabilities/01-bioenergetics-hiit-endocrine-prescription.md` | Glucose yields 32 ATP (34 from glycogen); Phosphagen (`5-10 s, 90-100%, W:R 1:12-1:20`); Fast glycolysis (`15-30 s, 75-90%, W:R 1:3-1:5`); HIIT (`>=90% VO2max`, `30:30 s @ 105% VO2max`); Testosterone (`85-95% 1RM, 30-60 s rest`); 22 kD GH (`10RM x 3, 1 min rest`) |
| Analyze levers/planes, calculate impulse/work/power, or program Chains, Bands, and AEL | `references/capabilities/02-biomechanics-levers-variable-resistance.md` | `F x dt = m x dv`; `TOV = sqrt(2gh)`; `Bar Load = Target RM - [(Top+Bottom)/2]` (`Tables 17.1-17.2`); Submaximal AEL (`+20-30% BW` on jumps), Maximal (`100% ecc`), Supramaximal (`105-120% ecc / 30-90% con`, requires `>=1.5x` bench / `>=2.0x` squat) |
| Build/order a test battery, run IMTP/Jump/Nordic/MAS/30-15 IFT/VBT, or compute SWC/ES | `references/capabilities/03-athletic-testing-vbt-force-plate-evaluation.md` | 7-stage test sequence; IMTP (`1000 Hz, knee 120-145 deg, hip 125-150 deg`); `RSI = Height/GCT`; `mRSI = Height/TTT`; VBT zones (`<0.50 m/s` absolute strength -> `>1.3 m/s` starting strength; never predict daily 1RM squat from L-V regression); `VO2max = 3.5 x MAS`; `SWC = 0.2 x SD` |
| Design a RAMP warm-up, PAPE CNS priming protocol, or static/dynamic/PNF flexibility session | `references/capabilities/04-ramp-warmup-pape-mobility-flexibility.md` | **RAMP** (`Raise -> Activate & Mobilize -> Potentiate`, `10-20 min`, end `<=15 min` pre-event); **PAPE** (`60-90% 1RM 1-3x1-3, 3-12 min rest` or sled/depth jump `1-5 min rest`); Static (`15-30 s` post-workout; avoid `>60 s` pre-event); PNF (`10 s pre + 6 s @ 20% MVC + 30 s passive`) |
| Audit lifting setup, grips, breathing/belts, spotting, or strongman/nontraditional technique | `references/capabilities/05-exercise-technique-spotting-nontraditional.md` | 5-point bench contact; Snatch grip (fist-to-opposite-shoulder or elbow-to-elbow); Never spot power lifts; Spot DBs at wrists/forearms (`Fig 16.3b`); Mid-thigh pull at power position (up to `140% 1RM`); Tire flip shoulders-against-tire (`45 deg`) to prevent biceps tear |
| Design a 7-step resistance program using %1RM, SRB/RIR, and weightlifting derivatives | `references/capabilities/06-resistance-program-design-srb-rir.md` | Strength (`>=85% 1RM, <=6 reps, >=3 sets, 2-5 min rest`); Power (`75-90% 1RM, 1-6 reps, 3-6 sets, 2-5 min rest`); Hypertrophy (`67-80% 1RM [or >80% 10x3], 3-12 reps, >=3 sets, 2-3 min multijoint / 60-90 s single-joint rest`); Endurance (`<=67% 1RM, >=12 reps, <=30 s rest`); `SRB` 5% bands (`Table 18.10`); WL derivatives (`30-140% 1RM`, `Table 18.14`) |
| Design plyometric, ballistic, or complex/contrast training programs | `references/capabilities/07-plyometric-ballistic-complex-training.md` | Fast SSC (`<0.25 s`) vs. Slow SSC (`>0.25 s`); Active flat-foot ("credit card rule"); Contacts/session (`Table 19.6`: Beginner `80-100` low, Interm `100-120` low / `20-100` mod, Adv `120-200` low / `20-120` mod / `20-40` high); Strength tiers (`1.0x, 1.5x, >2.0x BW` squat); Depth jump `16-42 in` (`<=18 in` if `>220 lb`); `W:R 1:5-1:10`, `48-72 hr` recovery |
| Diagnose sprint mechanics or design speed, deceleration, COD, and reactive agility blocks | `references/capabilities/08-speed-cod-agility-development.md` | Elite max velocity (`GCT 0.09-0.11 s`, front-half vertical force asymmetry); Sled load (`<=10-12%` velocity loss for sprinters; `20-30% BW` for field sport accel); 4-block short-to-long speed plan (`Table 20.7`); Cuts `>=75 deg` require multi-step braking impulse; `COD Deficit = 5-0-5 - 10m`; 3-block agility plan (`Tables 20.10-20.11`) |
| Design aerobic endurance programs (3/5-zone scales) or schedule altitude vs. heat acclimation | `references/capabilities/09-aerobic-endurance-metabolic-conditioning.md` | 3-Zone (`<LT1`, `LT1-OBLA`, `>OBLA`) & 5-Zone scales; 5 Modes (`LSD`, `Pace/Tempo`, `Interval 1:1`, `Repetition 1:5`, `Fartlek`); `<=10%/wk` progression; `1-3 wk` taper; **Altitude** (`>1,189 m, 3-6 wk` for EPO/RBCs) vs. **Heat Acclimation** (`~75%` in `4-6 d`, full in `10-14 d`, decays `2.5%/d`) |
| Plan annual periodization, prevent/recover from FOR/NFOR/OTS, or triage athlete mental health | `references/capabilities/10-periodization-overtraining-recovery.md` | Hierarchy (`Annual -> Macro -> Meso [2-6 wk] -> Micro [7 d]`); Phases (`GPP -> SPP -> 1st Transition -> Peaking/Maintenance -> Active Rest`); **Overtraining Continuum** (`Acute -> FOR -> NFOR -> Sympathetic/Parasympathetic OTS`); **3-Step ABC Mental Health Referral** (`<=1-2 wk` sport-only -> `CMPC`; `>=2-3 wk` or life/sleep disruption -> `Counselor/Psychologist`) |
| Adapt training for Youth (YPD/PHV/AMSC), Female & Pregnant/Postpartum, or Older Adults | `references/capabilities/11-youth-female-older-adult-special-populations.md` | **Youth**: `PHV` at `91-92%` adult height (growth spurt `88-95%`), 8 `AMSC` categories, `2-3x/wk`, `+5-10%` load progression.<br>**Pregnancy**: No supine after Trimester 1, `<90% HRmax`, `12-24 wk` postpartum pelvic floor/core.<br>**Older Adults**: Strength `2-3x6-12 @ 70-85% 1RM` + High-Velocity Power `1-3x6-10 @ 40-60% 1RM` + Balance, no Valsalva, `48-72 hr` rest |
| Calculate sports nutrition/RED-S, evaluate supplements/SARMs, run DAPRE rehab, or plan facilities/EAP | `references/capabilities/12-nutrition-ergogenics-rehab-facility-legal.md` | `Cunningham RMR = 500 + 22(FFM)`; `EA = (EI - EEE)/FFM` (`optimal 45, RED-S <30 kcal/kg FFM`); Protein `1.4-2.2+ g/kg` (`2.3-3.1 g/kg FFM` in deficit); Carb loading `8-12 g/kg`; Fluid `1.5 L/kg lost`; Creatine/Caffeine/Beta-Alanine/Bicarb vs. SARMs; `Inflammation -> Repair -> Remodeling` + `DAPRE`; `Cool first, transport second` for EHS; Clearances `>=36 in / 60 in`; Supervision `1:10 / 1:15 / 1:20` |

## Steps

### Step 1: Conduct Multi-Domain Needs Analysis (Sport + Athlete Audit)

Before generating any training program, test battery, nutritional plan, or facility layout, establish the governing context:

1. **Sport & Seasonal Evaluation**: Identify primary movement planes (`Figure 2.10`), bioenergetic profile (`Table 5.1`), injury mechanisms, and seasonal period (`Off-season`, `Preseason`, `In-season`, `Postseason`).
2. **Athlete Profile & Diagnostics**: Classify resistance training status (`Beginner <2 mo`, `Intermediate 2-6 mo`, `Advanced >=1 yr`, `Table 18.1`), age/maturation/sex/obstetric status (`PHV % adult height`, `pregnancy trimester`, `65+ senior`), force-plate/VBT profile (`IMTP`, `CMJ mRSI`, `RJT RSI`), and health/injury clearance.

### Step 2: Route to Domain Capability Cards and Execute Deterministic Rules

Load and apply the exact methodology from the relevant capability card(s) in `references/capabilities/`:

- For **Workout & Periodization Design**, combine `06-resistance-program-design-srb-rir.md` (7-step model, `%1RM` vs. `SRB/RIR`, weightlifting derivatives `Table 18.14`) with `10-periodization-overtraining-recovery.md` (macro/meso/microcycle sequencing and `3:1` deloading).
- For **Warm-Up, Plyometrics, and Speed/Agility**, sequence `04-ramp-warmup-pape-mobility-flexibility.md` (`RAMP` + `PAPE`) -> `08-speed-cod-agility-development.md` (sprint/COD/reactive agility blocks) -> `07-plyometric-ballistic-complex-training.md` (foot contacts and strength tiers).
- For **Special Populations, Nutrition, Rehab, or Facilities**, enforce the population/clinical guardrails in `11-youth-female-older-adult-special-populations.md` and `12-nutrition-ergogenics-rehab-facility-legal.md`.

### Step 3: Cross-Check Quantitative Prescriptions Against 5th Edition Master Tables

Verify all numerical outputs against the canonical 5th Edition prescription matrix (`Tables 18.11, 18.13, 18.15`):

| Training Goal | Load (%1RM) | Goal Repetitions | Core Exercise Sets (Nov / Int / Adv) | Rest Period Length (5th Ed Update) |
| :--- | :--- | :--- | :--- | :--- |
| **Muscular Strength** | `>= 85% 1RM` (Assistance `>=8RM`) | `<= 6` | `1-3` / `>= 3` / `>= 3` | **2 to 5 minutes** |
| **Power: Single-Effort** | `80-90% 1RM` (`30-140%` WL derivs) | `1-3` | `n/a` / `1-3` / `3-6` | **2 to 5 minutes** |
| **Power: Multiple-Effort** | `75-85% 1RM` (`30-140%` WL derivs) | `3-6` | `n/a` / `1-3` / `3-6` | **2 to 5 minutes** |
| **Hypertrophy** | `67-80% 1RM` (or `>80%` e.g., `10x3`) | `8-12` (`3-12` Adv) | `1-3` / `>= 3` / `>= 3` | **2-3 min (multijoint)** / **60-90 s (single-joint)** |
| **Muscular Endurance** | `<= 67% 1RM` | `12-25` | `1-3` / `>= 3` / `>= 3` | **<= 30 seconds** |

### Step 4: Run Final Safety, Technique, and Scope Verification

1. **Spotting & Belt Audit**: Never spot power exercises; spot dumbbell presses at the forearms/wrists (`Figure 16.3b`), never under the elbows; use a power rack or 2 spotters for squats; restrict weight belts and brief (`1-2 s`) Valsalva to heavy structural lifts (`non-senior, non-pregnant`).
2. **Testing & Training Order Audit**: Ensure tests follow the 7-stage non-interfering order (`Ch 13`) and daily sessions place Power/Speed/Agility before fatiguing Core/Assistance/Endurance work.
3. **Clinical & Legal Referral Audit**: Flag `EA < 30 kcal/kg FFM/day` (`RED-S`), persistent `>=2-3 wk` mental distress, eating disorder signs, or acute tissue inflammation for immediate referral to the physician, RD/CSSD, athletic trainer, or licensed mental health professional.

## Gotchas

- **Predicting Daily 1RM Back Squat from Submaximal Load-Velocity Profiles**: `Chapter 14 (Figure 14.1)` proves that linear load-velocity regressions from submaximal sets (`60-90% 1RM`) systematically overestimate actual 1RM back squat by `~20-26 kg`; use direct 1RM testing (`Figure 18.8`), velocity zones (`Table 14.13`), or `SRB/RIR` instead.
- **Confusing 1,000 Hz Instantaneous Peak Power with Mean Propulsion Power**: `Chapter 2` warns that 1-ms instantaneous peak power represents only 1-2 mm of displacement; evaluate net impulse (`F x dt`), mean propulsion power, and `mRSI` (`Jump Height / Time to Takeoff`).
- **Using Short Rest (60-90 s) on Heavy Multijoint Hypertrophy Lifts**: In the 5th Edition (`Table 18.15`), multijoint hypertrophy exercises (squats, deadlifts, presses) use **2-3 minutes rest** to preserve total volume-load, whereas **60-90 seconds rest** applies to single-joint assistance exercises.
- **Modifying Female Programs Solely by Menstrual Cycle Phase**: `Chapter 8` concludes from meta-analyses that there is no systematic performance change across menstrual cycle phases; do not apply rigid phase-based templates, but adjust individually for menstrual symptoms and sleep.
- **Setting Mid-Thigh Pull Bar at Anatomical Mid-Thigh**: `Chapter 16 (#44)` specifies that the mid-thigh pull must start from the athlete's individualized **second-pull power position** (`knee 125-145 deg, hip 140-150 deg`, vertical trunk), which usually places the bar across the upper thigh (clean grip) or hip crease (snatch grip), not anatomical mid-thigh.
