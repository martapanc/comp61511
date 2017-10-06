"""
>>> import subprocess
>>> subprocess.check_output('wc t.txt', shell=True)
b'       6       5      43 t.txt\\n'
>>> subprocess.check_output('python3 MACwc.py t.txt', shell=True)
b'       6       5      43 t.txt\\n'
>>> subprocess.check_output('python3 wc.py t.txt', shell=True)
b'       6       5      43 t.txt\\n'

>>> def format(output):
...     return "b'" + output.replace(" ", "\\t").append("\n") + "'"

>>> test('wc t.txt','       6       5      43 t.txt\\n')
"""

if __name__ == "__main__":
     import doctest
     doctest.testmod()

def test(input)
    return subprocess.check_output(input, shell=True)

def expected(exp_output):
    return b exp_output
