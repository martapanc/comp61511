#Created by Marta Pancaldi (10228373) on 28/09/17

import sys

def countWords(file):
    word_count = 0
    print(file)
    for line in file:
        print(line)
        words = line.split()
        word_count += len(words)
    return word_count

def countLines(file):
    line_count = 0
    for line in file:
        line_count += 1
    return line_count



def countBytes(file):
    byte_count = 0
    for line in file:
        words = line.split()
        byte_count += len(line.encode("utf8"))
    return byte_count

def miniWc():
    args_len = len(sys.argv)
    if args_len == 2:
        file = sys.argv[1]
    elif args_len > 2:
        print("Only one file as argument.")
        exit()
    else:
        print("No file argument was inserted.")
        exit()

    byte_count = 0
    word_count = 0
    line_count = 0

    try:
        with open(file, 'r', encoding='utf8') as f:
            line_count = countLines(f)
            word_count = countWords(f)
            byte_count = countBytes(f)
            # for line in f:
            #     words = line.split()
            #     line_count += 1
            #     word_count += len(words)
            #     byte_count += len(line.encode("utf8"))
            print("\t" +str(line_count) + "\t" + str(word_count) + "\t" + str(byte_count) + "\t" + file)
    except FileNotFoundError:
        print("Error: file \"" + file + "\" not found.")
    except UnicodeDecodeError:
        print("Error: cannot read file \"" + file + "\" correctly.")



miniWc()
