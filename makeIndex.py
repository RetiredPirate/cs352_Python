import sys
import re

################################################################
# createIndex function:
# - Should print an index of all words in the file. It is presently
# dummied up.
#
# If you do the enhancement where you process multiple files, the
# 'fileName' parameter should be a list of strings rather than
# a single string.
################################################################
def createIndex(fileName) :
    """
    Print each word in the given file with the line numbers on
    which it appears
    """

    lineList = open(fileName, "r").readlines()
    outList = []
    wordLineList = []

    for line in lineList:
        line = re.sub("[^a-zA-Z' ]+", " ", line).lower().split()
        for word in line:
            if word.startswith("'") and word.endswith("'"):
                line[line.index(word)] = word[1:-1]
            elif word.startswith("'"):
                line[line.index(word)] = word[1:]

        #todo: remove dupes!!!
        line = list(set(line))
        wordLineList.append(line) #split into words, no dupes


    allWords = []
    for line in wordLineList:
        for word in line:
            allWords.append(word)

    # no dupes list of all words
    allWords = list(set(allWords))
    allWords.sort()

    # for each word, get a list of the word and each line it appears on
    for word in allWords:
        indexList = [word,]
        for line in wordLineList:
            if word in line:
                indexList.append(wordLineList.index(line) + 1)

        outList.append(indexList)


    # format string to Print
    outString = ""
    for word in outList:
        outString += word[0] + " " + str(word[1])
        for num in word[2:]:
            outString += ", " + str(num)
        outString += "\n"

    print(outString)

################################################################
# main program:
# - prompts user for a file name
# - reads input from user
# - calls createIndex
################################################################

# prompt user and read the input line
fileName = input("Please type the name of a file: ")

# call createIndex
createIndex(fileName)
