# Update subprojects

import os
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    ox_path = Path(os.path.realpath(__file__)).parent.parent
    git_path = os.path.join(ox_path, ".git")
    
    os.chdir(ox_path)
    
    result = subprocess.run(["git", "submodule", "update", "--init", "--recursive"], capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Error updating subprojects", file = sys.stderr)
        print("details:", file = sys.stderr)
        print(result.stderr)
    else:
        print("Subprojects updated successfully")
        print(result.stdout)