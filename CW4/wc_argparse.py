# Created by mbaxtmp2 on 17/10/17

# TODO: --
# TODO: prefix bug

import sys
import argparse

def wc_argparse():

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lines', help='print the newline counts', action='store_true')
    parser.add_argument('-w', '--words', help='print the word counts', action="store_true")
    parser.add_argument('-c', '--bytes', help='print the byte counts', action='store_true')
    parser.add_argument('-m', '--chars', help='print the character counts', action="store_true")
    parser.add_argument('FILE', help='With no FILE, or when FILE is -, read standard input.', nargs='+')
    parser.add_argument('--files0-from=F [FILES0_FROM=F]', help='read input from the files specified by\nNUL-terminated names in file F;\nIf F is - then read names from standard input', nargs='?')

    arg_list = []

    for arg in sys.argv[1:]:
        if arg[0] == '-' and len(arg) > 1: #temporarely treat "-" as a file
            arg_list.insert(0, arg)
        else:
            arg_list.append(arg)
#    print(arg_list)

    args, unknown = parser.parse_known_args(arg_list)

#    print(args)
#    print(unknown)

    for arg in unknown:
        if len(arg) > 1 and arg[0] == '-' and arg[1].isalpha():
            invalid(arg[1])
        elif len(arg) > 1 and arg[0] == '-' and arg[1] == '-':
            unrecognized(arg)
        else:
            print ("*stdin not implemented yet") #should not be reachable yet

    total_line_count = 0
    total_word_count = 0
    total_byte_count = 0
    total_char_count = 0

    do_lines = True if args.lines else False
    do_words = True if args.words else False
    do_bytes = True if args.bytes else False
    do_chars = True if args.chars else False

    if not args.lines and not args.words and not args.bytes and not args.chars:  # no flags = -wcl
        do_lines = True
        do_words = True
        do_bytes = True

    for file in args.FILE:
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
                if do_chars:
                    char_count = count_chars(f)
                    print("\t" + str(char_count), end='')
                print("\t" + file)

                if len(args.FILE) > 1:
                    if do_lines:
                        total_line_count += line_count
                    if do_words:
                        total_word_count += word_count
                    if do_bytes:
                        total_byte_count += byte_count
                    if do_chars:
                        total_char_count += char_count

        except FileNotFoundError:
            print("wc: " + file + ": No such file or directory")
        except IsADirectoryError:
            print("wc: " + file + ": Is a directory")
            if do_lines: print("\t0", end='')
            if do_words: print("\t0", end='')
            if do_bytes: print("\t0", end='')
            if do_chars: print("\t0", end='')
            print("\t" + file)
    if len(args.FILE) > 1:
        if do_lines:
            print("\t" + str(total_line_count), end='')
        if do_words:
            print("\t" + str(total_word_count), end='')
        if do_bytes:
            print("\t" + str(total_byte_count), end='')
        if do_chars:
            print("\t" + str(total_char_count), end='')
        print("\ttotal")

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
    byte_count = 0
    for line in file:
        byte_count += len(line)
    file.seek(0)
    return byte_count

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
    wc_argparse()
