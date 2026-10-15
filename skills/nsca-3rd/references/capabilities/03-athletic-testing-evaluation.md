# Capability 03: Athletic Performance Testing and Evaluation

## R - Source Anchor (Reading)

- **Source Location**: Chapter 11 (Principles of Test Selection and Administration, `Table 11.1`) and Chapter 12 (Selected Test Protocols and Scoring Data).
- **Core Mechanism**:
  - **Validity**: Degree to which a test measures what it is supposed to measure (`Construct`, `Face`, `Content`, `Criterion-Referenced` [Concurrent, Predictive, Discriminant]).
  - **Reliability**: Consistency/repeatability across trials (`Intrasubject variability`, `Interrater reliability/objectivity`, `Intrarater reliability`).
  - **Environmental Temperature & Humidity Ceiling (`Table 11.1`)**: Strenuous outdoor/unconditioned exercise testing must be suspended when ambient temperature exceeds safety limits for relative humidity:
    - **0-20% RH**: Limit `95 F (35 C)`
    - **21-40% RH**: Limit `90 F (32 C)`
    - **41-60% RH**: Limit `85 F (29 C)`
    - **61-80% RH**: Limit `80 F (27 C)`
    - **81-100% RH**: Limit `75 F (24 C)`

## I - Methodology Skeleton (Interpretation)

### 1. Mandatory 7-Stage Test Battery Sequence (`Chapter 11`)
Tests must be ordered by neural demand and energy system depletion Rate/Recovery so earlier tests never contaminate later tests:

1. **Stage 1 - Nonfatiguing Tests**: Height, weight, flexibility (sit-and-reach), skinfold/girth body composition, vertical jump, standing long jump.
2. **Stage 2 - Agility Tests**: T-test, Hexagon test, Pro Agility (20-yard shuttle).
3. **Stage 3 - Maximum Power and Strength Tests**: 1RM Power Clean, 1RM Bench Press, 1RM Back Squat, Margaria-Kalamen stair sprint test.
4. **Stage 4 - Sprint Tests**: 10- to 40-yard (9-37 m) sprint (with/without split times).
5. **Stage 5 - Local Muscular Endurance Tests**: Partial curl-up test, push-up test, YMCA bench press test.
6. **Stage 6 - Fatiguing Anaerobic Capacity Tests**: 300-yard (274 m) shuttle, 400 m run.
7. **Stage 7 - Aerobic Capacity Tests**: 1.5-mile (2.4 km) run, 12-minute Cooper run, Yo-Yo intermittent recovery test (ideally administered on a **separate day**, or at minimum after a **>=1-hour rest period**).

- **Rest Between Trials/Tests**: Allow **2-3 minutes** between repeated trials of the same test and at least **3-5 minutes** between different test stations.

### 2. Canonical Parameter-to-Protocol Mapping (`Chapter 12`)

| Athletic Parameter | Primary NSCA Field/Lab Tests | Key Protocol Constraints |
| :--- | :--- | :--- |
| Low-Speed Muscular Strength | 1RM Bench Press, 1RM Back Squat | Measure true 1RM within 3-5 testing sets after warm-up (`Figure 15.1`) |
| High-Speed Muscular Strength / Anaerobic Power | 1RM Power Clean, Standing Long Jump, Vertical Jump, Margaria-Kalamen Test | Margaria-Kalamen: sprint stairs 3 steps at a time from 6 m run-up; `Power (W) = (Weight[N] x Vertical height[m]) / Time[s]` |
| Anaerobic Capacity | 300-Yard (274 m) Shuttle | 6 round-trips between lines 25 yards apart (`12 x 25 yd`); two trials with 5 min rest, average both times |
| Local Muscular Endurance | Partial Curl-Up, Push-Up (Army/ACSM), YMCA Bench Press | YMCA Bench: 80 lb (men) or 35 lb (women) at 30 reps/min (60 bpm metronome) to cadence failure |
| Aerobic Capacity | 1.5-Mile (2.4 km) Run, 12-Minute Run | Maximal sustained effort on flat track; avoid high heat/humidity (`Table 11.1`) |
| Agility | T-Test (forward/lateral/backward), Hexagon Test, Pro Agility (5-10-5 yd) | Pro Agility: straddle center line, sprint 5 yd left, 10 yd right, 5 yd back through center |
| Flexibility & Body Composition | Sit-and-Reach, Goniometry; 3- or 7-Site Skinfolds (Jackson-Pollock) | Skinfolds taken on right side of body before exercise (dehydration/hyperemia alters skinfold thickness) |

## A1 - Book Applications (Past Application)

### Case 1: Test Sequence Audit (`Chapter 11 Study Question 5`)

- **Problem**: A coach needs to schedule 4 tests: (1) T-test, (2) 1RM bench press, (3) 1RM power clean, (4) 1-minute sit-up test.
- **Application**: T-test (Stage 2 Agility) goes first; between 1RM power clean and 1RM bench press (both Stage 3), the multi-joint total-body power clean precedes the upper-body bench press; the 1-minute sit-up test (Stage 5 Local Muscular Endurance) goes last -> **1, 3, 2, 4**.

## A2 - Trigger Scenarios and Neighbor Distinction (Future Trigger)

- **Triggers**: User asks to design a team combine/testing day, select valid tests for a sport, order a test battery, or evaluate test results (percentile ranks, Z-scores, magnitude-based statistics).
- **Distinction vs. `05-resistance-program-design.md`**: `03` governs multi-parameter combine testing and sequence rules; `05` converts test outputs into daily training prescriptions.

## E - Executable Steps (Execution)

1. **Select Metabolic & Movement-Valid Tests**: Match test energy system and joint action to the sport's needs analysis (`Table 5.1`).
2. **Check Environmental & Health Clearance**: Verify medical clearance and confirm ambient temperature/humidity is below `Table 11.1` ceilings.
3. **Order the Test Battery**: Sort all selected tests strictly into Stages 1 -> 7, separating Stage 7 Aerobic tests to a different day (or >=1 hr after Stage 6).
4. **Standardize Administration & Scoring**: Use identical raters, pretest warm-ups (general + specific), 2-3 min inter-trial recovery, and convert raw scores to percentiles or Z-scores (`Z = (Score - Mean) / SD`).

## B - Boundary and Failure Modes (Boundary)

- **Failure Mode (Taking Skinfolds Post-Workout)**: Exercise shifts fluid to the skin and increases blood flow, inflating skinfold thickness and invalidating body density equations.
- **Failure Mode (Using 1RM Power Clean for Novice Power Testing)**: Because the power clean is highly technique-dependent, novices fail due to motor skill limitations rather than true muscular power capacity; use Vertical Jump or Standing Long Jump for novices instead (`Chapter 12`).

## Related Capabilities

- `composes-with`: `01-bioenergetics-interval-prescription.md`, `05-resistance-program-design.md`

## Triple Verification Audit

- **V1 Source Sufficiency**: Verified against Ch 11 (`Table 11.1`, Sequence of Tests) and Ch 12 (Test Protocols).
- **V2 Executability**: Deterministic 7-stage sorting algorithm and environmental threshold check.
- **V3 Task Utility**: Eliminates fatigue contamination in athletic testing batteries.
