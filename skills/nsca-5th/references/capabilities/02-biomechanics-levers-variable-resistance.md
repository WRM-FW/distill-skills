# Capability 02: Biomechanics, Levers, Variable Resistance, and AEL

## R - Source Anchor (Reading)

- **Source Location**: Chapter 2 (Biomechanics of Resistance Exercise, `Table 2.1`, `Figures 2.1-2.15`, `Equations 2.1-2.11`) and Chapter 17 (Variable Resistance, Chains, Bands, Accentuated Eccentric Loading, and Unilateral Training, `Tables 17.1-17.2`, `Figures 17.1-17.8`).
- **Core Mechanism**:
  - **Musculoskeletal Levers & Mechanical Advantage (`Ch 2`)**:
    - `Torque (N*m) = Force (N) x Moment Arm (m)`
    - `Mechanical Advantage (MA) = Internal Muscle Moment Arm (M_M) / External Resistive Moment Arm (M_R)`
    - **First-Class Lever**: `F_M` and `F_R` act on opposite sides of the fulcrum (e.g., forearm triceps extension, `MA < 1.0`).
    - **Second-Class Lever**: `F_M` and `F_R` act on the same side with `M_M > M_R` (`MA > 1.0`, mechanical advantage; e.g., plantarflexion standing heel raise).
    - **Third-Class Lever**: `F_M` and `F_R` act on the same side with `M_M < M_R` (`MA < 1.0`, mechanical disadvantage; e.g., biceps curl). Most human muscles operate at `MA < 1.0`, generating high internal tendon forces to achieve high distal movement velocity.
    - **Tendon Insertion Trade-Off**: Tendons inserting farther from the joint center increase `M_M` and lifting torque in slow movements (powerlifting) but require greater muscle shortening per degree of joint rotation, reducing force at high angular velocities (tennis/throwing).
  - **Impulse-Momentum, Work, and Power (`Equations 2.1-2.7`)**:
    - **Impulse-Momentum**: `F x dt = m x dv` (net impulse dictates change in velocity; vertical jump takeoff velocity `TOV = sqrt(2 x 9.81 x Jump Height)`).
    - **Mechanical Work**: `W = F x d`, or total mechanical energy change (`PE = m x g x h` + `KE = 0.5 x m x v^2`). Lowering a barbell performs **negative work** (`-W`).
    - **Mechanical Power**: `P = Work / dt`. **Critical 5th Edition Guardrail**: Do not confuse 1,000 Hz **instantaneous peak power** (work over 1 ms and 1-2 mm displacement) with **mean propulsion phase power** (`Total Propulsion Work / Propulsion Time`).
  - **Titin & Force-Velocity Relationship (`Figures 2.12-2.13`)**:
    - **Titin** is the third contractile/mechanosensing sarcomeric filament; during eccentric actions beyond resting length, Ca2+ influx causes spring-like titin to stiffen, increasing eccentric force production, aligning myosin filaments, and triggering hypertrophic trophic signaling.
    - Eccentric torque capability exceeds isometric and concentric torque (up to ~50% higher, creating the **eccentric strength deficit**, `Figure 17.5`).
  - **Five Sources of Resistance (`Equations 2.8-2.11`)**:
    1. **Gravity**: `F_g = m x 9.81`; horizontal moment arm changes resistive torque across the ROM (e.g., **low-bar squat** increases trunk lean, lengthening hip moment arm and shortening knee moment arm; **high-bar squat** stays upright, increasing knee moment arm).
    2. **Inertia**: `F = m x a`; explosive acceleration increases resistance early in the ROM and reduces it during late-phase deceleration.
    3. **Friction**: `F_R = k x F_N`; static friction coefficient (`u_s`) > dynamic sliding friction (`u_d`) in sled pushing/pulling (`45-136 kg` sleds: `u_s = 0.39-0.47`, `u_d = 0.31-0.35`).
    4. **Fluid Resistance**: `F_R = k x v` (surface drag + form drag; concentric-only in hydraulic/pneumatic cylinders without eccentric return).
    5. **Elasticity**: `F_R = k x x` (resistance increases with stretch length `x`, matching ascending human strength curves when paired with free weights).

## I - Methodology Skeleton (Interpretation)

### 1. Variable Resistance: Chains and Bands (`Tables 17.1-17.2`)

