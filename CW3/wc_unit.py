# Created by mbaxtmp2 on 4/10/17

# python3 wc.py <flags> <files>
# 0       1     2       3     ...
# lines  words   bytes   file.txt

import sys


def wc():
    args_len = len(sys.argv)
    if args_len < 2:
        not_implem()
    else:
        file_list = []
        flag_list = [] # avoid adding the same flag more than once if present
        flags_are_valid = True

        flags_are_valid, flag_list, file_list = all_valid_args(sys.argv[1:])

        if flags_are_valid:
            print(compute_result(flag_list, file_list))


def compute_result(flag_list, file_list):
    if len(file_list) == 0:
        not_implem()
    else:
        total_line_count = 0
        total_word_count = 0
        total_byte_count = 0

        do_lines = True if "l" in flag_list else False
        do_words = True if "w" in flag_list else False
        do_bytes = True if "c" in flag_list else False

        if len(flag_list) == 0:  # no flags = -wcl
            do_lines = True
            do_words = True
            do_bytes = True

        for file in file_list:
            try:
                with open(file, 'r', encoding='utf8') as f:
                    if do_lines:
                        line_count = count_lines(f)
                        print("\t" + str(line_count), end='')
                    if do_words:
                        word_count = count_words(f)
                        print("\t" + str(word_count), end='')
                    if do_bytes:
                        byte_count = count_bytes(f)
                        print("\t" + str(byte_count), end='')
                    print("\t" + file)

                    if len(file_list) > 1:
                        if do_lines:
                            total_line_count += line_count
                        if do_words:
                            total_word_count += word_count
                        if do_bytes:
                            total_byte_count += byte_count
            except FileNotFoundError:
                print("wc: " + file + ": No such file or directory")
            except IsADirectoryError:
                print("wc: " + file + ": Is a directory") # replicate wc's behaviour if one of the args is a directory - ugly, I know
                if do_lines: print("\t0", end='')
                if do_words: print("\t0", end='')
                if do_bytes: print("\t0", end='')
                print("\t" + file)
        if len(file_list) > 1:
            if do_lines:
                print("\t" + str(total_line_count), end='')
            if do_words:
                print("\t" + str(total_word_count), end='')
            if do_bytes:
                print("\t" + str(total_byte_count), end='')
            print("\ttotal")


def check_flag(flag):
    #if flag == '-':
    #    invalid(flag)
    #    return False
    if not flag.isalpha():
        return False
    if flag == 'l' or flag == 'w' or flag == 'c':
        return True
    else:
        return False

def all_valid_args(args):
    file_list = []
    flag_list = set([])
    for param in args:
        if len(param)>2 and param[0] == '-' and param[1] == '-':
            unrecognized(param)
            #return False, {}, []
        elif param == '--':
            not_implem()
        elif param[0] == '-' and len(param)>1:
            cur_flag = param[1:]
            for cf in cur_flag:  # check cases with more flags. E.g.: -wc -cl -lwc
                if check_flag(cf):
                    flag_list.add(cf)
                else:
                    invalid(cf)
                    #return False, {}, []
        else:
            file_list.append(param)  # If not preceded by "-", handle it as a file
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


def invalid(option):
    sys.exit("wc: invalid option -- '" + str(option) + "'\nTry 'wc --help' for more information.")

def unrecognized(option):
    sys.exit("wc: unrecognized option '" + str(option) + "'\nTry 'wc --help' for more information.")

def not_implem():
    sys.exit("*stdin not implemented yet*")

if __name__ == "__main__":
   wc()
