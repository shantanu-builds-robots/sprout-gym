# Sprout Gym 🌱

**Sprout couldn't walk. So it learned.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

https://github.com/user-attachments/assets/8f91cb60-bef9-4fa4-9049-b5246b1ea295

Sprout Gym is a custom MuJoCo environment where **Sprout**, a quadruped I designed in SolidWorks
([shantanu-builds-robots/quad_robo](https://github.com/shantanu-builds-robots/quad_robo)), learns to walk with
**TD3** (Twin Delayed Deep Deterministic Policy Gradient). It goes from tipping over at episode 100 to walking by episode 20,000.

## Training progress

https://github.com/user-attachments/assets/d51b1138-ef5c-40bf-964e-35f496e49969

## How it works

| Piece | Details | Where |
|---|---|---|
| **Robot** | Sprout's own meshes, 12 position actuators (3 per leg) | `quadrobo_gym/assets/` |
| **Environment** | `QuadroboEnv-v0`: 124-dim observation (joint positions/velocities, contact forces, roll/pitch/yaw) | `quadrobo_gym/env.py` |
| **Agent** | TD3 actor–critic: 124 → 256 → 256 → 12, twin critics, delayed policy updates | `models/td3.py`, `configs/model/td3.yaml` |
| **Config** | Hydra configs for training, environment, model, and rewards | `configs/` |

### Reward

From `QuadroboEnv.step`:

| Term | Weight |
|---|---|
| Forward velocity | **+5.0** |
| Forward distance per step | **+7.5** |
| Staying healthy (torso height in range) | **+1.0** |
| Sideways drift | **−0.1** |
| Σ \|joint velocity\| (flailing) | **−0.5** |
| \|roll\|, \|pitch\|, \|yaw\| | **−0.02, −0.02, −0.05** |

An episode ends when the robot is unhealthy, or when roll, pitch, or yaw goes past 60°.
More in [docs/reward_design.md](docs/reward_design.md).

## Quick start

```bash
conda create -n quadrobo_env python=3.10 && conda activate quadrobo_env
pip install -r requirements.txt
pip install .                 # project packages
pip install ./quadrobo_gym    # registers QuadroboEnv-v0

python scripts/train.py       # train (settings in configs/config.yaml)
python scripts/evaluate.py    # watch the latest checkpoint walk
```

Checkpoints and plots go to `outputs/`. If the MuJoCo viewer won't open inside conda, see
[troubleshooting](docs/installation_and_troubleshoot.md).

## Repository layout

```
├── configs/          Hydra configs: config.yaml + environment/, model/, rewards/
├── docs/             Guides (install, env, reward, model, training) and media/
├── environments/     Wrappers used by the scripts (QuadEnv)
├── models/           TD3 and a base model with save/load
├── quadrobo_gym/     The QuadroboEnv-v0 package: env.py, MuJoCo model, meshes
├── scripts/          train.py, evaluate.py, test_env.py, list_registered_envs.py
└── utils/            Replay buffer and optional reward shaping
```

Full breakdown: [docs/project_structure.md](docs/project_structure.md).

## Documentation

- [Installation and troubleshooting](docs/installation_and_troubleshoot.md)
- [Custom environment](docs/custom_env.md)
- [Reward design](docs/reward_design.md)
- [TD3 model](docs/model_definition.md)
- [Training and evaluation](docs/training_and_evaluation.md)

## Contributing

Issues and pull requests are welcome; templates are in `.github/ISSUE_TEMPLATE/`.

## License

MIT, see [LICENSE](LICENSE).