- **Load Adjustment Formula (`Baker Rule`)**:
  1. Determine the athlete's target constant-weight RM load (e.g., `5RM = 120 kg`).
  2. Calculate the variable resistance at the **bottom** (`R_bottom`) and **top** (`R_top`) of the lift, and compute the mean: `R_avg = (R_bottom + R_top) / 2`.
  3. Subtract `R_avg` from the target constant load to set the barbell weight: `Barbell Weight = Target RM Load - R_avg`.
- **Chain Mass Reference (`Table 17.1`, for 150 cm [59 in] length)**:
  - `6.4 mm (1/4 in)` = `3.8 kg (8.4 lb)` | `9.5 mm (3/8 in)` = `5.6 kg (12.3 lb)` | `12.7 mm (1/2 in)` = `11.1 kg (24.5 lb)` | `19.1 mm (3/4 in)` = `21.0 kg (46.3 lb)` | `22.2 mm (7/8 in)` = `32.4 kg (71.4 lb)` | `25.4 mm (1 in)` = `42.0 kg (92.6 lb)`.
  - Hang heavy chains from a light support chain so links furl completely onto the floor at the bottom of the squat/bench press and unfurl linearly to the top.
- **Resistance Band Tension Prediction Equations (`Table 17.2`, where `x` = stretched length in cm from 110 to 150 cm)**:
  - **Yellow (14 mm)**: `2.6 to 11.5 kg` (`Y = -0.003x^2 + 0.98x - 69.82`)
  - **Red (22 mm)**: `4.6 to 19.2 kg` (`Y = -0.004x^2 + 1.38x - 99.49`)
  - **Blue (32 mm)**: `8.5 to 27.3 kg` (`Y = -0.004x^2 + 1.60x - 114.86`)
  - **Green (48 mm)**: `11.8 to 49.3 kg` (`Y = -0.007x^2 + 2.43x - 179.56`)
  - **Black (67 mm)**: `15.4 to 57.2 kg` (`Y = -0.010x^2 + 3.73x - 269.21`)

### 2. Accentuated Eccentric Loading (AEL) Prescription Matrix (`Figures 17.6-17.8`)

| AEL Category & Modality | Relative Strength Prerequisite | Eccentric Phase Load | Concentric Phase Load | Recommended Set Structure (`Figure 17.8`) |
| :--- | :--- | :--- | :--- | :--- |
| **Submaximal AEL - Plyometric Jumps** (CMJ, Box, Drop, Depth Jump holding DBs/KBs/Bands released at bottom) | Bench `< 1.5x BW` or Squat `< 2.0x BW` | **+20-30% Body Mass** (or 60-90% 1RM) | **Body Mass only** (implements released at transition) | Release dumbbells/kettlebells at the bottom of the countermovement prior to concentric takeoff |
| **Submaximal AEL - Resistance Exercises** (Bench throw, Squat, Leg press w/ weight releasers) | Bench `< 1.5x BW` or Squat `< 2.0x BW` | **60-90% 1RM** | **30-50% 1RM** | Cluster sets (`15-40 s` inter-rep rest) or AEL on Rep 1 only |
| **Maximal AEL - Resistance Exercises** (Back/Front Squat, Bench Press, Leg Press) | Bench `>= 1.5x BW` and Squat `>= 2.0x BW` | **100% Concentric 1RM** | **30-80% 1RM** | Cluster sets (`15-40 s` inter-rep rest to reattach weight releasers) or Hybrid 3-rep clusters |
| **Supramaximal AEL - Resistance Exercises** (Back/Front Squat, Bench Press, Leg Press) | Bench `>= 1.5x BW` and Squat `>= 2.0x BW` | **105-120% Concentric 1RM** (differential `>40%` vs. concentric load) | **30-90% 1RM** (e.g., 110% ecc / 65% con) | **Option A**: Cluster sets (`30 s` rest between every rep)<br>**Option B**: AEL on Rep 1 of a 5-rep continuous set (potentiates Reps 3-5)<br>**Option C**: Hybrid clusters of 2-3 reps (`AEL on Rep 1 + 1-2 con reps`, `25-35 s` intraset rest) |

### 3. Bilateral Deficit vs. Bilateral Facilitation (`Ch 5 & 17`)

