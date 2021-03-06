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
        all_valid_flags = True
        file_list = []
        flag_list = set([])  # avoid adding the same flag more than once if present

        for param in sys.argv[1:]:
            if len(param)>2 and param[0] == '-' and param[1] == '-':
                unrecognized(param)
            elif param == '--':
                not_implem()
            elif param[0] == '-' and len(param)>1:
                cur_flag = param[1:]
                for cf in cur_flag:  # check cases with more flags. E.g.: -wc -cl -lwc
                    if check_flag(cf, param):
                        flag_list.add(cf)
                    else:
                        all_valid_flags = False
                        invalid(cf)
            else:
                file_list.append(param)  # If not preceded by "-", handle it as a file

        if all_valid_flags:
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

def check_flag(flag, param):
    if flag == '-':
        return invalid(flag)
    if not flag.isalpha():
        return False
    if flag == 'l' or flag == 'w' or flag == 'c':
        return True
    else:
        return False

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
    print("wc: invalid option -- '" + str(option) + "'\nTry 'wc --help' for more information.")
    exit()

def unrecognized(option):
    print("wc: unrecognized option '" + str(option) + "'\nTry 'wc --help' for more information.")
    exit()

def not_implem():
    print("*stdin not implemented yet*")
    exit()


if __name__ == "__main__":
   wc()
