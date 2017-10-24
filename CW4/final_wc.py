# Created by mbaxtmp2 on 20/10/17

#find . -type f -print0 | wc --files0-from=-
#find (dir) [-type f] -print0 | wc [flags] --files0-from=-

import sys

def wc():
    args_len = len(sys.argv) #stdin case
    if args_len < 2:
        compute_result([], ['-'], sys.argv)
    else:
        file_list = flag_list = []
        flags_are_valid = True
        flags_are_valid, flag_list, file_list = all_valid_args(sys.argv[1:])
        if flags_are_valid:
            result = compute_result(flag_list, file_list, sys.argv)
#            print("\n\n" + result)

def compute_result(flag_list, file_list, args):
    if len(file_list) == 0: #stdin case
        file_list.append('-')
    # The program prints counts file by file (to be consistent with wc's behaviour),
    # however a string with the final output is built for testing purposes
    resultString = ''
    total_line_count = total_word_count = total_byte_count = total_char_count = total_max_line_count = 0

    do_lines = True if "l" in flag_list else False
    do_words = True if "w" in flag_list else False
    do_bytes = True if "c" in flag_list else False
    do_chars = True if "m" in flag_list else False
    do_max_line = True if "L" in flag_list else False

    if len(flag_list) == 0:  # If no flags are specified, the result is the same as -lwc
        do_lines = do_words = do_bytes = True

    for file in file_list:
        if file == '-': # Handle stdin
            stdin_content = '';
            for line in sys.stdin:
                stdin_content += line
            resultString += stdin_content

            std_line, std_word, std_char, std_byte, std_max_line = count_stdin(stdin_content, do_lines, do_words, do_chars, do_bytes, do_max_line)
            total_line_count += std_line
            total_word_count += std_word
            total_char_count += std_char
            total_byte_count += std_byte
            if total_max_line_count < std_max_line:
                total_max_line_count = std_max_line
            if do_lines: # Print only the counts requested by the flags
                print("\t" + str(std_line), end='')
                resultString += "\t" + str(std_line)
            if do_words:
                print("\t" + str(std_word), end='')
                resultString += "\t" + str(std_word)
            if do_chars:
                print("\t" + str(std_char), end='')
                resultString += "\t" + str(std_char)
            if do_bytes:
                print("\t" + str(std_byte), end='')
                resultString += "\t" + str(std_byte)
            if do_max_line:
                print("\t" + str(std_max_line), end='')
                resultString += "\t" + str(std_max_line)
            if '-' in args: # If '-' is among the arguments, '-' is printed after the counts (as it was a file name), otherwise nothing is printed
                print("\t-")
                resultString += "\t-\n"
            else:
                print("\t")
                resultString += "\t\n"
        else: # Do counts for all files
            try:
                with open(file, 'r', encoding='utf8') as f:
                    if do_lines:
                        line_count = count_lines(f)
                        print("\t" + str(line_count), end='')
                        resultString += "\t" + str(line_count)
                    if do_words:
                        word_count = count_words(f)
                        print("\t" + str(word_count), end='')
                        resultString += "\t" + str(word_count)
                    if do_chars:
                        char_count = count_chars(f)
                        print("\t" + str(char_count), end='')
                        resultString += "\t" + str(char_count)
                    if do_bytes:
                        byte_count = count_bytes(f)
                        print("\t" + str(byte_count), end='')
                        resultString += "\t" + str(byte_count)
                    if do_max_line:
                        max_count = get_max_line(f)
                        print("\t" + str(max_count), end='')
                        resultString += "\t" + str(max_count)
                    print("\t" + file)
                    resultString += "\t" + file + "\n"

                    if len(file_list) > 1: # If more than one file is specified, the total sum of the counts is displayed
                        if do_lines: total_line_count += line_count
                        if do_words: total_word_count += word_count
                        if do_chars: total_char_count += char_count
                        if do_bytes: total_byte_count += byte_count
                        if do_max_line:
                            if total_max_line_count < max_count:
                                total_max_line_count = max_count

            except FileNotFoundError:
                print("wc: " + file + ": No such file or directory")
                resultString += "wc: " + file + ": No such file or directory\n"
            except IsADirectoryError:
                print("wc: " + file + ": Is a directory")
                resultString += "wc: " + file + ": Is a directory\n" # Replicate wc's behaviour if one of the args is a directory
                if do_lines:
                    print("\t0", end='')
                    resultString += "\t0"
                if do_words:
                    print("\t0", end='')
                    resultString += "\t0"
                if do_chars:
                    print("\t0", end='')
                    resultString += "\t0"
                if do_bytes:
                    print("\t0", end='')
                    resultString += "\t0"
                if do_max_line:
                    print("\t0", end='')
                    resultString += "\t0"
                print("\t" + file)
                resultString += "\t" + file + "\n"
    if len(file_list) > 1:
        if do_lines:
            print("\t" + str(total_line_count), end='')
            resultString += "\t" + str(total_line_count)
        if do_words:
            print("\t" + str(total_word_count), end='')
            resultString += "\t" + str(total_word_count)
        if do_chars:
            print("\t" + str(total_char_count), end='')
            resultString += "\t" + str(total_char_count)
        if do_bytes:
            print("\t" + str(total_byte_count), end='')
            resultString += "\t" + str(total_byte_count)
        if do_max_line:
            print("\t" + str(total_max_line_count), end='')
            resultString += "\t" + str(total_max_line_count)
        print("\ttotal")
        resultString += "\ttotal\n"
    return resultString


