#Created by mbaxtmp2 on 01/11/17

import sys
import subprocess
from subprocess import check_output, Popen, PIPE
import os

# file_list = []
# dir = sys.argv[1]
# for file in os.listdir(dir):
#     file_list.append(dir + '/' + file)
#
# for f in file_list:
# #    print (f
#     subprocess.call(['time', 'python3', 'bloody_bin.py', f])
#     out1 = check_output(['time', 'python3', 'bloody_bin.py', f])
# #    print(str(out1) + "\n")

print("")
subprocess.call(['time', 'wc', "testinputs/*"])
