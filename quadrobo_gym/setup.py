import os
from setuptools import setup, find_packages

_readme = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "README.md")
long_description = open(_readme).read() if os.path.exists(_readme) else ""

setup(
    name="quadrobo_gym",
    version="0.1",
    author="Shantanu Parab",
    author_email="sparab@umd.edu",
    description="Custom MuJoCo-based quadruped robot environment for OpenAI Gym",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "gym>=0.21",
        "mujoco",
        "numpy"
    ],
    entry_points={
        "gym.envs": [
            "QuadroboEnv-v0 = quadrobo_gym.env:QuadroboEnv",
        ]
    },
    include_package_data=True,
    package_data={
        "quadrobo_gym": [
            "assets/*.xml",
            "assets/meshes/*.STL"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
