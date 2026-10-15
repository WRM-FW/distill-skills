# Capability 01: Bioenergetics and Metabolic Interval Prescription

## R - Source Anchor (Reading)

- **Source Location**: Chapter 1 (Tables 1.1-1.2), Chapter 2 (Tables 2.1-2.7), Chapter 5 (Table 5.1).
- **Core Mechanism**: Human muscle contraction relies on ATP hydrolysis (`ATP + H2O -> ADP + Pi + H+ + Energy`), replenished by three integrated energy systems ranked inversely by ATP production rate versus total capacity (`Table 2.4`):
  1. **Phosphagen System**: Rate Rank #1 (fastest), Capacity Rank #5 (least); dominates 0-6 s of maximal effort via creatine kinase (`ADP + CP <-> ATP + Cr`) and adenylate kinase (`2 ADP <-> ATP + AMP`).
  2. **Fast Glycolysis**: Rate Rank #2, Capacity Rank #4; dominates 6-30 s (with phosphagen) and 30 s-2 min (alone), converting pyruvate to lactate to regenerate NAD+ rapidly.
  3. **Slow Glycolysis**: Rate Rank #3, Capacity Rank #3; channels pyruvate into mitochondria when oxygen supply meets demand (2-3 min transition with fast glycolysis).
  4. **Oxidative Phosphorylation (Carbohydrates -> Fats/Proteins)**: Rate Ranks #4-#5, Capacity Ranks #2-#1; dominates events >3 min. One glucose molecule yields 38 net ATP (or 40 gross from muscle glycogen); one 18-carbon triglyceride yields 463 ATP (`Tables 2.1-2.2`).
- **Substrate Recovery Kinetics**: Complete ATP resynthesis takes 3-5 minutes; complete creatine phosphate (CP) resynthesis takes ~8 minutes (`50%` restored in 30 s, `75%` in 60 s, `98%` in 3 min). Muscle glycogen repletion requires 24 hours with 0.7-1.0 g/kg carbohydrate every 2 hours post-exercise.

## I - Methodology Skeleton (Interpretation)

Metabolic specificity requires matching the training work duration, exercise intensity (% maximal power), and work-to-rest (W:R) ratio to the target sport's dominant energy system and limiting bioenergetic factor:

| Target Energy System | % Max Power | Typical Work Bout Duration | Prescribed Work-to-Rest Ratio (W:R) | Primary Limiting Factor (`Table 2.5`) |
| :--- | :--- | :--- | :--- | :--- |
| Phosphagen System | 90-100% | 5-10 seconds | 1:12 to 1:20 | ATP and Creatine Phosphate depletion |
| Fast Glycolysis | 75-90% | 15-30 seconds | 1:3 to 1:5 | Lower pH (H+ acidosis) & Muscle glycogen |
| Fast Glycolysis + Oxidative | 30-75% | 1-3 minutes | 1:3 to 1:4 | Lower pH (H+ acidosis) & Muscle glycogen |
| Oxidative System | 20-30% | >3 minutes | 1:1 to 1:3 | Muscle/liver glycogen & Fat stores |

## A1 - Book Applications (Past Application)

### Case 1: High-Intensity Intermittent Team Sport (American Football / Basketball)

- **Context**: American football plays last ~4-6 s separated by 25-40 s huddles (`Table 5.1`: High Phosphagen, Moderate Anaerobic Glycolysis).
- **Application**: Prescribe 5-10 s sprints/drills at 90-100% max power with 1:12 to 1:20 recovery during phosphagen-focused conditioning so CP stores replenish before the next bout, preventing premature shift into slow glycolysis.

### Case 2: 400 m Track / Wrestling / Boxing (`Table 2.5`)

- **Context**: Maximal effort lasting 45 s to 3 min relies heavily on fast glycolysis (50-75% anaerobic contribution at 60-90 s on cycle ergometry, `Table 2.6`).
- **Application**: Use 15-30 s bouts at 75-90% max power with 1:3 to 1:5 rest (or 1-3 min bouts at 30-75% with 1:3 to 1:4 rest) to overload H+ buffering capacity and glycolytic enzyme activity (PFK, LDH).

## A2 - Trigger Scenarios and Neighbor Distinction (Future Trigger)

- **Triggers**: User asks to design conditioning intervals, work-to-rest ratios, energy system training (ATP-CP, lactic/glycolytic, aerobic), or metabolic analysis of a sport.
- **Distinction vs. `08-aerobic-endurance-program-design.md`**: Use `01` for bioenergetic pathway diagnosis and anaerobic/mixed interval W:R ratios (`Table 2.7`); use `08` for distance endurance modes (LSD, pace/tempo, fartlek, Karvonen HR zones).

## E - Executable Steps (Execution)

1. **Clock the Sport Work-Rest Profile**: Measure average high-intensity rally/play duration, rest between plays, and total contest duration.
2. **Map to Energy System Proportion**: Assign primary and secondary energy systems using `Table 2.3` (0-6 s Phosphagen; 6-30 s Phosphagen+Fast Glycolysis; 30 s-2 min Fast Glycolysis; 2-3 min Fast Glycolysis+Oxidative; >3 min Oxidative).
3. **Prescribe Interval Parameters**: Output exact work duration, % max power intensity, and W:R ratio from `Table 2.7`, plus post-session glycogen/CP recovery windows.

## B - Boundary and Failure Modes (Boundary)

- **Failure Mode (Insufficient Rest in Phosphagen Training)**: Using a 1:1 or 1:2 W:R ratio for 10 s maximal sprints prevents CP resynthesis (which requires 3-8 min), converting a speed/power session into a fatiguing glycolytic session and degrading motor unit recruitment quality.
- **Failure Mode (Combo Training Interference)**: Combining high-volume aerobic endurance training with maximal anaerobic power training blunts Type II fiber hypertrophy and rate of force development (`Chapter 5`).

## Related Capabilities

- `composes-with`: `05-resistance-program-design.md`, `08-aerobic-endurance-program-design.md`

## Triple Verification Audit

- **V1 Source Sufficiency**: Verified against Ch 1-2 (`Tables 1.1-1.2, 2.1-2.7`) and Ch 5 (`Table 5.1`).
- **V2 Executability**: Deterministic lookup from rally duration -> energy system -> W:R ratio.
- **V3 Task Utility**: Prevents metabolic mismatch and chronic conditioning fatigue.
