#Created by Marta Pancaldi (10228373) on 28/09/17

import sys

def miniWcComplete():
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
    char_count = 0
    word_count = 0
    line_count = 0

    format = file[-4:]
    if format in ['.pdf', 'docx', '.doc']:
        encoding = 'latin1'
    else:
        encoding = "utf8"

    try:
        with open(file, 'r', encoding=encoding) as f:
            for line in f:
                words = line.split()
                line_count += 1
                word_count += len(words)
                char_count += len(line)
                byte_count += len(line.encode('utf8'))
                #Use of UTF-8 Encoding - test this script with htmlTest.html to see the difference, as often #Bytes = #chars in simple text files
            print("\t" +str(line_count) + "\t" + str(word_count) + "\t" + str(char_count)+ "\t" + str(byte_count) + "\t" + file)
            #Result:    lines   words   chars   bytes   filename
    except FileNotFoundError:
            print("Error: file \"" + file + "\" not found.")
    except UnicodeDecodeError:
            print("Error: cannot read file \"" + file + "\" correctly.")

miniWcComplete()