def check_flag(flag):
# Check args with single (-w, -c, -l, ...) or multiple flags (-wcl, -lL, ...)
    validFlags = ['l', 'w', 'c', 'm', 'L']
    if not flag.isalpha():
        return False
    if flag in validFlags:
        return True
    else:
        return False


def check_long_flag(flag):
# If the flag is valid, the short version is returned
    valid_flags = {'bytes': 'c', 'chars': 'm', 'lines': 'l', 'max-line-length': 'L', 'words': 'w',
                    'c':'c', 'w':'w', 'm':'m', 'l':'l', 'L':'L', # wc also recognises --w, --c, etc.
                    'help': 'help', 'version': 'version', 'h':'help', 'v':'version'}
#    if not flag.isalpha():
#        return False
    if flag in valid_flags:
        return True, valid_flags[flag]
    elif 'files0-from=' in flag:
        return True, flag
    else:
        return False

def all_valid_args(args):
# Returns true if all arguments are valid (or exits if the arg is invalid/unrecognized, or if 'version'/'help' is invoked)
    file_list = files0_list = []
    flag_list = set([])
    double_dash_in_args = False
    files0_in_args = False
    for param in args:
        if double_dash_in_args: #if -- is an arg, all args (including -- itselg) after it are treated as files regardless if they are or not (except -)
            file_list.append(param)
        else:
            if len(param)>2 and param[:2] == '--': # Long-version flags (--lines, --words, ...)
                if check_long_flag(param[2:]):
                    var, short_flag = check_long_flag(param[2:])
                    if short_flag == "version":
                        version()
                    elif short_flag == "help":
                        show_help()
                    elif "files0-from=" in short_flag: # Check if the flag is in the form "--files0-from=..."
                        files0_in_args = True
                        files0_list = files0(short_flag[12:])
                    else:
                        flag_list.add(short_flag)
                else:
                    unrecognized(param)
            elif param == '--':
                double_dash_in_args = True
            elif param[0] == '-' and len(param)>1: # Short-version flags (-w, -c, -m, -wc...)
                cur_flag = param[1:]
                for cf in cur_flag:  # check cases with more flags. E.g.: -wc -cl -lwc
                    if check_flag(cf):
                        flag_list.add(cf)
                    else:
                        invalid(cf)
            else:
                file_list.append(param)  # If not preceded by "-", handle it as a file
    if len(file_list) > 0 and files0_in_args: # If --files0-from is present, there cannot be other files as args
        return extra_operand(file_list[0])
    elif files0_in_args:
        print("files0")
        return True, flag_list, files0_list
        #files0_list = files0()
    else:
        return True, flag_list, file_list

def count_lines(file):
    line_count = 0
    for line in file:
        if "\n" in line:
            line_count += 1
    file.seek(0)  # restores pointer at the beginning of file
    return line_count

def count_words(file):
    word_count = 0
    for line in file:
        words = line.split()
        word_count += len(words)
    file.seek(0)
    return word_count

