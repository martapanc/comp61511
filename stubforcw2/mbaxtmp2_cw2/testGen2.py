from random import randint
import sys
import subprocess

files = sys.argv
flags=['c','l','w','','','']

def randomFlag():
    flip = randint(0,4)
    if flip == 0 or flip == 1:
        result=' -'
        for n in range(randint(1,5)):
            result += flags[randint(0,5)]
        result += ' '
    elif flip == 2 or flip == 3:
        result=' '
        for n in range(randint(1,5)):
            result += "-" + flags[randint(0,5)] + " "
    else:
        result=' '
    return str(result)

args = randomFlag()
for n in range(randint(2,4)):
    args += files[randint(0,10)] + randomFlag()

print(args)
#subprocess.run('python3 MACwc.py ' + args, shell=True)
subprocess.run('bash compare.sh ' + args, shell=True)
