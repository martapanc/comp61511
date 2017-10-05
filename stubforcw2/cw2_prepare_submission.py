#!/usr/bin/env python
from pathlib import Path
import argparse
import zipfile
assignment_name = "cw2"

file_structure = map(Path, ['wc.py', 'testinputs', 'doctest_wc.py'])
file_structure = zip(file_structure, [10, 3,7])
stubs = {'wc.py':'', 'doctest_wc.py':''}

def contents(path):
    with path.open('r') as f:
        return f.read()
        
def test_contents_if_necessary(path,stubs):
    if path.exists() and path.is_dir():
        if len(list(path.iterdir())):
            return True
        else:
            return False
    if path.name in stubs.keys():
        return (contents(path).strip() != stubs[path.name].strip())
    else:
        return True
def make_submission(assignment, username, dir, structure):
    dirp = Path(dir)
    target_name = '%s_%s'%(username, assignment)
    print('Creating zipped file called %s for submission.' % (target_name + '.zip'))
    try:
        sub = zipfile.ZipFile(target_name + '.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
    except NotImplementedError:
        sub = zipfile.ZipFile(target_name + '.zip', mode='w')

    total = 0
    possible = 0
    missing = ''
    for p, mark in structure:
        total += mark
        cur_file = dirp / p
        if cur_file.exists() and test_contents_if_necessary(cur_file, stubs):
            sub.write(str(cur_file), str(Path(target_name) / p))
            possible += mark
        else:
            missing += '\t%s (0 out of %d points)\n' % (str(p), mark)
    sub.close()
    if missing:
        print('''Your submission is missing (or you haven't edited) the following files:

%s

This may be due to you putting them in the wrong place, some typo in the 
names, you haven't produced them, or you haven't edited the stub files.

This means your submission can get a MAXIMUM of %d out of a total of %d marks!

So check the instructions, fix the problem, and try again.''' % (missing, possible, total))
    else:
        print('''Your submission seems reasonable.
Note that we didn't check the correctness of any file, just that it 
existed and/or was different from the stubs.''')
    print('\nYour submittable archive is called %s' % target_name + '.zip')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sanity check and prepare your %s for upload to Blackboard.' % assignment_name)
    parser.add_argument('username', help="Your central username, often looks like 'mbassbp2'.")
    parser.add_argument('srcdir', help="The path to the directory containing all the parts of your submission. You can use a relative path from the directory you run the script in.")
    args = parser.parse_args()

    make_submission(assignment_name, args.username, args.srcdir, file_structure)
