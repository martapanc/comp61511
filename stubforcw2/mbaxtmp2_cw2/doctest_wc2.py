"""
>>> import subprocess

>>> def test(input):
...     return subprocess.check_output("python3 MACwc.py " + input, shell=True)

>>> test('t.txt')
b'\\t6\\t5\\t43\\tt.txt\\n'

>>> test('t.txt -w')
b'\\t5\\tt.txt\\n'
>>> test('t.txt -c')
b'\\t43\\tt.txt\\n'
>>> test('t.txt -l')
b'\\t6\\tt.txt\\n'

>>> test('t.txt wc.py')
b'\\t6\\t5\\t43\\tt.txt\\n\\t144\\t528\\t5371\\twc.py\\n\\t150\\t533\\t5414\\t total\\n'
>>> test('t.txt wc.py -w')
b'\\t5\\tt.txt\\n\\t528\\twc.py\\n\\t533\\t total\\n'
>>> test('t.txt wc.py -c')
b'\\t43\\tt.txt\\n\\t5371\\twc.py\\n\\t5414\\t total\\n'
>>> test('t.txt wc.py -l')
b'\\t6\\tt.txt\\n\\t144\\twc.py\\n\\t150\\t total\\n'

>>> test('t.txt wc.py test.py')
b'\\t6\\t5\\t43\\tt.txt\\n\\t144\\t528\\t5371\\twc.py\\n\\t62\\t172\\t1511\\ttest.py\\n\\t212\\t705\\t6925\\t total\\n'



"""

if __name__ == "__main__":
     import doctest
     doctest.testmod()

# format("6 5 43 t.txt") returns "\\t6\\t5\\t43\\tt.txt\\n"
