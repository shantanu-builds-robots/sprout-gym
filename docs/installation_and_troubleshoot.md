
**Installation Steps:**

1. **Install Miniconda:**

   - Download Miniconda from the official website and follow the installation instructions for your operating system.

2. **Create a Virtual Environment:**

   ```bash
   conda create -n quadrobo_env python=3.10
   conda activate quadrobo_env
   ```

3. **Install Required Packages:**

   ```bash
   pip install gymnasium[mujoco] matplotlib hydra-core
   ```

4. **Install `CadQuery`:**

   ```bash
   pip install cadquery
   ```

5. **Install `quadrobo_gym` Custom Environment:**

   From the repository root:

   ```bash
   pip install -r requirements.txt
   pip install .                 # installs models/, utils/, environments/ and quadrobo_gym/
   pip install ./quadrobo_gym    # registers QuadroboEnv-v0 through the gym.envs entry point
   ```

   Check that it registered with `python scripts/list_registered_envs.py`.

**Note:** Always ensure that your package versions are compatible to prevent such errors. Regularly check the official repositories and documentation for updates and fixes related to these issues. 

**Troubleshooting Known Issues:**


To address the issues you've encountered, follow these troubleshooting steps:

**1. AttributeError: module 'numpy' has no attribute 'bool8'**

This error arises due to incompatibility between `CadQuery` and `numpy` version 2.0.0, where the `bool8` attribute has been removed. To resolve this:

- **Downgrade `numpy` to a compatible version:**

  ```bash
  pip install numpy==1.26.4
  ```

This solution is discussed in CadQuery's GitHub issue [#1626](https://github.com/CadQuery/cadquery/issues/1626).

**2. AttributeError: 'MjData' object has no attribute 'solver_iter'**

This error occurs because, in MuJoCo version 3.0.0, the `solver_iter` attribute has been renamed to `solver_niter`. To fix this:

- **Update your code to use the new attribute name:**

  Replace instances of `solver_iter` with `solver_niter` in your codebase.

This change is detailed in Gymnasium's GitHub pull request [#746](https://github.com/Farama-Foundation/Gymnasium/pull/746).

**3. MuJoCo viewer fails to open (`ERROR: could not create window`) inside a conda env**

This is usually a `libstdc++` mismatch between the conda env and the system OpenGL drivers. Preloading the system library before launching works around it:

```bash
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
```

MuJoCo writes these viewer errors to `MUJOCO_LOG.TXT` in the working directory (now git-ignored).