- **Untrained, Weaker, or Injured Athletes**: Exhibit a **bilateral deficit** (sum of unilateral forces > bilateral force); unilateral exercises (split squat, lunge, step-up, single-leg RDL) are highly effective for building foundational strength and correcting asymmetries.
- **Trained or Stronger Athletes**: Exhibit **bilateral facilitation** (increased voluntary agonist neural drive during bilateral contractions); use bilateral ground-based free-weight lifts as the primary maximal strength driver and unilateral lifts as supplemental assistance.

## A1 - Book Applications (Past Application)

### Case 1: Rugby Vertical Jump Impulse Analysis (`Ch 2 Sidebar`)

- **Problem**: Comparing two rugby cohorts jumping `0.37 m` (95.2 kg, TOV `2.694 m/s`, required net impulse `256.6 N*s` over `0.232 s` = `1,105.6 N` mean net force) vs. `0.44 m` (98.2 kg, TOV `2.938 m/s`, required net impulse `288.5 N*s`).
- **Conclusion**: The higher-jumping cohort achieved 16% greater jump height despite applying 7% less peak force by extending force application over 17% more time (`Impulse = F x dt`), proving that impulse - not instantaneous peak force or 1-ms peak power - governs takeoff velocity.

### Case 2: 5RM Bench Press with Chains or Bands (`Ch 17`)

- **Problem**: An athlete with a `150 kg` 5RM bench press wants to train at a 5RM equivalent using resistance bands that provide `0 kg` tension at the chest and `26.6 kg` total tension at lockout.
- **Application**: Mean band tension = `(0 + 26.6) / 2 = 13.3 kg`. Set barbell weight to `150 - 13.3 = 136.7 kg` (~136-137 kg) so the combined bar + band resistance averages 150 kg across the ROM.

## A2 - Trigger Scenarios and Neighbor Distinction (Future Trigger)

- **Triggers**: User asks to analyze levers/torque/planes (`Figure 2.10`), calculate impulse/work/power/jump TOV, compute chain or band variable resistance loads, or program Accentuated Eccentric Loading (AEL).
- **Distinction vs. `05-exercise-technique-spotting-nontraditional.md`**: `02` handles biomechanical math, lever/torque analysis, and chain/band/AEL loading calculations; `05` handles physical setup, grips, spotting, and movement execution checklists.

## E - Executable Steps (Execution)

1. **Analyze Movement Mechanics**: Identify plane (sagittal/frontal/transverse), lever class, horizontal moment arm alterations (e.g., high-bar vs. low-bar squat), and impulse demands (`F x dt = m x dv`).
2. **Compute Variable Resistance Loads (If Applicable)**: Lookup chain mass (`Table 17.1`) or band tension (`Table 17.2`), compute `(Top + Bottom) / 2`, and subtract from the target constant RM load.
3. **Prescribe AEL Set Structure (If Applicable)**: Verify athlete relative strength (`>=1.5x BW` bench / `>=2.0x BW` squat for maximal/supramaximal AEL), set weight releasers to disengage `5-10 cm (2-4 in)` above the bottom position, and select Cluster, Rep-1-Only, or Hybrid 3-Rep Cluster structure (`Figure 17.8`).

## B - Boundary and Failure Modes (Boundary)

- **Failure Mode (Elastic Bands on Vertical Jumps)**: Attaching heavy elastic bands to vertical jumps provides minimal resistance early in the squat where glutes/quads are strongest, while pulling the jumper violently back toward the floor from peak flight, increasing landing velocity and injury risk (`Ch 2`).
- **Failure Mode (Training on Unstable Surfaces for Strength/Power)**: Performing squats or presses on Swiss balls/BOSU balls reduces agonist force, power output, and RFD by **>=30%** (`Ch 5 & 17`); reserve instability devices for injury rehabilitation or isolated core progressions.

## Related Capabilities

- `composes-with`: `05-exercise-technique-spotting-nontraditional.md`, `06-resistance-program-design-srb-rir.md`
- `contrasts-with`: `05-exercise-technique-spotting-nontraditional.md`

## Triple Verification Audit

- **V1 Source Sufficiency**: Verified against Ch 2 (`Equations 2.1-2.11, Table 2.1, Fig 2.10`) and Ch 17 (`Tables 17.1-17.2, Figs 17.5-17.8`).
- **V2 Executability**: Exact mechanical equations, chain/band lookup tables, and AEL decision trees.
- **V3 Task Utility**: Prevents biomechanical misloading and enables precise variable/eccentric overload prescription.
