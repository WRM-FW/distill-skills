---
name: nsca-3rd
description: >-
  Evidence-based strength training, athletic conditioning, testing, nutrition,
  rehabilitation, and facility management system distilled from the NSCA
  textbook Essentials of Strength Training and Conditioning (Baechle and Earle,
  3rd Ed.) using the Cangjie RIA-TV++ framework. Use when the user asks to
  design resistance training programs, calculate %1RM loads/volume/rest, plan
  periodization macrocycles, prescribe plyometrics or speed/agility/aerobic
  endurance training, order athletic performance tests, audit exercise
  technique and spotting, calculate athlete nutrition/hydration needs, design
  injury reconditioning (DAPRE/kinetic chain), or plan strength facilities.
---

# nsca-3rd

Whole-book executable methodology router distilled from the National Strength and Conditioning Association (NSCA) flagship textbook *Essentials of Strength Training and Conditioning* (3rd Edition, edited by Thomas R. Baechle and Roger W. Earle) via the Cangjie Skill RIA-TV++ pipeline.

## When to Use

Use this skill when the user asks to:

- Design or audit a resistance training program (needs analysis, exercise selection, frequency, order, %1RM load, 2-for-2 progression, volume, rest periods) or adapt training for youth, female, or older adult athletes.
- Plan a periodized training macrocycle, mesocycle, or microcycle across off-season, preseason, in-season, and active rest periods (linear or undulating models).
- Prescribe metabolic interval work-to-rest ratios or design aerobic endurance programs (LSD, pace/tempo, interval, repetition, fartlek, Karvonen heart rate, tapering).
- Design plyometric programs (foot-contact volume, stretch-shortening cycle mechanics, depth jump box heights, safety prerequisites) or speed and agility mechanics drills.
- Select and sequence an athletic performance test battery (nonfatiguing, agility, max power/strength, sprint, local muscular endurance, anaerobic capacity, aerobic capacity) or run a 1RM testing protocol.
- Evaluate exercise technique, grip/stance stability, breathing (Valsalva vs. exhalation at sticking point), weight belt usage, or free-weight spotting rules.
- Calculate athletic macronutrient intake (protein, carbohydrate, fat by g/kg), hydration replacement, precompetition meals, or weight gain/loss targets.
- Structure post-injury rehabilitation and reconditioning across tissue healing phases (inflammation, repair, remodeling) using closed/open kinetic chain exercises and DeLorme, Oxford, or DAPRE loading protocols.
- Plan or audit a strength and conditioning facility (equipment space formulas, ceiling height, lighting, temperature, humidity, staff-to-athlete supervision ratios, risk management).

Do not use this skill when:

- The user requests acute medical diagnosis, surgical decision-making, or prescription drug treatment (defer to a licensed physician or athletic trainer).
- The user wants general casual fitness chatting without structured exercise science parameters or actionable prescription.

## Core Principles

1. **Specific Adaptation to Imposed Demands (SAID)**: Align every training prescription with the biomechanical movement pattern, primary bioenergetic system (phosphagen, glycolytic, oxidative), and seasonal priority of the target sport.
2. **Fatigue-Ordered Sequencing**: Place high-skill, high-neural-demand activities before fatiguing activities across both testing batteries (nonfatiguing -> agility -> power/strength -> sprint -> muscular endurance -> anaerobic -> aerobic) and daily workouts (power exercises -> nonpower core exercises -> assistance exercises).
3. **Inverse Intensity-Volume Manipulation**: Never maximize training intensity and volume simultaneously; progress from high-volume/low-intensity physiological base building ( Preparatory Hypertrophy/Endurance ) toward high-intensity/low-volume sport specificity ( Basic Strength -> Strength/Power -> Peaking ).
4. **Tissue and Prerequisite Gatekeeping**: Verify structural readiness before high-stress loading (e.g., 1.5x bodyweight 1RM squat and static/dynamic balance before high-intensity lower-body plyometrics; tissue healing phase clearance before remodeling loads).
5. **Conservative Quantitative Progression**: Advance loads systematically using the **2-for-2 rule** (resistance training), **<= 10% weekly progression** (aerobic endurance), and daily Set-3 autoregulation (**DAPRE** in rehabilitation).

## Capability Routing and Reference Cards

Consult the corresponding RIA-TV++ capability card under `references/capabilities/` (or `references/book/overview.md` and `references/book/glossary.md`) when executing specialized tasks:

