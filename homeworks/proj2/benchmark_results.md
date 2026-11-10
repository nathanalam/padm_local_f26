# Agent Benchmarks

**Author:** Nathan Alam

## Overview

For each combination of environment and agent, I ran 10 episodes. With a discount rate of 0.999, and a +1 if rescue succeeded, -1 if
burned, and 0 otherwise, I calculated the reward.

These were the agent settings:

```
    ("Random", RolloutLookaheadAgent(problem, receding_horizon=0)),
    ("Rollout-40", RolloutLookaheadAgent(problem, receding_horizon=40)),
    ("Determinized A*", FireMDPDeterminizedAStarAgent(problem)),
    ("MCTS-10", MCTSAgent(problem, iteration_budget=10, receding_horizon=40)),
    ("MCTS-50", MCTSAgent(problem, iteration_budget=50, receding_horizon=40)),
```

I measured success as the fraction of the episodes where the patient was rescued.

## Results

| Environment | Agent | Mean ± SD | Min | Max | Success | Time (s) |
|---|---|---:|---:|---:|---:|---:|
| maze | Random | +0.00 ± 0.00 | +0.00 | +0.00 | 0% | 0 |
| maze | Rollout-40 | +0.49 ± 0.49 | +0.00 | +0.99 | 50% | 3 |
| maze | Determinized A* | +0.99 ± 0.00 | +0.99 | +0.99 | 100% | 0 |
| maze | MCTS-10 | +0.99 ± 0.00 | +0.98 | +0.99 | 100% | 66 |
| maze | MCTS-50 | +0.99 ± 0.00 | +0.98 | +0.99 | 100% | 56 |
| just_wait | Random | +0.34 ± 0.87 | -1.00 | +0.96 | 70% | 0 |
| just_wait | Rollout-40 | +0.76 ± 0.59 | -1.00 | +0.98 | 90% | 3 |
| just_wait | Determinized A* | +0.96 ± 0.02 | +0.91 | +0.98 | 100% | 4 |
| just_wait | MCTS-10 | +0.96 ± 0.01 | +0.93 | +0.98 | 100% | 155 |
| just_wait | MCTS-50 | +0.75 ± 0.57 | -0.95 | +0.97 | 90% | 222 |
| the_circle | Random | +0.95 ± 0.02 | +0.91 | +0.98 | 100% | 0 |
| the_circle | Rollout-40 | +0.98 ± 0.01 | +0.97 | +0.99 | 100% | 4 |
| the_circle | Determinized A* | +0.99 ± 0.00 | +0.99 | +0.99 | 100% | 0 |
| the_circle | MCTS-10 | +0.99 ± 0.01 | +0.97 | +0.99 | 100% | 90 |
| the_circle | MCTS-50 | +0.98 ± 0.01 | +0.97 | +0.99 | 100% | 98 |
| the_choice | Random | -0.01 ± 0.99 | -1.00 | +0.99 | 50% | 0 |
| the_choice | Rollout-40 | -0.21 ± 0.97 | -1.00 | +0.99 | 40% | 1 |
| the_choice | Determinized A* | -0.40 ± 0.91 | -1.00 | +0.99 | 30% | 0 |
| the_choice | MCTS-10 | +0.19 ± 0.97 | -1.00 | +0.99 | 60% | 36 |
| the_choice | MCTS-50 | -0.01 ± 0.99 | -1.00 | +0.99 | 50% | 34 |

## Findings

As roughly expected, the random agent is uniformly the worst agent of them all, with very low odds of success for any of the environments. The Rollout-40 agent is marginally better in that is chooses the best path among 40 horizons, but it is still not intelligently navigating through the space in a way that is reasoning about the fire or the path to the goal. Because these random agents do act fairly quickly, though, either to their demise or to the next step, they are also the fastest.

Determinized A* performs well on `the_maze` and `the_circle`, as it has almost complete success and is among the fastest algorithms by a significant margin, because these environments are more or less deterministic. It also does well in `just_wait` because it can also just choose to wait out the fire until it clears, at which point it is once again deterministic. 

Determinized A* struggles though with `the_choice` because it does not take into account the optionality from entering the room that allows evasions, as it only selects and considers the route to the hospital. MCTS of both forms perform much better because they weigh and take into account the branches of the state tree that lead to better outcomes in a larger number of potential scenarios.

Increasing the horizon from 10 to 50 for MCTS does not seem to help, however, as it seems to take a bit more time and produces little additional value. In fact, a few seem to do worse, but it is likely within noise for the sample size in this test.
