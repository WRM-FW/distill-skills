# Capability 03: Athletic Performance Testing, VBT, and Force-Plate Evaluation

## R - Source Anchor (Reading)

- **Source Location**: Chapter 13 (Principles of Test Selection and Administration, `Table 13.1`, `Figures 13.1-13.2`) and Chapter 14 (Administration, Scoring, and Interpretation of Selected Tests, 37 Test Protocols, `Tables 14.1-14.37`, `Figures 14.1-14.34`).
- **Core Mechanism**:
  - **5-Step Scientific Process of Testing (`Figure 13.1`)**: (1) **Question** (identify performance problem) -> (2) **Test** (select valid/reliable test & metrics) -> (3) **Hypothesize** (formulate intervention hypothesis) -> (4) **Intervene** (execute training modification) -> (5) **Evaluate** (retest and accept/reject hypothesis).
  - **Psychometric Quality (`Ch 13`)**:
    - **Validity**: `Construct Validity` (overall construct representation, supported by **Convergent Validity** [high correlation with gold standard] and **Discriminant Validity** [low correlation with unrelated constructs, e.g., 1RM squat vs. VO2max]), `Face Validity`, `Content Validity`, and `Criterion Validity` (`Concurrent` and `Predictive`).
    - **Reliability**: Quantified via **Intraclass Correlation Coefficient (ICC)** and **Typical Error of Measurement (TE)** (combines equipment error + biological variation). Requires controlling intrasubject variability, interrater agreement, and intrarater consistency.
  - **Environmental Heat & Humidity Testing Limits (`Figure 13.2`)**:
    - **1-20% RH**: Max temperature limit `~95 F (35 C)`
    - **21-50% RH**: Max temperature limit `~90 F (32 C)`
    - **51-90% RH**: Max temperature limit `~85 F (29 C)`
    - **91-100% RH**: Max temperature limit `~75 F (24 C)`
    - **Safety Margin**: Suspend or move outdoor testing indoors at **>=5 F (3 C) below** these limits on sunny days. Above `1,900 ft (579 m)` altitude, adjust aerobic norms (~5% VO2max drop per `3,000 ft [914 m]` up to `9,000 ft [2,743 m]`; allow >=10 days acclimatization).

## I - Methodology Skeleton (Interpretation)

### 1. Mandatory 7-Stage Test Battery Sequence (`Ch 13`)

Tests must be sequenced so phosphagen, neural, or glycolytic fatigue never corrupts subsequent tests:

1. **Stage 1 - Nonfatiguing Tests**: Height, weight, flexibility (sit-and-reach, overhead squat), skinfold/BIA/girth body composition, vertical jump (CMJ/SJ/Drop/Rebound jump), standing long jump, BESS/SEBT balance.
2. **Stage 2 - Agility / Change-of-Direction Tests**: T-test, Hexagon test, 5-10-5 (Pro Agility), 5-0-5 test, Illinois test.
3. **Stage 3 - Maximum Power and Strength Tests**: Isometric Mid-Thigh Pull (IMTP), 1RM Power Clean, 1RM Bench Press, 1RM Bench Pull, 1RM Back Squat, Nordic Hamstring test, Margaria-Kalamen test.
4. **Stage 4 - Sprint Tests**: Straight-line sprints (10 m, 20 m, 40 m / 40 yd with split gates).
5. **Stage 5 - Local Muscular Endurance Tests**: Partial curl-up (40 bpm metronome, max 75 reps), Standard/Modified push-up, AFT 2-min hand-release push-up, YMCA bench press (80 lb M / 35 lb F at 60 bpm [30 reps/min]).
6. **Stage 6 - Fatiguing Anaerobic Capacity Tests**: 300-yard (274 m) shuttle (`6 x 50 yd` round-trips, 2 trials with 5-min rest), 90-second box jump test (`18 in H x 30 in W` box).
7. **Stage 7 - Aerobic Capacity Tests**: 1.5-mile (2.4 km) run, 12-minute run, Yo-Yo Intermittent Recovery Test (IRT1 starts at `10 km/h`, IRT2 at `13 km/h`), Maximal Aerobic Speed (`MAS`) test, 30-15 Intermittent Fitness Test (`30-15 IFT`). *Ideally test on a separate day or after >=1 hour recovery.*

