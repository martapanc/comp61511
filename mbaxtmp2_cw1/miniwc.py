#Created by mbaxtmp2 on 28/09/17

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

    byte_count = 0
    word_count = 0
    line_count = 0

    try:
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                words = line.split()
                line_count += 1
                word_count += len(words)
                byte_count += len(line.encode("utf8"))
            print(" " +str(line_count) + " " + str(word_count) + " " + str(byte_count) + " " + file)
    except FileNotFoundError:
        print("Error: file \"" + file + "\" not found.")
    #except UnicodeDecodeError:
       # print("Error: cannot read file \"" + file + "\" correctly.")

miniWc()

#implement the no argument case
