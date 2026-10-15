# 🚁 UAV Swarm Simulation & Search and Rescue

<p align="center">
  <img src="https://img.shields.io/badge/Projects-{{COUNT}}-2563eb?style=flat-square" alt="{{COUNT}} curated projects">
  <img src="https://img.shields.io/badge/Focus-Search%20%26%20Rescue-dc2626?style=flat-square" alt="Search and rescue">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/MATLAB-e16737?style=flat-square" alt="MATLAB">
  <img src="https://img.shields.io/badge/ROS-22314E?style=flat-square&amp;logo=ros&amp;logoColor=white" alt="ROS">
</p>

A curated collection of **{{COUNT}} UAV swarm simulation projects**, with an emphasis on **search and rescue (SAR)**. Explore cooperative search, flight dynamics, multi-agent reinforcement learning, and emergency communication networks.

**Explore:** [Project catalog](#-project-catalog) · [Selection guide](docs/SELECTION_GUIDE.md) · [SAR benchmark](docs/SAR_BENCHMARK.md) · [Catalog data](catalog.json)

## 🧭 Choose your starting point

| Your goal | Start with | What to consider |
| :--- | :--- | :--- |
| 🌊 Maritime search and rescue | DSSE | Search and coverage environments with drift-based search distributions |
| 🗺️ Cooperative search on a 2D map | SwarmSAR | Verify implementation maturity and reported performance |
| 👁️ Visual target search | CTS visual drone swarm | Add SAR-specific targets, sensing assumptions, and evaluation |
| 🐍 Flight dynamics and learning in Python | gym-pybullet-drones, QuadSwarm | Build mission logic on top of the flight simulation |
| 📐 Swarm algorithms in MATLAB | SwarmLab, SwarmFly | Check MATLAB versions, toolboxes, and vehicle models |
| 🛩️ Multi-vehicle flight and control | XTDrone, Pegasus, Crazyswarm2 | Match middleware, autopilot, simulator, and hardware requirements |
| 📡 Emergency communication networks | uav-swarm-sim | Evaluate communication separately from flight and search performance |

## 📚 Project catalog

| Project | Category | Technology | SAR relevance | Profile |
| :--- | :--- | :--- | :--- | :--- |
{{TABLE}}

**Category key:** 🛟 SAR mission environments · 🔍 Cooperative target search · ⚙️ Simulation and control platforms · 📡 Communication networks.

Detailed project profiles and supporting guides are currently in Vietnamese. This README provides an English overview.

## 🔎 Scope and verification

SAR environments explicitly describe search and rescue tasks. Target-search projects focus on cooperative discovery. General simulation platforms require additional mission logic, target models, and sensors. Network simulators support communication research relevant to rescue operations.

Sources were reviewed on **October 15, 2026**. Suitability notes are editorial assessments based on official repositories and documentation. Third-party projects have **not been installed, benchmarked, or validated here**. Compatibility between projects has not been established, and upstream performance claims require independent verification.

## 🧪 Build a reproducible SAR experiment

1. **Choose a modeling level.** Use the [selection guide](docs/SELECTION_GUIDE.md) to decide whether you need mission-level simulation, flight dynamics, visual sensing, or network modeling.
2. **Establish a baseline.** Start with equal-area partitioning and lawnmower coverage before adding adaptive policies or reinforcement learning.
3. **Define the mission.** Specify targets, detection probability, battery limits, communication assumptions, and stopping conditions.
4. **Compare fairly.** Follow the [proposed SAR benchmark](docs/SAR_BENCHMARK.md), using matched seeds and consistent mission budgets.
5. **Record evidence.** Save upstream commits, configurations, trajectories, logs, and failure cases alongside results.

The benchmark is an experimental proposal; this repository does not report benchmark results. Detecting a simulated target is distinct from completing a rescue operation.

## 🗂️ Repository contents

| Resource | Purpose |
| :--- | :--- |
| [catalog.json](catalog.json) | Source data for all curated entries |
| [catalog.csv](catalog.csv) | Spreadsheet-friendly export for filtering and comparison |
| [repositories/](repositories/) | Profiles with capabilities, SAR extensions, exercises, and limitations |
| [Selection guide](docs/SELECTION_GUIDE.md) | Platform choices and environment considerations |
| [SAR benchmark](docs/SAR_BENCHMARK.md) | Proposed scenarios, baselines, metrics, and run records |
| [README template](docs/README.template.md) | Source template for this generated overview |

## 🛠️ Maintain the catalog

Edit [catalog.json](catalog.json), including the English overview fields under `readme_en`. From the repository root, regenerate the README, CSV, and profiles:

```console
python scripts/build_catalog.py
```

The generator uses only the Python standard library. Update each entry's review date when checking its sources. Claims of successful execution or benchmark performance should include the environment, configuration, upstream commit, and logs.

## 🤝 Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Prefer official sources, explain how each project relates to SAR, and distinguish documented capabilities from proposed extensions.

## 📄 Upstream licenses

This collection contains descriptions and links without redistributing upstream source code. Check each project's license at the exact revision you intend to use. MATLAB, Isaac Sim, and other dependencies may have separate licensing and system requirements.