### 2. Force-Plate, VBT, and Field Test Protocols (`Ch 14`)

| Test Protocol | Setup & Execution Standards | Key Metrics & Interpretation Rules |
| :--- | :--- | :--- |
| **Isometric Mid-Thigh Pull (IMTP, `#4`)** | Force plate `>=1,000 Hz` (or strain gauge `>=100 Hz`); bar at 2nd-pull power position (**knee 120-145 deg, hip 125-150 deg**, upright torso, clean grip with straps). Warm up at 50%, 70%, 90%; perform `>=3 maximal trials` (3-5 s for Peak Force, 1 s for RFD) with 1-2 min rest. | **Discard trial if**: >50 N fluctuation during 1 s quiet standing, >50 N pre-tension, countermovement dip prior to pull, or peak force occurs at the very end of the pull. Repeat if trials vary `>15%`. Report **Peak Force (N and N/kg)**, **Force at 50/100/150/200/250 ms**, and **RFD**. |
| **Vertical, Squat, Drop, and 10-5 Rebound Jumps (`#8-11`)** | **CMJ**: Hands on hips (or Abalakov with arm swing).<br>**SJ**: Hold `~110 deg` knee angle for 2-3 s, no dip.<br>**Drop Jump**: Step straight out off `20, 30, or 40 cm` box, minimize GCT.<br>**10-5 RJT**: 1 maximal CMJ followed by 10 maximal rebound jumps; average the best 5 RSI trials. | **Eccentric Utilization Ratio (EUR)** = `CMJ / SJ`.<br>**Modified RSI (mRSI)** = `CMJ Height / Time to Takeoff` (diagnoses slow vs. fast impulse generation).<br>**Drop/Rebound RSI** = `Jump Height / Ground Contact Time (GCT)`. |
| **Velocity-Based Testing (VBT, `#13`, `Table 14.13`)** | Linear position transducer or IMU attached to barbell across progressive loads (`20%, 40%, 60%, 80%, 90% 1RM`). **Do NOT predict daily 1RM back squat from L-V regression** (`Figure 14.1` shows systematic overestimation, e.g., predicting 185-191 kg when actual 1RM is 165 kg). | **Barbell Velocity Zones (Lower / Upper Body)**:<br>- **Absolute Strength (80-100% 1RM)**: `<0.50` / `<0.40 m/s`<br>- **Accelerative Strength (60-80%)**: `0.50-0.75` / `0.40-0.60 m/s`<br>- **Strength-Speed (40-60%)**: `0.75-1.0` / `0.60-0.85 m/s`<br>- **Speed-Strength (20-40%)**: `1.0-1.3` / `0.85-1.1 m/s`<br>- **Starting Strength (<20%)**: `>1.3` / `>1.1 m/s` |
| **Nordic Hamstring Test (`#5`, `Table 14.7`)** | Kneel on instrumented board at 90 deg knee flexion; hooks around ankles; lower torso forward under control maintaining straight line from knees to shoulders (no hip flexion). | Measure **Absolute (N)** and **Relative (N/kg)** eccentric peak force (normative mean `~4.74 +/- 1.03 N/kg` across sports) and bilateral asymmetry %. |
| **Maximal Aerobic Speed (MAS, `#23`) & 30-15 IFT (`#24`)** | **MAS**: Cones every 25 m on track; start at `10 km/h`, add `1 km/h` every 2 min until failure.<br>**30-15 IFT**: 40 m shuttle (`30 s run / 15 s walk`), start `8.0 km/h`, add `0.5 km/h` per stage. | **MAS Formula**: `VO2max (mL/kg/min) = 3.5 x MAS (km/h)`.<br>**30-15 IFT**: Final velocity `V_IFT` (typically 15-25% higher than MAS because it includes anaerobic reserve and COD). |

### 3. Statistical Evaluation and Athletic Profiling (`Ch 14`)

1. **Standardize Scores (`Z-Score`)**: `Z = (Athlete Score - Group Mean) / Group SD` (multiply time-based sprint/agility Z-scores by `-1` so positive bars always represent superior performance on profile charts, `Figure 14.33`).
2. **Evaluate Meaningful Change**: Compare pre-to-post difference (`Post - Pre`) against the **Smallest Worthwhile Change (`SWC = 0.2 x SD_between`)** and **Typical Error (`TE`)**:
   - If `Change > SWC` and `Change > TE`, the improvement is both real (exceeds measurement noise) and practically meaningful.
