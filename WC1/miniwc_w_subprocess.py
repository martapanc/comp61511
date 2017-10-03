#Created by Marta Pancaldi (10228373) on 28/09/17

import sys
import subprocess

if len(sys.argv) == 2:
    subprocess.call(['wc', sys.argv[1]])
else: quit()
