# 🧩 Trajectory Planning and Quantum Optimization: Four Repository Reviews

Reviewed on October 18, 2026. This is a source review, not an execution report. The integration designs and experiments below are proposals, not upstream features or reproduced results.

## 🧭 Comparison at a glance

| Repository | Actual role | Candidate SAR use | Main gap |
| :--- | :--- | :--- | :--- |
| OpenQuantumComputing/QAOA | Modular quantum optimization library | Small discrete task-allocation experiments | Requires an explicit UAV problem encoding and simulator adapter |
| SWAN | Drone light-show choreography pipeline | Reuse trajectory coordination and validation ideas | Its objective is choreography, not finding survivors |
| uav-trajectory-optimization-pso | Single-UAV waypoint optimization | Classical route-planning baseline | Requires multi-UAV coordination, mission sensing, and timing |
| qaoa_training_pipeline | Classical training of QAOA circuit parameters | Study parameter initialization and training costs | Trained angles are neither UAV assignments nor executable trajectories |

## ⚛️ OpenQuantumComputing/QAOA

**Observed:** The library separates problems, mixers, initial states, optimizers, and backends. It includes QUBO examples and supports experimentation with QAOA components. Its objective convention distinguishes the natural objective from the energy minimized by the algorithm. This makes sign handling a necessary integration check. [README at reviewed commit](https://github.com/OpenQuantumComputing/QAOA/blob/3ba1d8d54f0fc47b1d0fd963fae0197dd0b551f9/README.md).

**Proposed use:** Encode assignment of a few search sectors to available UAVs. Compare alternative penalties or feasible-state mixers while keeping travel-cost estimates and detection rewards fixed.

**Limit:** No UAV sensing, flight dynamics, or SAR mission logic was established by this review. A low circuit energy alone does not establish a feasible assignment or successful search. Circuit simulation also does not establish a quantum speedup.

**First experiment:** Exhaustively enumerate a tiny assignment instance, then compare sampled QAOA solutions against its exact optimum. Report feasibility, objective gap, shot budget, circuit depth, and total optimization time.

## 🎆 SWAN

**Observed:** SWAN turns text prompts into drone light-show choreography. Its documented stages include generated video, segmentation, point tracking, trajectory construction, and simulation. The simulation code combines AXSwarm control with crazyflow. Its `CollisionlessSim` disables contact physics, while `check_collisions_fast` checks pairwise distances at sampled times. [README](https://github.com/Data-Science-in-Mechanical-Engineering/SWAN/blob/4915d4842498ec601b1bbea9c5786e2e8ee0ac87/README.md), [simulation implementation](https://github.com/Data-Science-in-Mechanical-Engineering/SWAN/blob/4915d4842498ec601b1bbea9c5786e2e8ee0ac87/swan/simulation.py).

**Proposed use:** Study whether its trajectory coordination and post-simulation separation checks can be adapted to a search formation. Replace artistic targets with search waypoints and add an independent mission evaluator.

**Limit:** Generated imagery is not an observed disaster scene. Pairwise separation at sampled times is not a continuous-time collision guarantee, and disabling contact dynamics does not model collision consequences. A light-show workflow does not establish coverage, survivor detection, endurance, or communication performance.

**First experiment:** Supply a small, deterministic search formation rather than generated video. Measure tracking error, minimum separation, solver failures, and collisions under finer temporal sampling. This requires adaptation and is not an existing SAR example.

## 🛤️ UAV trajectory optimization with PSO

**Observed:** The project optimizes intermediate waypoints between a start and goal in a 2D obstacle environment. `objective.py` combines path length, an energy proxy, turning smoothness, collision and boundary penalties, and a backward-progress penalty. Collision cost uses interpolated path samples, with 35 samples per segment in that call. The energy proxy depends on segment lengths and turning rather than a calibrated electrical power model. [Objective implementation](https://github.com/Mahek010/uav-trajectory-optimization-pso/blob/c38b16ea8444fc1efd8d9b1b72d6f96583635540/objective.py), [README](https://github.com/Mahek010/uav-trajectory-optimization-pso/blob/c38b16ea8444fc1efd8d9b1b72d6f96583635540/README.md).

**Proposed use:** Use it as a classical baseline for routing a UAV toward a selected search sector or reported target. Treat its output as a geometric path that still needs timing and tracking validation.

**Limit:** PSO particles are candidate solutions, not collaborating aircraft. Finite penalties permit tradeoffs with constraint violations. Sampled obstacle checks can miss intersections between samples. The progress penalty can discourage detours that are useful for exploration. Energy-proxy improvement is not measured battery savings.

**First experiment:** Run multiple seeds, independently check each line segment against expanded circular obstacles, and report feasible-run rate separately from cost. Add timing and inter-UAV separation before extending to multiple vehicles.

## 🧠 QAOA training pipeline

**Observed:** This project trains QAOA parameters using classical evaluators, including light-cone and matrix-product-state approaches. Its README uses a maximization convention by default and returns angles ordered as all beta values followed by all gamma values. The package metadata declares Python 3.11 or newer and optional tensor-network dependencies. [README](https://github.com/qiskit-community/qaoa_training_pipeline/blob/4bad7bc13e132d29f5545d60fa655a6229baa05b/README.md), [package metadata](https://github.com/qiskit-community/qaoa_training_pipeline/blob/4bad7bc13e132d29f5545d60fa655a6229baa05b/pyproject.toml).

**Proposed use:** Investigate parameter preparation for small task-allocation Hamiltonians before sampling a circuit. Evaluate whether parameter reuse across related mission instances reduces training cost.

**Limit:** Classical evaluation costs depend on circuit and problem structure; they are not uniformly inexpensive. Approximate evaluators require accuracy checks. Transferring angles to another library requires reconciling objective signs, Hamiltonian scaling, mixer conventions, parameter ordering, and qubit ordering.

**First experiment:** For one tiny Hamiltonian, compare evaluator energies with exact statevector evaluation at fixed angles. Only after agreement, test trained angles and decode sampled bitstrings into assignments.

## 🔗 Proposed integration into a SAR workflow

The following architecture is an editorial proposal. None of these four projects was verified as already integrated with DSSE, SwarmSAR, XTDrone, or Pegasus.

| Stage | Input | Output | Validation |
| :--- | :--- | :--- | :--- |
| Mission estimation | Target beliefs, UAV state, map | Sector rewards and travel estimates | Prevent access to hidden ground truth |
| Discrete assignment | Costs, rewards, availability | UAV-to-sector assignment | Compare greedy and exact baselines with QAOA |
| Route planning | Assignment and obstacles | Geometric paths | Check complete segments and keep-out regions |
| Timing and coordination | Paths and vehicle limits | Time-indexed trajectories | Check speed, acceleration, and inter-UAV separation |
| Tracking simulation | Trajectories and vehicle state | Executed motion | Measure tracking error and failed control steps |
| SAR evaluation | Motion and sensor observations | Detections and mission metrics | Separate detection from rescue completion |

PSO is a candidate for route planning. QAOA is a candidate for a small discrete assignment problem. The training pipeline prepares circuit parameters. SWAN provides ideas for trajectory coordination and simulation checks. These roles are complementary, but their integration requires new code and shared coordinate, time, and data conventions.

## 📐 A small assignment formulation to start with

This formulation is proposed here and is not claimed to be implemented in any reviewed repository. Let binary variable `x[u,s]` assign UAV `u` to sector `s`. Let `c[u,s]` be estimated travel cost, `r[u,s]` expected search benefit, and `lambda` the tradeoff weight. Minimize:

```text
J(x) = sum(u,s) (c[u,s] - lambda * r[u,s]) * x[u,s]
       + A * sum(u) (sum(s) x[u,s] - 1)^2
       + B * sum(s) sum(u<v) x[u,s] * x[v,s]
```

The first penalty encourages one sector per UAV. The second penalizes assigning two UAVs to the same sector. This is a simplified single-step model, not a full routing or scheduling problem. If sectors are fewer than active UAVs, distinct assignment is infeasible; add suitable idle options or revise the constraints. Exclude unreachable assignments or encode them with justified penalties. Choose penalties from objective bounds and verify the resulting optimum by enumeration before running QAOA.

This encoding uses `U*S` binary variables before reductions or additional constraints. Qubit requirements and classical simulation memory therefore grow with the assignment size. A tiny test should not be interpreted as evidence of scalability or quantum advantage.

## 🧪 Recommended evaluation sequence

1. Verify the assignment objective, bit ordering, and feasible solutions by exhaustive enumeration on a tiny instance.
2. Establish classical references: greedy assignment and an exact assignment solver where the simplified formulation permits it. Do not compare PSO route cost directly with QAOA assignment energy.
3. Validate PSO paths independently, then introduce timing and multi-UAV coordination.
4. Evaluate QAOA and training methods using equal problem instances, reporting all preprocessing, training, sampling, and decoding time.
5. Replay accepted trajectories in a chosen simulator, then measure target detection, coverage, mission duration, and failures using the [SAR benchmark](SAR_BENCHMARK.md).

Record source commits, solver versions, random seeds, cost weights, penalty coefficients, hardware, and stopping budgets. Report unsuccessful runs and constraint violations separately. No simulator compatibility, SAR improvement, energy saving, or quantum advantage is established by this review.
