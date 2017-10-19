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
        flag_list = []
        flags_are_valid = True

        flags_are_valid, flag_list, file_list = all_valid_args(sys.argv[1:])
        if flags_are_valid:
            print(compute_result(flag_list, file_list))


def compute_result(flag_list, file_list):
    if len(file_list) == 0:
        not_implem()
    else:
        resultString = ''
        total_line_count = 0
        total_word_count = 0
        total_byte_count = 0
        total_char_count = 0
        total_max_line_count = 0

        do_lines = True if "l" in flag_list else False
        do_words = True if "w" in flag_list else False
        do_bytes = True if "c" in flag_list else False
        do_chars = True if "m" in flag_list else False
        do_max_line = True if "L" in flag_list else False

        if len(flag_list) == 0:  # no flags = -wcl
            do_lines = True
            do_words = True
            do_bytes = True

        for file in file_list:
            try:
                with open(file, 'r', encoding='utf8') as f:
                    if do_lines:
                        line_count = count_lines(f)
                        resultString += "\t" + str(line_count)
                    if do_words:
                        word_count = count_words(f)
                        resultString += "\t" + str(word_count)
                    if do_chars:
                        char_count = count_chars(f)
                        resultString += "\t" + str(char_count)
                    if do_bytes:
                        byte_count = count_bytes(f)
                        resultString += "\t" + str(byte_count)
                    if do_max_line:
                        max_count = get_max_line(f)
                        resultString += "\t" + str(max_count)

                    resultString += "\t" + file + "\n"

                    if len(file_list) > 1:
                        if do_lines: total_line_count += line_count
                        if do_words: total_word_count += word_count
                        if do_chars: total_char_count += char_count
                        if do_bytes: total_byte_count += byte_count
                        if do_max_line:
                            if total_max_line_count < max_count:
                                total_max_line_count = max_count

            except FileNotFoundError:
                resultString += "wc: " + file + ": No such file or directory\n"
            except IsADirectoryError:
                resultString += "wc: " + file + ": Is a directory\n" # replicate wc's behaviour if one of the args is a directory - ugly, I know
                if do_lines: resultString += "\t0"
                if do_words: resultString += "\t0"
                if do_chars: resultString += "\t0"
                if do_bytes: resultString += "\t0"
                if do_max_line: resultString += "\t0"
                resultString += "\t" + file + "\n"
        if len(file_list) > 1:
            if do_lines: resultString += "\t" + str(total_line_count)
            if do_words: resultString += "\t" + str(total_word_count)
            if do_chars: resultString += "\t" + str(total_char_count)
            if do_bytes: resultString += "\t" + str(total_byte_count)
            if do_max_line: resultString += "\t" + str(total_max_line_count)
            resultString += "\ttotal\n"
        return resultString


def check_flag(flag):
    #if flag == '-':
    #    invalid(flag)
    #    return False
    validFlags = ['l', 'w', 'c', 'm', 'L']
    if not flag.isalpha():
        return False
    if flag in validFlags:
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

def get_max_line(file):
    max_count = 0
    for line in file:
        if len(line) > max_count:
            max_count = len(line)-1
    file.seek(0)
    return max_count


def invalid(option):
    sys.exit("wc: invalid option -- '" + str(option) + "'\nTry 'wc --help' for more information.")

def unrecognized(option):
    sys.exit("wc: unrecognized option '" + str(option) + "'\nTry 'wc --help' for more information.")

def not_implem():
    sys.exit("*stdin not implemented yet*")

if __name__ == "__main__":
   wc()