| User Intent / Task | Primary Capability Card | Key Quantitative Anchors |
| :--- | :--- | :--- |
| Prescribe energy-system intervals or analyze metabolic demands | `references/capabilities/01-bioenergetics-interval-prescription.md` | Phosphagen (0-6 s, 90-100% power, W:R 1:12-1:20); Fast glycolysis (6-30 s, 75-90%, W:R 1:3-1:5); Glycolytic+Oxidative (1-3 min, 30-75%, W:R 1:3-1:4); Oxidative (>3 min, 20-30%, W:R 1:1-1:3) |
| Analyze joint biomechanics, levers, or movement planes | `references/capabilities/02-biomechanics-movement-analysis.md` | Work = F x d; Power = Work / t; Mechanical advantage = Moment arm(internal) / Moment arm(external); 3 planes (sagittal, frontal, transverse) |
| Build or order an athletic performance test battery | `references/capabilities/03-athletic-testing-evaluation.md` | 7-stage sequence: Nonfatiguing -> Agility -> Max Power/Strength -> Sprint -> Local Muscular Endurance -> Fatiguing Anaerobic -> Aerobic (separate day or >= 1 hr rest) |
| Audit warm-up, stretching, lifting technique, or spotting | `references/capabilities/04-warmup-flexibility-technique-spotting.md` | General warm-up (5-10 min) + Specific dynamic warm-up (8-12 min); Static stretch (15-30 s post-workout); PNF (6 s isometric + 10-30 s passive); Never spot power exercises |
| Design a 7-step resistance training program or 1RM test | `references/capabilities/05-resistance-program-design.md` | Strength (>=85% 1RM, <=6 reps, 2-6 sets, 2-5 min rest); Power single/multi (80-90% / 75-85% 1RM, 1-2 / 3-5 reps, 3-5 sets, 2-5 min rest); Hypertrophy (67-85% 1RM, 6-12 reps, 3-6 sets, 30-90 s rest); Endurance (<=67% 1RM, >=12 reps, 2-3 sets, <=30 s rest) |
| Design a plyometric training program | `references/capabilities/06-plyometric-training-design.md` | Volume (contacts/session): Beginner 80-100, Intermediate 100-120, Advanced 120-140; W:R 1:5-1:10; Depth jump 16-42 in (norm 30-32 in; <=18 in if >220 lb); 48-72 hr recovery |
| Diagnose sprint mechanics or design speed/agility drills | `references/capabilities/07-speed-agility-development.md` | Speed = Stride length x Stride frequency; Impulse = F x t; Primary (technique), Secondary (resisted/assisted), Tertiary (mobility/strength/power) |
| Prescribe aerobic endurance training or tapering | `references/capabilities/08-aerobic-endurance-program-design.md` | Karvonen THR = (HRR x intensity) + RHR; 5 modes (LSD ~70% VO2max, Pace/Tempo at LT, Interval ~VO2max 1:1, Repetition >VO2max 1:5, Fartlek); Weekly increase <=10% |
| Plan annual/seasonal periodization macrocycles | `references/capabilities/09-periodization-macrocycle-planning.md` | Preparatory (Hypertrophy/Endurance 50-75% 1RM, 3-6x10-20 -> Basic Strength 80-90% 1RM, 3-5x4-8 -> Strength/Power 75-95% 1RM, 3-5x2-5) -> Competition (Peaking >=93% 1RM, 1-3x1-3 or Maintenance 80-85% 1RM, 2-3x6-8) -> Active Rest (1-4 wk) |
| Calculate sport nutrition, rehab DAPRE, or facility specs | `references/capabilities/10-nutrition-rehab-facility-management.md` | Protein 1.5-2.0 g/kg; Carb 8-10 g/kg (endurance) or 5-6 g/kg (strength/sprint); Fluid 1 pint (0.5 L) per lb lost; DAPRE 4-set protocol; Ceiling 12-14 ft; Supervision 1:10 (middle), 1:15 (high school), 1:20 (college) |

## Steps

### Step 1: Conduct Needs Analysis (Athlete and Sport Audit)

Identify the core inputs before prescribing any training, testing, or nutritional intervention:

1. **Sport Evaluation**: Determine movement patterns (joint actions, planes, muscle groups), physiological priorities (strength, power, hypertrophy, muscular endurance, aerobic/anaerobic capacity), and common injury sites.
2. **Athlete Assessment**: Classify training status (`Beginner`: untrained or <2 months, 1-2 sessions/wk; `Intermediate`: 2-6 months, 2-3 sessions/wk; `Advanced`: >=1 year, >=3-4 sessions/wk), current 1RM or fitness baseline, body weight, age/sex considerations, and current sport season (`Off-season`, `Preseason`, `In-season`, `Postseason`).

### Step 2: Route to Domain Capability Modules

Match the user's primary goal to one or more capability modules in the routing table above:

