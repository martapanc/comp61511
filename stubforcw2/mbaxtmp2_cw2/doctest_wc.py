"""
>>> import subprocess
>>> subprocess.check_output('wc t.txt', shell=True)
b'       6       5      43 t.txt\\n'
>>> subprocess.check_output('python3 MACwc.py t.txt', shell=True)
b'       6       5      43 t.txt\\n'
>>> subprocess.check_output('python3 wc.py t.txt', shell=True)
b'       6       5      43 t.txt\\n'
"""

if __name__ == "__main__":
     import doctest
     doctest.testmod()
