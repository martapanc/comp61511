import unittest

from wc import *
from wc_argparse import wc_argparse

#f1 = open('wc.py', 'r')
f2 = open("compare.sh", 'r')
f3 = open("testinputs/arabic.txt", 'r')
f4 = open("testinputs/chinese.txt", 'r')
f5 = open("testinputs/die.java", 'r')
f6 = open("testinputs/emoji.txt", 'r')
f7 = open("testinputs/empty", 'r')
f8 = open("testinputs/htmlTest.html", 'r')
f9 = open("testinputs/inferno2.txt", 'r')
f10 = open("testinputs/oneLine.txt", 'r')
f11 = open("testinputs/strangerThings.txt", 'r')
f12 = open("testinputs/test2.txt", 'r')
f13 = open("testinputs/test.txt", 'r')


class TestWC(unittest.TestCase):

    def setUp(self):
        pass

    def test_common_inputs(self):
        self.assertEqual('wc','*stdin not implemented yet*\\n')
        self.assertEqual('wc ','*stdin not implemented yet*\\n')
        self.assertEqual('wc -','wc: -: No such file or directory\\n')
        self.assertEqual('--','*stdin not implemented yet*\\n')
        self.assertEqual('- -','wc: -: No such file or directory\\nwc: -: No such file or directory\\n\\t0\\t0\\t0\\ttotal\\n')
        self.assertEqual('- -   - ','wc: -: No such file or directory\\nwc: -: No such file or directory\\nwc: -: No such file or directory\\n\\t0\\t0\\t0\\ttotal\\n')
        self.assertEqual('-w','*stdin not implemented yet*\\n')
        self.assertEqual('-c','*stdin not implemented yet*\\n')
        self.assertEqual('-l','*stdin not implemented yet*\\n')
        self.assertEqual('-wc','*stdin not implemented yet*\\n')
        self.assertEqual('-cl','*stdin not implemented yet*\\n')
        self.assertEqual('-wl ','*stdin not implemented yet*\\n')
        self.assertEqual('-wcl','*stdin not implemented yet*\\n')
        self.assertEqual('-lcw -ll -w','*stdin not implemented yet*\\n')
        self.assertEqual('-cl -','wc: -: No such file or directory\\n')
        self.assertEqual('-c -w -l','*stdin not implemented yet*\\n')
        self.assertEqual('-wwc -lw -l -','wc: -: No such file or directory\\n')
        self.assertEqual('--','*stdin not implemented yet*\\n')
        self.assertEqual('-w -','wc: -: No such file or directory\\n')

    def test_count_lines(self):
#        self.assertEqual(count_lines(f1), 140)
        self.assertEqual(count_lines(f2), 6)
        self.assertEqual(count_lines(f3), 19)
        self.assertEqual(count_lines(f4), 21)
        self.assertEqual(count_lines(f5), 126)
        self.assertEqual(count_lines(f6), 256)
        self.assertEqual(count_lines(f7), 0)
        self.assertEqual(count_lines(f8), 15)
        self.assertEqual(count_lines(f9), 14920)
        self.assertEqual(count_lines(f10), 1)
        self.assertEqual(count_lines(f11), 109)
        self.assertEqual(count_lines(f12), 8)
        self.assertEqual(count_lines(f13), 10)

    def test_count_words(self):
#        self.assertEqual(count_words(f1), 454)
        self.assertEqual(count_words(f2), 15)
        self.assertEqual(count_words(f3), 485)
        self.assertEqual(count_words(f4), 1127)
        self.assertEqual(count_words(f5), 533)
        self.assertEqual(count_words(f6), 854)
        self.assertEqual(count_words(f7), 0)
        self.assertEqual(count_words(f8), 229)
        self.assertEqual(count_words(f9), 102197)
        self.assertEqual(count_words(f10), 6)
        self.assertEqual(count_words(f11), 536)
        self.assertEqual(count_words(f12), 22)
        self.assertEqual(count_words(f13), 74)

    def test_count_bytes(self):
#        self.assertEqual(count_bytes(f1), 4733)
        self.assertEqual(count_bytes(f2), 89)
        self.assertEqual(count_bytes(f3), 4898)
        self.assertEqual(count_bytes(f4), 8483)
        self.assertEqual(count_bytes(f5), 3608)
        self.assertEqual(count_bytes(f6), 5401)
        self.assertEqual(count_bytes(f7), 0)
        self.assertEqual(count_bytes(f8), 2488)
        self.assertEqual(count_bytes(f9), 562492)
        self.assertEqual(count_bytes(f10), 37)
        self.assertEqual(count_bytes(f11), 11618)
        self.assertEqual(count_bytes(f12), 141)
        self.assertEqual(count_bytes(f13), 373)

    def test_count_chars(self):
#        self.assertEqual(count_chars(f1), 4733)
        self.assertEqual(count_chars(f2), 89)
        self.assertEqual(count_chars(f3), 2750)
        self.assertEqual(count_chars(f4), 3721)
        self.assertEqual(count_chars(f5), 3608)
        self.assertEqual(count_chars(f6), 4616)
        self.assertEqual(count_chars(f7), 0)
        self.assertEqual(count_chars(f8), 2462)
        self.assertEqual(count_chars(f9), 553466)
        self.assertEqual(count_chars(f10), 37)
        self.assertEqual(count_chars(f11), 5585)
        self.assertEqual(count_chars(f12), 133)
        self.assertEqual(count_chars(f13), 373)



if __name__ == '__main__':
    unittest.main()
