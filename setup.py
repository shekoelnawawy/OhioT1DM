import shutil
import subprocess
import os
import sys
from pathlib import Path

def run_command(cmd, shell=False, env=None):
    """Run a shell command and print output in real time."""
    print(f"\n>>> Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    result = subprocess.run(cmd, shell=shell, env=env, check=True)
    return result

def main():
    base_dir = Path.cwd()
    venv_dir = base_dir / "myvenv"

    # 1. Create virtual environment
    run_command([sys.executable, "-m", "venv", str(venv_dir)])

    # 2. Path to the virtual environment's Python
    venv_python = venv_dir / "bin" / "python"
    venv_pip = venv_dir / "bin" / "pip"

    # 3. Install requirements
    run_command([str(venv_pip), "install", "-r", "requirements.txt"])

    # 4. Copy data
    """Run a shell command and print output in real time."""
    print("\n>>> Running: cp -r ~/Downloads/OhioT1DM/processed_data/20* .")
    shutil.copytree("/home/mnawawy/Downloads/OhioT1DM/processed_data/2020data", base_dir+"/2020data", dirs_exist_ok=True)
    shutil.copytree("/home/mnawawy/Downloads/OhioT1DM/processed_data/2018data", base_dir+"/2018data", dirs_exist_ok=True)
    # 5. Copy pretrained models
    """Run a shell command and print output in real time."""
    print("\n>>> Running: cp -r ~/Downloads/OhioT1DM/models/PRETRAINS .")
    shutil.copytree("/home/mnawawy/Downloads/OhioT1DM/models/PRETRAINS", base_dir+"/PRETRAINS", dirs_exist_ok=True)

    # 6. Change directory to URET
    os.chdir("URET")

    # 7. Install URET package in editable mode
    run_command([str(venv_pip), "install", "-e", "."])

if __name__ == "__main__":
    main()
