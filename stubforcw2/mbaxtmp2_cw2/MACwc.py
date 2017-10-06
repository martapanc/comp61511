# Created by mbaxtmp2 on 4/10/17

# python3 wc.py <flags> <files>
# 0       1     2       3     ...
# lines  words   bytes   file.txt

# OK - TODO: Add "Try 'wc --help' for more information."
# OK - TODO: improve to accept flags in the form "-mcl..."
# TODO: fix the bloody encoding thing
# TODO: reduce things a bit

import sys


def wc():
    args_len = len(sys.argv)
    if args_len < 2:
        print("*stdin not implemented yet*")
    else:
        all_valid_flags = True
        file_list = []
        flag_list = set([])  # avoid adding the same flag more than once if present

        for param in sys.argv[1:]:
            if param[0] == '-':
                cur_flag = param[1:]
                for cf in cur_flag:  # check cases with more flags. E.g.: -wc -cl -lwc
                    if check_flag(cf):
                        flag_list.add(cf)
                    else:
                        all_valid_flags = False
                        print(invalid_option(cf))
                        exit()
            else:
                file_list.append(param)  # If not preceded by "-", handle it as a file

        if all_valid_flags:
            if len(file_list) == 0:
                print("*stdin not implemented yet*")
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
                if len(file_list) > 1:
                    if do_lines:
                        print("\t" + str(total_line_count), end='')
                    if do_words:
                        print("\t" + str(total_word_count), end='')
                    if do_bytes:
                        print("\t" + str(total_byte_count), end='')
                    print("\t total")


def check_flag(argument):
    switcher = {
        'l': True,
        'w': True,
        'c': True
    }
    return switcher.get(argument, False)


def invalid_option(arg):
    return "wc: invalid option -- '" + str(arg) + "'\nTry 'wc --help' for more information."


def count_lines(file):
    line_count = 0
    for line in file:
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
        byte_count += len(line.encode("utf8"))
    file.seek(0)
    return byte_count


wc()
