#Created by mbaxtmp2 on 4/10/17

#python3 wc.py <flags> <files>
# 0       1     2       3     ...
# lines  words   bytes   file.txt

#TODO: Add "Try 'wc --help' for more information."
#TODO: improve to accept flags in the form "-mcl..."
#TODO: fix the bloody encoding thing

import sys

def wc():
    args_len = len(sys.argv)
    if args_len < 2 :
        print ("*stdin not implemented yet*")
    else:
        allValidFlags=True
        fileList = []
        flagList = []

        for param in sys.argv[1:]:
            if param[0] == '-':
                curFlag = param[1:]
                if checkFlag(curFlag):
                    flagList.append(curFlag)
                else:
                    allValidFlags = False
                    print(invalidOption(curFlag))
                    exit()
            else:
                fileList.append(param)
        if allValidFlags :
            if len(fileList) == 0 :
                print ("*stdin not implemented yet*")
            else:
                print (sys.argv[1:])
                print (fileList)

                if flagList == 0:
                    print("no flags") #compute all 3 values
                else:


                    if "-l" in flagList:
                        line_count = count




            #print(param)

    #print(numbers_to_strings(3))

def checkFlag(argument):
    switcher = {
        'w': "words",
        'c': "bytes",
        'l': "lines",
        'm': "*char count not implemented yet*"
    }
    return switcher.get(argument, False)
    #return switcher.get(argument, invalidOption(argument))

def invalidOption(arg):
    return "wc: invalid option -- '" + str(arg) + "'"

def countLines(file):
    line_count = 0
    for line in file:
        line_count += 1
    return line_count

def countWords(file):
    word_count = 0
    for line in file:
        words = line.split()
        word_count += len(words)
    return word_count

def countBytes(file):
    byte_count = 0
    for line in file:
        words = line.split()
        byte_count += len(line.encode("utf8"))
    return byte_count

def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, invalidOption(argument))

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

wc()

#miniWc()

#implement the no argument case
