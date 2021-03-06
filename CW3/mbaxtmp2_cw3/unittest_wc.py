import unittest

from wc_unit import *
#from wc_argparse import *

#f1 = open('wc.py', 'r')
#f2 = open("compare.sh", 'r')
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

    def test_count_lines(self):
        #self.assertEqual(count_lines(f1), 140)
        #self.assertEqual(count_lines(f2), 6)
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
        # self.assertEqual(count_words(f1), 454)
        #self.assertEqual(count_words(f2), 15)
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
        #self.assertEqual(count_bytes(f1), 4733)
        #self.assertEqual(count_bytes(f2), 89)
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
        #self.assertEqual(count_chars(f1), 4733)
        #self.assertEqual(count_chars(f2), 89)
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

    def test_check_flags(self):
        self.assertTrue(check_flag("w"))
        self.assertTrue(check_flag("c"))
        self.assertTrue(check_flag("l"))
        self.assertFalse(check_flag("ç"))
        self.assertFalse(check_flag("q"))
        self.assertFalse(check_flag("e"))
        self.assertFalse(check_flag("r"))
        self.assertFalse(check_flag("t"))
        self.assertFalse(check_flag("y"))
        self.assertFalse(check_flag("u"))
        self.assertFalse(check_flag("i"))
        self.assertFalse(check_flag("o"))
        self.assertFalse(check_flag("p"))
        self.assertFalse(check_flag("n"))
        self.assertFalse(check_flag("x"))
        self.assertFalse(check_flag("@"))
        self.assertFalse(check_flag("%"))
        self.assertFalse(check_flag("1"))
        self.assertFalse(check_flag("0"))
        self.assertFalse(check_flag("("))
        self.assertFalse(check_flag("\""))
        self.assertFalse(check_flag("0"))
        self.assertFalse(check_flag(" "))
        self.assertFalse(check_flag("wc"))
        self.assertFalse(check_flag("wlc"))
        self.assertFalse(check_flag("wa"))
        self.assertFalse(check_flag("."))

    def test_all_valid_args(self):
        self.assertEqual(all_valid_args(['-w', 'file.txt']), (True, {'w'}, ['file.txt']))
        self.assertEqual(all_valid_args(['-w', 'file.txt', '-c']), (True, {'w', 'c'}, ['file.txt']))
        self.assertEqual(all_valid_args(['-c', '-w', 'file.txt']), (True, {'w', 'c'}, ['file.txt']))
        self.assertEqual(all_valid_args(['-l', '-w', '-c', 'file.txt']), (True, {'w', 'c', 'l'}, ['file.txt']))
        self.assertEqual(all_valid_args(['-w', '-']), (True, {'w'}, ['-']))
        self.assertEqual(all_valid_args(['-w', 'file.txt', '-']), (True, {'w'}, ['file.txt', '-']))
        self.assertEqual(all_valid_args(['-w', 'file.txt', '-']), (True, {'w'}, ['file.txt', '-']))
        self.assertEqual(all_valid_args(['-w', 'file.txt', '-']), (True, {'w'}, ['file.txt', '-']))
        self.assertEqual(all_valid_args(['-w', 'file.txt', '-']), (True, {'w'}, ['file.txt', '-']))
        self.assertEqual(all_valid_args(['-w', 'file.txt', '-']), (True, {'w'}, ['file.txt', '-']))

        self.assertRaises(SystemExit, all_valid_args, ['-a file.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['-k', 'file.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['- -', 'file.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['--', 'file.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['---', 'file.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['--w-', 'file.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['-a -w', 'file.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['- -   - ', 'file.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['-wc -l -a.', 'file.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['-.', 'file.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['-l -@', 'file.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['-wcl -'])
        self.assertRaises(SystemExit, all_valid_args, ['-lcw -ll -w'])
        self.assertRaises(SystemExit, all_valid_args, ['-cl -'])
        self.assertRaises(SystemExit, all_valid_args, ['-c -w -l'])
        self.assertRaises(SystemExit, all_valid_args, ['-wwc -lw -l -'])
        self.assertRaises(SystemExit, all_valid_args, ['-k'])
        self.assertRaises(SystemExit, all_valid_args, ['-y','testinputs/'])
        self.assertRaises(SystemExit, all_valid_args, ['-qw testinputs/test.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['-w -x -f testinputs/test.txt testinputs/chinese.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['-clg testinputs/test.txt testinputs/chinese.txt'])
        self.assertRaises(SystemExit, all_valid_args, ['-ql -'])
        self.assertRaises(SystemExit, all_valid_args, ['-w-'])
        self.assertRaises(SystemExit, all_valid_args, ['-l--a'])
        self.assertRaises(SystemExit, all_valid_args, ['-wc-37'])
        self.assertRaises(SystemExit, all_valid_args, ['-wc--37'])
        self.assertRaises(SystemExit, all_valid_args, ['--wc--3'])
        self.assertRaises(SystemExit, all_valid_args, ['- ---'])
        self.assertRaises(SystemExit, all_valid_args, ['--- -'])
        self.assertRaises(SystemExit, all_valid_args, ['----'])
        self.assertRaises(SystemExit, all_valid_args, ['---w'])
        self.assertRaises(SystemExit, all_valid_args, ['--w--'])
        self.assertRaises(SystemExit, all_valid_args, ['--w--23'])
        self.assertRaises(SystemExit, all_valid_args, ['--c-'])
        self.assertRaises(SystemExit, all_valid_args, ['--w-- 23'])
        self.assertRaises(SystemExit, all_valid_args, ['--@'])


    def test_compute_result(self):
        self.assertEqual(compute_result(['w', 'c', 'l'], ['testinputs/arabic.txt']), "\t19\t485\t4898\ttestinputs/arabic.txt\n")
        self.assertEqual(compute_result([], ['testinputs/arabic.txt']), "\t19\t485\t4898\ttestinputs/arabic.txt\n")
        self.assertEqual(compute_result([], ['testinputs']),'wc: testinputs: Is a directory\n\t0\t0\t0\ttestinputs\n')
        self.assertEqual(compute_result([], ['testinputs/']),'wc: testinputs/: Is a directory\n\t0\t0\t0\ttestinputs/\n')
        self.assertEqual(compute_result([], ['testinputs/','testinputs/die.java']),'wc: testinputs/: Is a directory\n\t0\t0\t0\ttestinputs/\n\t126\t533\t3608\ttestinputs/die.java\n\t126\t533\t3608\ttotal\n')
        self.assertEqual(compute_result(['w', 'c'], ['testinputs/strangerThings.txt','testinputs', 'testinputs/htmlTest.html']),'\t536\t11618\ttestinputs/strangerThings.txt\nwc: testinputs: Is a directory\n\t0\t0\ttestinputs\n\t229\t2488\ttestinputs/htmlTest.html\n\t765\t14106\ttotal\n')
        self.assertEqual(compute_result([], ['testinputs/chinese.txt','testinputs', 'testinputs/htmlTest.html', 'testinputs/']),'\t21\t1127\t8483\ttestinputs/chinese.txt\nwc: testinputs: Is a directory\n\t0\t0\t0\ttestinputs\n\t15\t229\t2488\ttestinputs/htmlTest.html\nwc: testinputs/: Is a directory\n\t0\t0\t0\ttestinputs/\n\t36\t1356\t10971\ttotal\n')
        self.assertEqual(compute_result(['c'], ['testinputs/']), 'wc: testinputs/: Is a directory\n\t0\ttestinputs/\n')
        self.assertEqual(compute_result([], ['idk ']), 'wc: idk : No such file or directory\n')
        self.assertEqual(compute_result([], ['noSuchFile.dat']),'wc: noSuchFile.dat: No such file or directory\n')
        self.assertEqual(compute_result([], ['noSuchFile.dat','testinputs/arabic.txt']), 'wc: noSuchFile.dat: No such file or directory\n\t19\t485\t4898\ttestinputs/arabic.txt\n\t19\t485\t4898\ttotal\n')
        self.assertEqual(compute_result(['c'], ['noSuchFile.dat','testinputs/die.java']), 'wc: noSuchFile.dat: No such file or directory\n\t3608\ttestinputs/die.java\n\t3608\ttotal\n')
        self.assertEqual(compute_result(['w', 'l'], ['noSuchFile.dat','testinputs/die.java','noSuchFile.txt','testinputs/htmlTest.html']), 'wc: noSuchFile.dat: No such file or directory\n\t126\t533\ttestinputs/die.java\nwc: noSuchFile.txt: No such file or directory\n\t15\t229\ttestinputs/htmlTest.html\n\t141\t762\ttotal\n')
        self.assertEqual(compute_result([], ['noSuchfile.txt','testinputs/']), 'wc: noSuchfile.txt: No such file or directory\nwc: testinputs/: Is a directory\n\t0\t0\t0\ttestinputs/\n\t0\t0\t0\ttotal\n')


if __name__ == '__main__':
    unittest.main()