3. **Quantify Training Program Magnitude**: Compute **Effect Size (`ES = (Mean_post - Mean_pre) / SD_pre`)**: `<0.2` trivial, `0.2-0.59` small, `0.6-1.19` moderate, `1.2-1.99` large, `>=2.0` very large.

## A1 - Book Applications (Past Application)

### Case 1: L-V Profile 1RM Overestimation Pitfall (`Ch 14`, `Figure 14.1`)

- **Problem**: A practitioner uses submaximal back squat bar velocities up to 60%, 80%, or 90% 1RM (`V_1RM = 0.20 m/s`) to predict an athlete's daily 1RM.
- **Method & Result**: Even with `R^2 = 0.99`, the 60% L-V regression predicted `191.2 kg`, the 80% regression predicted `186.3 kg`, and the 90% regression predicted `184.8 kg`, whereas the athlete's actual tested 1RM was `165.0 kg` (an overestimation of ~20-26 kg).
- **Conclusion**: Never use submaximal load-velocity regressions to prescribe daily %1RM back squat loads; test 1RM directly (`Figure 18.8`) or use velocity zones (`Table 14.13`) and Set-Repetition Best (`SRB`).

## A2 - Trigger Scenarios and Neighbor Distinction (Future Trigger)

- **Triggers**: User asks to design a testing combine, sequence tests, run an IMTP/CMJ/Drop Jump/Nordic/MAS/30-15 IFT/Yo-Yo protocol, interpret VBT velocity zones, or calculate Z-scores, SWC, and Effect Size.
- **Distinction vs. `06-resistance-program-design-srb-rir.md`**: `03` governs performance assessment, force-plate/VBT diagnostics, and statistical evaluation; `06` turns those diagnostic profiles into resistance training workouts.

## E - Executable Steps (Execution)

1. **Follow the 5-Step Scientific Process**: Define the performance question and select valid, reliable, sport-specific tests (`Table 13.1`).
2. **Screen Environment & Sequence Battery**: Verify heat/humidity limits (`Figure 13.2`) and order tests strictly from Stage 1 (Nonfatiguing) -> Stage 7 (Aerobic).
3. **Execute Standardized Protocols**: Enforce quiet-standing/countermovement quality checks on force plates (`IMTP`, `CMJ`, `SJ`, `10-5 RJT`), use electronic timing gates (handheld stopwatches read up to **0.24 s faster** due to reaction delay), and take skinfolds on dry right-side skin *before* exercise.
4. **Compute Profile & Magnitude Metrics**: Calculate `Z-scores`, `SWC (0.2 x SD)`, and `ES` to identify individual training priorities (`Figures 14.33, 18.3-18.5`).

## B - Boundary and Failure Modes (Boundary)

- **Failure Mode (Comparing Jump-and-Reach Vertec Scores to Force-Plate Flight-Time Jump Heights)**: Jump-and-reach tests include shoulder elevation/reach and measure relative to flat-footed reach, whereas force plates measure center-of-mass displacement from takeoff height with hands on hips; never use the two interchangeably (`Ch 14`).
- **Failure Mode (Handheld Stopwatch Bias)**: Handheld sprint times are systematically **~0.24 s faster** than electronic timing gates; never compare hand-timed scores to electronic normative tables (`Table 14.30`).

## Related Capabilities

- `composes-with`: `06-resistance-program-design-srb-rir.md`, `08-speed-cod-agility-development.md`
- `contrasts-with`: `06-resistance-program-design-srb-rir.md`

## Triple Verification Audit

- **V1 Source Sufficiency**: Verified against Ch 13 (`Table 13.1, Figs 13.1-13.2`) and Ch 14 (`Protocols 1-37, Tables 14.1-14.37`).
- **V2 Executability**: Deterministic 7-stage sorting, IMTP/jump rejection rules, VBT velocity zones, and statistical formulas.
- **V3 Task Utility**: Ensures valid, uncontaminated athlete diagnostics and data-driven programming.
