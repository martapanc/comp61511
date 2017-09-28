#Created by Marta Pancaldi (10228373) on 28/09/17

import sys

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

    char_count = 0
    word_count = 0
    line_count = 0

    try:
        with open(file, 'r') as f:
            for line in f:
                words = line.split()
                line_count += 1
                word_count += len(words)
                char_count += len(line)
            print("\t" +str(line_count) + "\t" + str(word_count) + "\t" + str(char_count) + "\t" + file)
    except FileNotFoundError:
            print("Error: file \"" + file + "\" not found.")

miniWc()
