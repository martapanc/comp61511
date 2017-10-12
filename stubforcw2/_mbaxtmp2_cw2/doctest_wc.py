"""
>>> import subprocess

>>> def test(input):
...     return subprocess.check_output("python3 wc.py " + input, shell=True)

>>> test('')
b'*stdin not implemented yet*\\n'
>>> test(' ')
b'*stdin not implemented yet*\\n'
>>> test('-')
b'*stdin not implemented yet*\\n'
>>> test('--')
b'*stdin not implemented yet*\\n'
>>> test('- -')
b'*stdin not implemented yet*\\n'
>>> test('- -   - ')
b'*stdin not implemented yet*\\n'
>>> test('-w')
b'*stdin not implemented yet*\\n'
>>> test('-c')
b'*stdin not implemented yet*\\n'
>>> test('-l')
b'*stdin not implemented yet*\\n'
>>> test('-wc')
b'*stdin not implemented yet*\\n'
>>> test('-cl')
b'*stdin not implemented yet*\\n'
>>> test('-wl ')
b'*stdin not implemented yet*\\n'
>>> test('-wcl')
b'*stdin not implemented yet*\\n'
>>> test('-lcw -ll -w')
b'*stdin not implemented yet*\\n'
>>> test('-cl -')
b'*stdin not implemented yet*\\n'
>>> test('-c -w -l')
b'*stdin not implemented yet*\\n'
>>> test('-wwc -lw -l -')
b'*stdin not implemented yet*\\n'
>>> test('--')
b'*stdin not implemented yet*\\n'
>>> test('-w -')
b'*stdin not implemented yet*\\n'

>>> test('testinputs')
b'wc: testinputs: Is a directory\\n\\t0\\t0\\t0\\ttestinputs\\n'
>>> test('testinputs/')
b'wc: testinputs/: Is a directory\\n\\t0\\t0\\t0\\ttestinputs/\\n'
>>> test('testinputs/ testinputs/die.java')
b'wc: testinputs/: Is a directory\\n\\t0\\t0\\t0\\ttestinputs/\\n\\t126\\t533\\t3608\\ttestinputs/die.java\\n\\t126\\t533\\t3608\\ttotal\\n'
>>> test('testinputs/strangerThings.txt testinputs testinputs/htmlTest.html -wc')
b'\\t702\\t13620\\ttestinputs/strangerThings.txt\\nwc: testinputs: Is a directory\\n\\t0\\t0\\ttestinputs\\n\\t229\\t2488\\ttestinputs/htmlTest.html\\n\\t931\\t16108\\ttotal\\n'
>>> test('testinputs/chinese.txt testinputs testinputs/htmlTest.html testinputs/')
b'\\t21\\t1127\\t8483\\ttestinputs/chinese.txt\\nwc: testinputs: Is a directory\\n\\t0\\t0\\t0\\ttestinputs\\n\\t15\\t229\\t2488\\ttestinputs/htmlTest.html\\nwc: testinputs/: Is a directory\\n\\t0\\t0\\t0\\ttestinputs/\\n\\t36\\t1356\\t10971\\ttotal\\n'
>>> test('-c testinputs/ ')
b'wc: testinputs/: Is a directory\\n\\t0\\ttestinputs/\\n'
>>> test('idk ')
b'wc: idk: No such file or directory\\n'

>>> test('noSuchFile.dat')
b'wc: noSuchFile.dat: No such file or directory\\n'
>>> test(' noSuchFile.dat testinputs/arabic.txt')
b'wc: noSuchFile.dat: No such file or directory\\n\\t19\\t485\\t4898\\ttestinputs/arabic.txt\\n\\t19\\t485\\t4898\\ttotal\\n'
>>> test('noSuchFile.dat testinputs/die.java -c')
b'wc: noSuchFile.dat: No such file or directory\\n\\t3608\\ttestinputs/die.java\\n\\t3608\\ttotal\\n'
>>> test('noSuchFile.dat testinputs/die.java -wl noSuchFile.txt testinputs/htmlTest.html')
b'wc: noSuchFile.dat: No such file or directory\\n\\t126\\t533\\ttestinputs/die.java\\nwc: noSuchFile.txt: No such file or directory\\n\\t15\\t229\\ttestinputs/htmlTest.html\\n\\t141\\t762\\ttotal\\n'
>>> test('noSuchfile.txt testinputs/')
b'wc: noSuchfile.txt: No such file or directory\\nwc: testinputs/: Is a directory\\n\\t0\\t0\\t0\\ttestinputs/\\n\\t0\\t0\\t0\\ttotal\\n'

>>> test('-k')
b"wc: invalid option -- 'k'\\nTry 'wc --help' for more information.\\n"
>>> test('-y testinputs/')
b"wc: invalid option -- 'y'\\nTry 'wc --help' for more information.\\n"
>>> test('testinputs/test.txt -qw')
b"wc: invalid option -- 'q'\\nTry 'wc --help' for more information.\\n"
>>> test('testinputs/test.txt testinputs/chinese.txt -w -x -f')
b"wc: invalid option -- 'x'\\nTry 'wc --help' for more information.\\n"
>>> test('-clg testinputs/test.txt testinputs/chinese.txt')
b"wc: invalid option -- 'g'\\nTry 'wc --help' for more information.\\n"
>>> test('-ql -')
b"wc: invalid option -- 'q'\\nTry 'wc --help' for more information.\\n"
>>> test('-w-')
b"wc: invalid option -- '-'\\nTry 'wc --help' for more information.\\n"
>>> test('-l--a')
b"wc: invalid option -- '-'\\nTry 'wc --help' for more information.\\n"
>>> test('-wc-37')
b"wc: invalid option -- '-'\\nTry 'wc --help' for more information.\\n"
>>> test('-wc--37')
b"wc: invalid option -- '-'\\nTry 'wc --help' for more information.\\n"
>>> test('--wc--3')
b"wc: unrecognized option '--wc--3'\\nTry 'wc --help' for more information.\\n"

>>> test('---')
b"wc: unrecognized option '---'\\nTry 'wc --help' for more information.\\n"
>>> test('- ---')
b"wc: unrecognized option '---'\\nTry 'wc --help' for more information.\\n"
>>> test('--- -')
b"wc: unrecognized option '---'\\nTry 'wc --help' for more information.\\n"
>>> test('----')
b"wc: unrecognized option '----'\\nTry 'wc --help' for more information.\\n"
>>> test('---w')
b"wc: unrecognized option '---w'\\nTry 'wc --help' for more information.\\n"
>>> test('--w--')
b"wc: unrecognized option '--w--'\\nTry 'wc --help' for more information.\\n"
>>> test('--w--23')
b"wc: unrecognized option '--w--23'\\nTry 'wc --help' for more information.\\n"
>>> test('--c-')
b"wc: unrecognized option '--c-'\\nTry 'wc --help' for more information.\\n"
>>> test('--w--23')
b"wc: unrecognized option '--w--23'\\nTry 'wc --help' for more information.\\n"
>>> test('--@')
b"wc: unrecognized option '--@'\\nTry 'wc --help' for more information.\\n"

>>> test('.--@')
b'wc: .--@: No such file or directory\\n'
>>> test('.--@')
b'wc: .--@: No such file or directory\\n'


>>> test('testinputs/test.txt -w')
b'\\t74\\ttestinputs/test.txt\\n'
>>> test('testinputs/test.txt -c')
b'\\t373\\ttestinputs/test.txt\\n'
>>> test('testinputs/test.txt -l')
b'\\t10\\ttestinputs/test.txt\\n'

>>> test('testinputs/test.txt testinputs/inferno2.txt')
b'\\t10\\t74\\t373\\ttestinputs/test.txt\\n\\t14920\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t14930\\t102271\\t562865\\ttotal\\n'
>>> test('-wwc testinputs/die.java testinputs/inferno2.txt -cw')
b'\\t533\\t3608\\ttestinputs/die.java\\n\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t102730\\t566100\\ttotal\\n'
>>> test('-l testinputs/oneLine.txt testinputs/strangerThings.txt testinputs/inferno2.txt -l -l')
b'\\t1\\ttestinputs/oneLine.txt\\n\\t117\\ttestinputs/strangerThings.txt\\n\\t14920\\ttestinputs/inferno2.txt\\n\\t15038\\ttotal\\n'
>>> test(' testinputs/arabic.txt -cwlc testinputs/emoji.txt testinputs/test.txt testinputs/inferno2.txt -c -c -c -c ')
b'\\t19\\t485\\t4898\\ttestinputs/arabic.txt\\n\\t256\\t854\\t5401\\ttestinputs/emoji.txt\\n\\t10\\t74\\t373\\ttestinputs/test.txt\\n\\t14920\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t15205\\t103610\\t573164\\ttotal\\n'


>>> test('testinputs/arabic.txt')
b'\\t19\\t485\\t4898\\ttestinputs/arabic.txt\\n'
>>> test('-w testinputs/arabic.txt')
b'\\t485\\ttestinputs/arabic.txt\\n'
>>> test('-l testinputs/arabic.txt')
b'\\t19\\ttestinputs/arabic.txt\\n'
>>> test('-c testinputs/arabic.txt')
b'\\t4898\\ttestinputs/arabic.txt\\n'
>>> test('-cw testinputs/arabic.txt')
b'\\t485\\t4898\\ttestinputs/arabic.txt\\n'
>>> test('-cl testinputs/arabic.txt')
b'\\t19\\t4898\\ttestinputs/arabic.txt\\n'
>>> test('-wl testinputs/arabic.txt')
b'\\t19\\t485\\ttestinputs/arabic.txt\\n'
>>> test('-wc testinputs/arabic.txt')
b'\\t485\\t4898\\ttestinputs/arabic.txt\\n'
>>> test('-lc testinputs/arabic.txt')
b'\\t19\\t4898\\ttestinputs/arabic.txt\\n'
>>> test('-lw testinputs/arabic.txt')
b'\\t19\\t485\\ttestinputs/arabic.txt\\n'
>>> test('-clw testinputs/arabic.txt')
b'\\t19\\t485\\t4898\\ttestinputs/arabic.txt\\n'
>>> test('-wclwcllc testinputs/arabic.txt')
b'\\t19\\t485\\t4898\\ttestinputs/arabic.txt\\n'
>>> test('-w testinputs/arabic.txt -c testinputs/arabic.txt')
b'\\t485\\t4898\\ttestinputs/arabic.txt\\n\\t485\\t4898\\ttestinputs/arabic.txt\\n\\t970\\t9796\\ttotal\\n'
>>> test('-l testinputs/arabic.txt -wc testinputs/arabic.txt -wl -c testinputs/arabic.txt')
b'\\t19\\t485\\t4898\\ttestinputs/arabic.txt\\n\\t19\\t485\\t4898\\ttestinputs/arabic.txt\\n\\t19\\t485\\t4898\\ttestinputs/arabic.txt\\n\\t57\\t1455\\t14694\\ttotal\\n'
>>> test('testinputs/arabic.txt -w testinputs/arabic.txt testinputs/arabic.txt -ww -c testinputs/arabic.txt')
b'\\t485\\t4898\\ttestinputs/arabic.txt\\n\\t485\\t4898\\ttestinputs/arabic.txt\\n\\t485\\t4898\\ttestinputs/arabic.txt\\n\\t485\\t4898\\ttestinputs/arabic.txt\\n\\t1940\\t19592\\ttotal\\n'

>>> test('testinputs/chinese.txt')
b'\\t21\\t1127\\t8483\\ttestinputs/chinese.txt\\n'
>>> test('-w testinputs/chinese.txt')
b'\\t1127\\ttestinputs/chinese.txt\\n'
>>> test('-l testinputs/chinese.txt')
b'\\t21\\ttestinputs/chinese.txt\\n'
>>> test('-c testinputs/chinese.txt')
b'\\t8483\\ttestinputs/chinese.txt\\n'
>>> test('-cw testinputs/chinese.txt')
b'\\t1127\\t8483\\ttestinputs/chinese.txt\\n'
>>> test('-cl testinputs/chinese.txt')
b'\\t21\\t8483\\ttestinputs/chinese.txt\\n'
>>> test('-wl testinputs/chinese.txt')
b'\\t21\\t1127\\ttestinputs/chinese.txt\\n'
>>> test('-wc testinputs/chinese.txt')
b'\\t1127\\t8483\\ttestinputs/chinese.txt\\n'
>>> test('-lc testinputs/chinese.txt')
b'\\t21\\t8483\\ttestinputs/chinese.txt\\n'
>>> test('-lw testinputs/chinese.txt')
b'\\t21\\t1127\\ttestinputs/chinese.txt\\n'
>>> test('-clw testinputs/chinese.txt')
b'\\t21\\t1127\\t8483\\ttestinputs/chinese.txt\\n'
>>> test('-wclwcllc testinputs/chinese.txt')
b'\\t21\\t1127\\t8483\\ttestinputs/chinese.txt\\n'
>>> test('-w testinputs/chinese.txt -c testinputs/chinese.txt')
b'\\t1127\\t8483\\ttestinputs/chinese.txt\\n\\t1127\\t8483\\ttestinputs/chinese.txt\\n\\t2254\\t16966\\ttotal\\n'
>>> test('-l testinputs/chinese.txt -wc testinputs/chinese.txt -wl -c testinputs/chinese.txt')
b'\\t21\\t1127\\t8483\\ttestinputs/chinese.txt\\n\\t21\\t1127\\t8483\\ttestinputs/chinese.txt\\n\\t21\\t1127\\t8483\\ttestinputs/chinese.txt\\n\\t63\\t3381\\t25449\\ttotal\\n'
>>> test('testinputs/chinese.txt -w testinputs/chinese.txt testinputs/chinese.txt -ww -c testinputs/chinese.txt')
b'\\t1127\\t8483\\ttestinputs/chinese.txt\\n\\t1127\\t8483\\ttestinputs/chinese.txt\\n\\t1127\\t8483\\ttestinputs/chinese.txt\\n\\t1127\\t8483\\ttestinputs/chinese.txt\\n\\t4508\\t33932\\ttotal\\n'

>>> test('testinputs/die.java')
b'\\t126\\t533\\t3608\\ttestinputs/die.java\\n'
>>> test('-w testinputs/die.java')
b'\\t533\\ttestinputs/die.java\\n'
>>> test('-l testinputs/die.java')
b'\\t126\\ttestinputs/die.java\\n'
>>> test('-c testinputs/die.java')
b'\\t3608\\ttestinputs/die.java\\n'
>>> test('-cw testinputs/die.java')
b'\\t533\\t3608\\ttestinputs/die.java\\n'
>>> test('-cl testinputs/die.java')
b'\\t126\\t3608\\ttestinputs/die.java\\n'
>>> test('-wl testinputs/die.java')
b'\\t126\\t533\\ttestinputs/die.java\\n'
>>> test('-wc testinputs/die.java')
b'\\t533\\t3608\\ttestinputs/die.java\\n'
>>> test('-lc testinputs/die.java')
b'\\t126\\t3608\\ttestinputs/die.java\\n'
>>> test('-lw testinputs/die.java')
b'\\t126\\t533\\ttestinputs/die.java\\n'
>>> test('-clw testinputs/die.java')
b'\\t126\\t533\\t3608\\ttestinputs/die.java\\n'
>>> test('-wclwcllc testinputs/die.java')
b'\\t126\\t533\\t3608\\ttestinputs/die.java\\n'
>>> test('-w testinputs/die.java -c testinputs/die.java')
b'\\t533\\t3608\\ttestinputs/die.java\\n\\t533\\t3608\\ttestinputs/die.java\\n\\t1066\\t7216\\ttotal\\n'
>>> test('-l testinputs/die.java -wc testinputs/die.java -wl -c testinputs/die.java')
b'\\t126\\t533\\t3608\\ttestinputs/die.java\\n\\t126\\t533\\t3608\\ttestinputs/die.java\\n\\t126\\t533\\t3608\\ttestinputs/die.java\\n\\t378\\t1599\\t10824\\ttotal\\n'
>>> test('testinputs/die.java -w testinputs/die.java testinputs/die.java -ww -c testinputs/die.java')
b'\\t533\\t3608\\ttestinputs/die.java\\n\\t533\\t3608\\ttestinputs/die.java\\n\\t533\\t3608\\ttestinputs/die.java\\n\\t533\\t3608\\ttestinputs/die.java\\n\\t2132\\t14432\\ttotal\\n'

>>> test('testinputs/emoji.txt')
b'\\t256\\t854\\t5401\\ttestinputs/emoji.txt\\n'
>>> test('-w testinputs/emoji.txt')
b'\\t854\\ttestinputs/emoji.txt\\n'
>>> test('-l testinputs/emoji.txt')
b'\\t256\\ttestinputs/emoji.txt\\n'
>>> test('-c testinputs/emoji.txt')
b'\\t5401\\ttestinputs/emoji.txt\\n'
>>> test('-cw testinputs/emoji.txt')
b'\\t854\\t5401\\ttestinputs/emoji.txt\\n'
>>> test('-cl testinputs/emoji.txt')
b'\\t256\\t5401\\ttestinputs/emoji.txt\\n'
>>> test('-wl testinputs/emoji.txt')
b'\\t256\\t854\\ttestinputs/emoji.txt\\n'
>>> test('-wc testinputs/emoji.txt')
b'\\t854\\t5401\\ttestinputs/emoji.txt\\n'
>>> test('-lc testinputs/emoji.txt')
b'\\t256\\t5401\\ttestinputs/emoji.txt\\n'
>>> test('-lw testinputs/emoji.txt')
b'\\t256\\t854\\ttestinputs/emoji.txt\\n'
>>> test('-clw testinputs/emoji.txt')
b'\\t256\\t854\\t5401\\ttestinputs/emoji.txt\\n'
>>> test('-wclwcllc testinputs/emoji.txt')
b'\\t256\\t854\\t5401\\ttestinputs/emoji.txt\\n'
>>> test('-w testinputs/emoji.txt -c testinputs/emoji.txt')
b'\\t854\\t5401\\ttestinputs/emoji.txt\\n\\t854\\t5401\\ttestinputs/emoji.txt\\n\\t1708\\t10802\\ttotal\\n'
>>> test('-l testinputs/emoji.txt -wc testinputs/emoji.txt -wl -c testinputs/emoji.txt')
b'\\t256\\t854\\t5401\\ttestinputs/emoji.txt\\n\\t256\\t854\\t5401\\ttestinputs/emoji.txt\\n\\t256\\t854\\t5401\\ttestinputs/emoji.txt\\n\\t768\\t2562\\t16203\\ttotal\\n'
>>> test('testinputs/emoji.txt -w testinputs/emoji.txt testinputs/emoji.txt -ww -c testinputs/emoji.txt')
b'\\t854\\t5401\\ttestinputs/emoji.txt\\n\\t854\\t5401\\ttestinputs/emoji.txt\\n\\t854\\t5401\\ttestinputs/emoji.txt\\n\\t854\\t5401\\ttestinputs/emoji.txt\\n\\t3416\\t21604\\ttotal\\n'

>>> test('testinputs/htmlTest.html')
b'\\t15\\t229\\t2488\\ttestinputs/htmlTest.html\\n'
>>> test('-w testinputs/htmlTest.html')
b'\\t229\\ttestinputs/htmlTest.html\\n'
>>> test('-l testinputs/htmlTest.html')
b'\\t15\\ttestinputs/htmlTest.html\\n'
>>> test('-c testinputs/htmlTest.html')
b'\\t2488\\ttestinputs/htmlTest.html\\n'
>>> test('-cw testinputs/htmlTest.html')
b'\\t229\\t2488\\ttestinputs/htmlTest.html\\n'
>>> test('-cl testinputs/htmlTest.html')
b'\\t15\\t2488\\ttestinputs/htmlTest.html\\n'
>>> test('-wl testinputs/htmlTest.html')
b'\\t15\\t229\\ttestinputs/htmlTest.html\\n'
>>> test('-wc testinputs/htmlTest.html')
b'\\t229\\t2488\\ttestinputs/htmlTest.html\\n'
>>> test('-lc testinputs/htmlTest.html')
b'\\t15\\t2488\\ttestinputs/htmlTest.html\\n'
>>> test('-lw testinputs/htmlTest.html')
b'\\t15\\t229\\ttestinputs/htmlTest.html\\n'
>>> test('-clw testinputs/htmlTest.html')
b'\\t15\\t229\\t2488\\ttestinputs/htmlTest.html\\n'
>>> test('-wclwcllc testinputs/htmlTest.html')
b'\\t15\\t229\\t2488\\ttestinputs/htmlTest.html\\n'
>>> test('-w testinputs/htmlTest.html -c testinputs/htmlTest.html')
b'\\t229\\t2488\\ttestinputs/htmlTest.html\\n\\t229\\t2488\\ttestinputs/htmlTest.html\\n\\t458\\t4976\\ttotal\\n'
>>> test('-l testinputs/htmlTest.html -wc testinputs/htmlTest.html -wl -c testinputs/htmlTest.html')
b'\\t15\\t229\\t2488\\ttestinputs/htmlTest.html\\n\\t15\\t229\\t2488\\ttestinputs/htmlTest.html\\n\\t15\\t229\\t2488\\ttestinputs/htmlTest.html\\n\\t45\\t687\\t7464\\ttotal\\n'
>>> test('testinputs/htmlTest.html -w testinputs/htmlTest.html testinputs/htmlTest.html -ww -c testinputs/htmlTest.html')
b'\\t229\\t2488\\ttestinputs/htmlTest.html\\n\\t229\\t2488\\ttestinputs/htmlTest.html\\n\\t229\\t2488\\ttestinputs/htmlTest.html\\n\\t229\\t2488\\ttestinputs/htmlTest.html\\n\\t916\\t9952\\ttotal\\n'

>>> test('testinputs/inferno2.txt')
b'\\t14920\\t102197\\t562492\\ttestinputs/inferno2.txt\\n'
>>> test('-w testinputs/inferno2.txt')
b'\\t102197\\ttestinputs/inferno2.txt\\n'
>>> test('-l testinputs/inferno2.txt')
b'\\t14920\\ttestinputs/inferno2.txt\\n'
>>> test('-c testinputs/inferno2.txt')
b'\\t562492\\ttestinputs/inferno2.txt\\n'
>>> test('-cw testinputs/inferno2.txt')
b'\\t102197\\t562492\\ttestinputs/inferno2.txt\\n'
>>> test('-cl testinputs/inferno2.txt')
b'\\t14920\\t562492\\ttestinputs/inferno2.txt\\n'
>>> test('-wl testinputs/inferno2.txt')
b'\\t14920\\t102197\\ttestinputs/inferno2.txt\\n'
>>> test('-wc testinputs/inferno2.txt')
b'\\t102197\\t562492\\ttestinputs/inferno2.txt\\n'
>>> test('-lc testinputs/inferno2.txt')
b'\\t14920\\t562492\\ttestinputs/inferno2.txt\\n'
>>> test('-lw testinputs/inferno2.txt')
b'\\t14920\\t102197\\ttestinputs/inferno2.txt\\n'
>>> test('-clw testinputs/inferno2.txt')
b'\\t14920\\t102197\\t562492\\ttestinputs/inferno2.txt\\n'
>>> test('-wclwcllc testinputs/inferno2.txt')
b'\\t14920\\t102197\\t562492\\ttestinputs/inferno2.txt\\n'
>>> test('-w testinputs/inferno2.txt -c testinputs/inferno2.txt')
b'\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t204394\\t1124984\\ttotal\\n'
>>> test('-l testinputs/inferno2.txt -wc testinputs/inferno2.txt -wl -c testinputs/inferno2.txt')
b'\\t14920\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t14920\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t14920\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t44760\\t306591\\t1687476\\ttotal\\n'
>>> test('testinputs/inferno2.txt -w testinputs/inferno2.txt testinputs/inferno2.txt -ww -c testinputs/inferno2.txt')
b'\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t408788\\t2249968\\ttotal\\n'

>>> test('testinputs/oneLine.txt')
b'\\t1\\t6\\t37\\ttestinputs/oneLine.txt\\n'
>>> test('-w testinputs/oneLine.txt')
b'\\t6\\ttestinputs/oneLine.txt\\n'
>>> test('-l testinputs/oneLine.txt')
b'\\t1\\ttestinputs/oneLine.txt\\n'
>>> test('-c testinputs/oneLine.txt')
b'\\t37\\ttestinputs/oneLine.txt\\n'
>>> test('-cw testinputs/oneLine.txt')
b'\\t6\\t37\\ttestinputs/oneLine.txt\\n'
>>> test('-cl testinputs/oneLine.txt')
b'\\t1\\t37\\ttestinputs/oneLine.txt\\n'
>>> test('-wl testinputs/oneLine.txt')
b'\\t1\\t6\\ttestinputs/oneLine.txt\\n'
>>> test('-wc testinputs/oneLine.txt')
b'\\t6\\t37\\ttestinputs/oneLine.txt\\n'
>>> test('-lc testinputs/oneLine.txt')
b'\\t1\\t37\\ttestinputs/oneLine.txt\\n'
>>> test('-lw testinputs/oneLine.txt')
b'\\t1\\t6\\ttestinputs/oneLine.txt\\n'
>>> test('-clw testinputs/oneLine.txt')
b'\\t1\\t6\\t37\\ttestinputs/oneLine.txt\\n'
>>> test('-wclwcllc testinputs/oneLine.txt')
b'\\t1\\t6\\t37\\ttestinputs/oneLine.txt\\n'
>>> test('-w testinputs/oneLine.txt -c testinputs/oneLine.txt')
b'\\t6\\t37\\ttestinputs/oneLine.txt\\n\\t6\\t37\\ttestinputs/oneLine.txt\\n\\t12\\t74\\ttotal\\n'
>>> test('-l testinputs/oneLine.txt -wc testinputs/oneLine.txt -wl -c testinputs/oneLine.txt')
b'\\t1\\t6\\t37\\ttestinputs/oneLine.txt\\n\\t1\\t6\\t37\\ttestinputs/oneLine.txt\\n\\t1\\t6\\t37\\ttestinputs/oneLine.txt\\n\\t3\\t18\\t111\\ttotal\\n'
>>> test('testinputs/oneLine.txt -w testinputs/oneLine.txt testinputs/oneLine.txt -ww -c testinputs/oneLine.txt')
b'\\t6\\t37\\ttestinputs/oneLine.txt\\n\\t6\\t37\\ttestinputs/oneLine.txt\\n\\t6\\t37\\ttestinputs/oneLine.txt\\n\\t6\\t37\\ttestinputs/oneLine.txt\\n\\t24\\t148\\ttotal\\n'

>>> test('testinputs/strangerThings.txt')
b'\\t117\\t702\\t13620\\ttestinputs/strangerThings.txt\\n'
>>> test('-w testinputs/strangerThings.txt')
b'\\t702\\ttestinputs/strangerThings.txt\\n'
>>> test('-l testinputs/strangerThings.txt')
b'\\t117\\ttestinputs/strangerThings.txt\\n'
>>> test('-c testinputs/strangerThings.txt')
b'\\t13620\\ttestinputs/strangerThings.txt\\n'
>>> test('-cw testinputs/strangerThings.txt')
b'\\t702\\t13620\\ttestinputs/strangerThings.txt\\n'
>>> test('-cl testinputs/strangerThings.txt')
b'\\t117\\t13620\\ttestinputs/strangerThings.txt\\n'
>>> test('-wl testinputs/strangerThings.txt')
b'\\t117\\t702\\ttestinputs/strangerThings.txt\\n'
>>> test('-wc testinputs/strangerThings.txt')
b'\\t702\\t13620\\ttestinputs/strangerThings.txt\\n'
>>> test('-lc testinputs/strangerThings.txt')
b'\\t117\\t13620\\ttestinputs/strangerThings.txt\\n'
>>> test('-lw testinputs/strangerThings.txt')
b'\\t117\\t702\\ttestinputs/strangerThings.txt\\n'
>>> test('-clw testinputs/strangerThings.txt')
b'\\t117\\t702\\t13620\\ttestinputs/strangerThings.txt\\n'
>>> test('-wclwcllc testinputs/strangerThings.txt')
b'\\t117\\t702\\t13620\\ttestinputs/strangerThings.txt\\n'
>>> test('-w testinputs/strangerThings.txt -c testinputs/strangerThings.txt')
b'\\t702\\t13620\\ttestinputs/strangerThings.txt\\n\\t702\\t13620\\ttestinputs/strangerThings.txt\\n\\t1404\\t27240\\ttotal\\n'
>>> test('-l testinputs/strangerThings.txt -wc testinputs/strangerThings.txt -wl -c testinputs/strangerThings.txt')
b'\\t117\\t702\\t13620\\ttestinputs/strangerThings.txt\\n\\t117\\t702\\t13620\\ttestinputs/strangerThings.txt\\n\\t117\\t702\\t13620\\ttestinputs/strangerThings.txt\\n\\t351\\t2106\\t40860\\ttotal\\n'
>>> test('testinputs/strangerThings.txt -w testinputs/strangerThings.txt testinputs/strangerThings.txt -ww -c testinputs/strangerThings.txt')
b'\\t702\\t13620\\ttestinputs/strangerThings.txt\\n\\t702\\t13620\\ttestinputs/strangerThings.txt\\n\\t702\\t13620\\ttestinputs/strangerThings.txt\\n\\t702\\t13620\\ttestinputs/strangerThings.txt\\n\\t2808\\t54480\\ttotal\\n'

>>> test('testinputs/test2.txt')
b'\\t8\\t22\\t141\\ttestinputs/test2.txt\\n'
>>> test('-w testinputs/test2.txt')
b'\\t22\\ttestinputs/test2.txt\\n'
>>> test('-l testinputs/test2.txt')
b'\\t8\\ttestinputs/test2.txt\\n'
>>> test('-c testinputs/test2.txt')
b'\\t141\\ttestinputs/test2.txt\\n'
>>> test('-cw testinputs/test2.txt')
b'\\t22\\t141\\ttestinputs/test2.txt\\n'
>>> test('-cl testinputs/test2.txt')
b'\\t8\\t141\\ttestinputs/test2.txt\\n'
>>> test('-wl testinputs/test2.txt')
b'\\t8\\t22\\ttestinputs/test2.txt\\n'
>>> test('-wc testinputs/test2.txt')
b'\\t22\\t141\\ttestinputs/test2.txt\\n'
>>> test('-lc testinputs/test2.txt')
b'\\t8\\t141\\ttestinputs/test2.txt\\n'
>>> test('-lw testinputs/test2.txt')
b'\\t8\\t22\\ttestinputs/test2.txt\\n'
>>> test('-clw testinputs/test2.txt')
b'\\t8\\t22\\t141\\ttestinputs/test2.txt\\n'
>>> test('-wclwcllc testinputs/test2.txt')
b'\\t8\\t22\\t141\\ttestinputs/test2.txt\\n'
>>> test('-w testinputs/test2.txt -c testinputs/test2.txt')
b'\\t22\\t141\\ttestinputs/test2.txt\\n\\t22\\t141\\ttestinputs/test2.txt\\n\\t44\\t282\\ttotal\\n'
>>> test('-l testinputs/test2.txt -wc testinputs/test2.txt -wl -c testinputs/test2.txt')
b'\\t8\\t22\\t141\\ttestinputs/test2.txt\\n\\t8\\t22\\t141\\ttestinputs/test2.txt\\n\\t8\\t22\\t141\\ttestinputs/test2.txt\\n\\t24\\t66\\t423\\ttotal\\n'
>>> test('testinputs/test2.txt -w testinputs/test2.txt testinputs/test2.txt -ww -c testinputs/test2.txt')
b'\\t22\\t141\\ttestinputs/test2.txt\\n\\t22\\t141\\ttestinputs/test2.txt\\n\\t22\\t141\\ttestinputs/test2.txt\\n\\t22\\t141\\ttestinputs/test2.txt\\n\\t88\\t564\\ttotal\\n'

>>> test('testinputs/test.txt')
b'\\t10\\t74\\t373\\ttestinputs/test.txt\\n'
>>> test('-w testinputs/test.txt')
b'\\t74\\ttestinputs/test.txt\\n'
>>> test('-l testinputs/test.txt')
b'\\t10\\ttestinputs/test.txt\\n'
>>> test('-c testinputs/test.txt')
b'\\t373\\ttestinputs/test.txt\\n'
>>> test('-cw testinputs/test.txt')
b'\\t74\\t373\\ttestinputs/test.txt\\n'
>>> test('-cl testinputs/test.txt')
b'\\t10\\t373\\ttestinputs/test.txt\\n'
>>> test('-wl testinputs/test.txt')
b'\\t10\\t74\\ttestinputs/test.txt\\n'
>>> test('-wc testinputs/test.txt')
b'\\t74\\t373\\ttestinputs/test.txt\\n'
>>> test('-lc testinputs/test.txt')
b'\\t10\\t373\\ttestinputs/test.txt\\n'
>>> test('-lw testinputs/test.txt')
b'\\t10\\t74\\ttestinputs/test.txt\\n'
>>> test('-clw testinputs/test.txt')
b'\\t10\\t74\\t373\\ttestinputs/test.txt\\n'
>>> test('-wclwcllc testinputs/test.txt')
b'\\t10\\t74\\t373\\ttestinputs/test.txt\\n'
>>> test('-w testinputs/test.txt -c testinputs/test.txt')
b'\\t74\\t373\\ttestinputs/test.txt\\n\\t74\\t373\\ttestinputs/test.txt\\n\\t148\\t746\\ttotal\\n'
>>> test('-l testinputs/test.txt -wc testinputs/test.txt -wl -c testinputs/test.txt')
b'\\t10\\t74\\t373\\ttestinputs/test.txt\\n\\t10\\t74\\t373\\ttestinputs/test.txt\\n\\t10\\t74\\t373\\ttestinputs/test.txt\\n\\t30\\t222\\t1119\\ttotal\\n'
>>> test('testinputs/test.txt -w testinputs/test.txt testinputs/test.txt -ww -c testinputs/test.txt')
b'\\t74\\t373\\ttestinputs/test.txt\\n\\t74\\t373\\ttestinputs/test.txt\\n\\t74\\t373\\ttestinputs/test.txt\\n\\t74\\t373\\ttestinputs/test.txt\\n\\t296\\t1492\\ttotal\\n'

>>> test('testinputs/arabic.txt testinputs/chinese.txt testinputs/die.java testinputs/emoji.txt testinputs/htmlTest.html testinputs/inferno2.txt testinputs/oneLine.txt testinputs/strangerThings.txt testinputs/test2.txt testinputs/test.txt')
b'\\t19\\t485\\t4898\\ttestinputs/arabic.txt\\n\\t21\\t1127\\t8483\\ttestinputs/chinese.txt\\n\\t126\\t533\\t3608\\ttestinputs/die.java\\n\\t256\\t854\\t5401\\ttestinputs/emoji.txt\\n\\t15\\t229\\t2488\\ttestinputs/htmlTest.html\\n\\t14920\\t102197\\t562492\\ttestinputs/inferno2.txt\\n\\t1\\t6\\t37\\ttestinputs/oneLine.txt\\n\\t117\\t702\\t13620\\ttestinputs/strangerThings.txt\\n\\t8\\t22\\t141\\ttestinputs/test2.txt\\n\\t10\\t74\\t373\\ttestinputs/test.txt\\n\\t15493\\t106229\\t601541\\ttotal\\n'

"""

if __name__ == "__main__":
     import doctest
     doctest.testmod()

# format("6 5 43 t.txt") returns "\\t6\\t5\\t43\\tt.txt\\n"