def count_bytes(file):
    byte_count = 0
    for line in file:
        byte_count += len(line.encode("utf-8"))
    file.seek(0)
    return byte_count

def count_chars(file):
    char_count = 0
    for line in file:
        char_count += len(line)
    file.seek(0)
    return char_count

def get_max_line(file):
    max_count = 0
    for line in file:
        line_length = len(line)
        if line_length > max_count:
            max_count = line_length-1
    file.seek(0)
    return max_count

def count_stdin(stdin_content, do_lines, do_words, do_chars, do_bytes, do_max_line):
# Handle counts for stdin
    line_count = word_count = byte_count = char_count = max_line_count = 0
    for line in stdin_content.split("\n"):
        if do_max_line:
            if len(line) > max_line_count:
                max_line_count = len(line)
        if do_lines:  line_count +=1
    if do_words:
        words = stdin_content.split()
        word_count += len(words)
    if do_chars: char_count += len(stdin_content.encode("utf-8"))
    if do_bytes:  byte_count += len(stdin_content)
    return line_count-1, word_count, char_count, byte_count, max_line_count

def files0(short_flag):
    if short_flag == '-':
        #sys.exit("stdin: " + sys.stdin.read())
        stdin_content = sys.stdin.read()
        file_list = stdin_content.split("\x00")
        return file_list
    else:
        file_name = short_flag
        try:
            with open(file_name, 'r', encoding='utf8') as file:
                file_content = ''
                for line in file:
                    file_content += line
                file_list = file_content.split("\x00") # Files must be separated by the NULL character
                return file_list
        except FileNotFoundError:
            sys.exit("wc: cannot open '" + file_name + "' for reading: No such file or directory")
        except IsADirectoryError:
            sys.exit("wc: " + file_name + ": read error: Is a directory")

def invalid(option):
    sys.exit("wc: invalid option -- '" + str(option) + "'\nTry 'wc --help' for more information.")

def unrecognized(option):
    sys.exit("wc: unrecognized option '" + str(option) + "'\nTry 'wc --help' for more information.")

def extra_operand(file):
    sys.exit("wc: extra operand '" + file + "'\nfile operands cannot be combined with --files0-from\nTry 'wc --help' for more information.")

def version():
    sys.exit("wc.py 4.0 - Python implementation of\n"
        + "  \"wc (GNU coreutils) 8.25\n"
        + "  Copyright (C) 2016 Free Software Foundation, Inc.\n"
        + "  Written by Paul Rubin and David MacKenzie.\"\n\n"
        + "Created by Marta Pancaldi\n"
        + "Final project of the course \'Software Engineering Concepts in Practice\' 2017 \n  by Dr Bijan Parsia @ The University of Manchester\n\n"
        + "License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.\n"
        + "This is free software: you are free to change and redistribute it.\n"
        + "There is NO WARRANTY, to the extent permitted by law.\n")

def show_help():
    sys.exit("Usage: wc [OPTION]... [FILE]...\nor:  wc [OPTION]... --files0-from=F\n"
        + "Print newline, word, and byte counts for each FILE, and a total line if\nmore than one FILE is specified.  A word is a non-zero-length sequence of"
        + "characters delimited by white space. \n\n"
        + "With no FILE, or when FILE is -, read standard input.\n\n"
        + "The options below may be used to select which counts are printed, always in\nthe following order: newline, word, character, byte, maximum line length.\n"
        + "  -c, --bytes            print the byte counts\n"
        + "  -m, --chars            print the character counts\n"
        + "  -l, --lines            print the newline counts\n"
        + "      --files0-from=F    read input from the files specified by\n"
        + "                           NUL-terminated names in file F;\n"
        + "                           If F is - then read names from standard input\n"
        + "  -L, --max-line-length  print the maximum display width\n"
        + "  -w, --words            print the word counts \n"
        + "      --help     display this help and exit\n"
        + "      --version  output version information and exit\n\n"
        + "GNU coreutils online help: <http://www.gnu.org/software/coreutils/>\nFull documentation at: <http://www.gnu.org/software/coreutils/wc>\n"
        + "or available locally via: info '(coreutils) wc invocation'")

if __name__ == "__main__":
   wc()