- For **Resistance Training Prescription**, apply the 7-Step Model (`references/capabilities/05-resistance-program-design.md`): Needs Analysis -> Exercise Selection (Core [Structural/Power] vs. Assistance; agonist-antagonist balance) -> Frequency (by status and season: Off-season 4-6x, Preseason 3-4x, In-season 1-3x, Postseason 0-3x) -> Exercise Order (Power -> Nonpower Core -> Assistance; or Upper/Lower, Push/Pull, Supersets/Compound sets) -> Load & Repetitions (%1RM table) -> Volume (sets x reps x weight) -> Rest Periods.
- For **Plyometrics, Speed, or Aerobic Conditioning**, enforce prerequisite checks and work-to-rest ratios (`06-plyometric-training-design.md`, `07-speed-agility-development.md`, `08-aerobic-endurance-program-design.md`).
- For **Annual/Seasonal Planning**, map sport seasons to Periodization Phases (`09-periodization-macrocycle-planning.md`) and choose between Traditional Linear and Daily/Weekly Undulating (Nonlinear) periodization.
- For **Testing, Nutrition, Rehab, or Facilities**, apply the deterministic sequences and formulas in `03-athletic-testing-evaluation.md` and `10-nutrition-rehab-facility-management.md`.

### Step 3: Verify Quantitative Prescriptions Against Quick-Reference Tables

Cross-check all numerical outputs against these canonical NSCA tables:

| Training Goal | Load (%1RM) | Goal Repetitions | Sets (Core Exercises) | Rest Period |
| :--- | :--- | :--- | :--- | :--- |
| Muscular Strength | >=85% | <=6 | 2-6 | 2-5 min |
| Power (Single-Effort) | 80-90% | 1-2 | 3-5 | 2-5 min |
| Power (Multiple-Effort) | 75-85% | 3-5 | 3-5 | 2-5 min |
| Hypertrophy | 67-85% | 6-12 | 3-6 | 30-90 s |
| Muscular Endurance | <=67% | >=12 | 2-3 | <=30 s |

Cross-check %1RM-to-Repetition assignments using the NSCA lookup scale:

- **100% 1RM**: 1 rep | **95%**: 2 reps | **93%**: 3 reps | **90%**: 4 reps | **87%**: 5 reps | **85%**: 6 reps
- **83% 1RM**: 7 reps | **80%**: 8 reps | **77%**: 9 reps | **75%**: 10 reps | **70%**: 11 reps | **67%**: 12 reps | **65%**: 15 reps

Apply the **2-for-2 Load Progression Rule** and Load Increment Guidelines:

- When an athlete completes >=2 repetitions above the assigned goal in the final set for 2 consecutive workouts, increase load in the next session:
  - **Smaller, weaker, or less-trained athlete**: +2.5-5 lb (1-2 kg) for upper body; +5-10 lb (2-4 kg) for lower body.
  - **Larger, stronger, or more-trained athlete**: +5-10+ lb (2-4+ kg) for upper body; +10-15+ lb (4-7+ kg) for lower body.

### Step 4: Run Safety, Technique, and Boundary Checks

Verify that the final deliverable satisfies all NSCA safety constraints:

1. **Power Exercise Loading & Spotting**: Never assign maximal RM-to-failure loads (e.g., 8RM at 80% 1RM) to multijoint power exercises (snatch, power clean, push jerk), because technique degrades rapidly; limit power sets to 1-5 reps at 75-90% 1RM. Never spot power exercises; clear a safe drop zone and teach the athlete how to release the bar safely.
2. **Assistance Exercise Load Ceiling**: Limit single-joint assistance exercises to loads no heavier than an 8RM (>=8 reps) even during a maximal strength phase to protect isolated joints and connective tissues.
3. **Stretching Timing**: Use dynamic stretching during the specific warm-up (8-12 min); reserve static and PNF stretching for post-practice/post-workout cool-downs or separate flexibility sessions so acute force/power output is not compromised.
4. **Concurrent Training Compatibility**: When combining high-intensity resistance/plyometric training with aerobic endurance training, separate sessions by >=24 hours or alternate upper/lower high-low intensity days (`Table 16.6`) to minimize interference with anaerobic power and rate of force development.

## Gotchas

- **Confusing %1RM-Repetition Table with Power Loads**: At 80% 1RM, an athlete can theoretically grind out 8 reps (`Table 15.7`), but for power training (`Table 15.9`), loads of 75-90% 1RM are performed for only 1-5 explosive repetitions to prevent neuromuscular fatigue and preserve maximal bar velocity.
- **Violating Test Battery Order**: Administering a 300-yard shuttle or 1.5-mile run before vertical jump, T-test, or 1RM testing invalidates neural and phosphagen test reliability. Always follow the 7-stage sequence in `03-athletic-testing-evaluation.md`.
- **Excessive Depth Jump Box Heights**: Box heights above 42 in (107 cm) or >18 in (46 cm) for athletes weighing >220 lb (100 kg) prolong the amortization phase, defeating the stretch reflex and sharply increasing joint injury risk.
- **Wrong Dumbbell Spotting Location**: Spot overhead or supine dumbbell exercises by supporting the athlete's wrists/forearms close to the dumbbells (or the dumbbells themselves), never under the elbows.
- **Premature Open-Kinetic-Chain Loading in Rehab**: During tissue inflammation, avoid active loading of the injured site; during repair and remodeling, progress from isometric to controlled isotonic/isokinetic and closed-kinetic-chain functional movements in coordination with the sports medicine team.
