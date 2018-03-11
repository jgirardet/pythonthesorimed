# Standard Libraries
import subprocess

# pythonthesorimed
from pythonthesorimed.parseur import parseur

if __name__ == '__main__':
    parseur.main()
    subprocess.run(["yapf", "-i", "pythonthesorimed/api.py"])
