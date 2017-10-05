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
                totalLineCount = 0
                totalWordCount = 0
                #totalCharCount = 0
                totalByteCount = 0

                if len(flagList) == 0:
                    for file in fileList:
                        try:
                            with open(file, 'r', encoding='utf8') as f:
                                line_count = countLines(f)
                                word_count = countWords(f)
                                byte_count = countBytes(f)
                                if len(fileList) > 1:
                                    totalLineCount += line_count
                                    totalWordCount += word_count
                                    totalByteCount += byte_count
                                print ("  " + str(line_count) + "\t" + str(word_count) + "\t" + str(byte_count) + "\t" + file)
                        except FileNotFoundError:
                            print("wc: " + file + ": No such file or directory")
                    if len(fileList) > 1:
                        print("  " + str(totalLineCount) + "\t" + str(totalWordCount) + "\t" + str(totalByteCount) + "\t total")
                else:
                    doLines = True if "l" in flagList else False
                    doWords = True if "w" in flagList else False
                    doBytes = True if "c" in flagList else False
                    #doChars = True if "m" in flagList else False

                    for file in fileList:
                        try:
                            with open(file, 'r', encoding='utf8') as f:
                                if doLines:
                                    line_count = countLines(f)
                                    print(" " + str(line_count), end='')
                                if doWords:
                                    word_count = countWords(f)
                                    print(" " + str(word_count), end='')
                                # if doChars:
                                #     char_count = countBytes(f)
                                #     print(" " + str(char_count), end='')
                                if doBytes:
                                    byte_count = countBytes(f)
                                    print(" " + str(byte_count), end='')
                                print(" " + file)

                                if len(fileList) > 1:
                                    if doLines: totalLineCount += line_count
                                    if doWords: totalWordCount += word_count
                                    # if doChars: totalCharCount += char_count
                                    if doBytes: totalByteCount += byte_count

                                #print ("  " + str(line_count) + "\t" + str(word_count) + "\t" + str(byte_count) + "\t" + file)
                        except FileNotFoundError:
                            print("wc: " + file + ": No such file or directory")
                    if len(fileList) > 1:
                        if doLines: print(" " + str(totalLineCount), end='')
                        if doWords: print(" " + str(totalWordCount), end='')
                        #if doChars: print(" " + str(totalCharCount), end='')
                        if doBytes: print(" " + str(totalByteCount), end='')
                        print("\t total")

def checkFlag(argument):
    switcher = {
        'l': True,
        'w': True,
#        'm': True,
        'w': True
    }
    return switcher.get(argument, False)

def invalidOption(arg):
    return "wc: invalid option -- '" + str(arg) + "'\nTry 'wc --help' for more information."

def countLines(file):
    line_count = 0
    for line in file:
        line_count += 1
    file.seek(0) #restores pointer at the beginning of file
    return line_count

def countWords(file):
    word_count = 0
    for line in file:
        words = line.split()
        word_count += len(words)
    file.seek(0)
    return word_count

def countBytes(file):
    byte_count = 0
    for line in file:
        byte_count += len(line.encode("utf8"))
    file.seek(0)
    return byte_count

def countChars(file):
    char_count = 0
    for line in file:
        char_count += len(line.encode("utf8"))
    file.seek(0)
    return char_count

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
