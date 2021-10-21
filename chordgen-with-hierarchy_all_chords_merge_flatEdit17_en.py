def transpose(transList, dictNumbers, n):
    for x in dictNumbers:
        value = dictNumbers[x] - (14-n)
        forInToList(transList, value)
    return(None)

def forInToList(transList, value):
    transList.append(value)
    return(transList)

def indexToNote(transListNotes, transList, listNotes):
    for x in transList:
        newValue = listNotes[x]
        forInToList(transListNotes, newValue)
    return(transListNotes)

def changeDictNotes(transListNotes, dictNotes):
    n = 0    
    for x in dictNotes:
        dictNotes[x] = getValueFromTransListNotes(transListNotes, n)
        n = n+1
        
def getValueFromTransListNotes(transListNotes, n):
    return(transListNotes[n])

def hierarchy(dictNotes):
    hierarchyDict = {"a1":3, "a#1":2, "b1":1, "c1":12, "c#1":11, "d1":10, "d#1":9, "e1":8, "f1":7, "f#1":6, "g1":5, "g#1":4}
    n = 0
    tempHierarchy = []
    for x in dictNotes:
        #print(dictNotes[x])
        #print(x)
        tempHierarchy.append(hierarchyDict[dictNotes[x]])
    tempHierarchy.append(int("100"))
    #print(tempHierarchy)
    n = 0
    tempNoteList = []
    for x in range(len(dictNotes)):
        n = n+1
        tempNoteList.append(dictNotes[n])
    #print(tempNoteList)
    n2 = 0
    dictNotesCopy = dict(dictNotes)
    for x in dictNotes:
        if hierarchyDict[dictNotes[x]] > tempHierarchy[x]:
            pass
            #print(dictNotes[x])
            #print(hierarchyDict[dictNotes[x]])
            #print(tempHierarchy[x])
        elif tempHierarchy[x] == 100:
            quit()
        else:
            #print(dictNotes[x])
            sS1 = tempNoteList[x]
            LC = int(lastChar(sS1)) + 1
            sS2 = removeLastChar(sS1) + str(LC)
            #print(sS2)
            getKey = splitPattern(sS1, dictNotesCopy)
            dictNotesCopy[getKey] = sS2
            #print(dictNotesCopy)
            n2 = n2+1
            if tempHierarchy[x+1] == 100:
                return(dictNotesCopy)
            else:
                tempHierarchy[x+1] = 99

def splitPattern(x, dictNotes):
    key_list = list(dictNotes.keys())
    val_list = list(dictNotes.values())
    position = val_list.index(x)
    return(key_list[position])

def lastChar(LC):
    last_char = LC[-1:]
    return(last_char)

def removeLastChar(sS):
    my_str =  sS
    my_str = my_str[:-1]
    return(my_str)

def octavizer(dictNotes, pattern):
    chNumList = []
    chNumListMod = []
    patternList = []
    for x in pattern:
        y = splitPattern(x, dictNotes)
        chNumList.append(y)
        chNumListMod.append(y)
        patternList.append(x)
#    print(chNumList)
#    print(patternList)
    chNumListMod.append(0) #append 0 so that (x-1) < element 1
#    print(chNumListMod)
    n = 0
    for x in range(len(chNumListMod)):
        if chNumListMod[x-1] > chNumListMod[x] and chNumListMod[x] in chNumList: #throw away appended 0, because it is not in chNumList
            sS1 = dictNotes[chNumListMod[x]]            
            LC = int(lastChar(sS1)) + 1
            sS2 = removeLastChar(sS1) + str(LC)
            #print(sS2)           
            patternList[n] = sS2
            chNumListMod[x] = 100 #after first octavization, octavize all remaining notes
            n = n+1
        else:
            n = n+1
    return(patternList)

def listToTuple(list):
    return tuple(list)

def tupleToList(tuple):
    return list(tuple)



'''
********************************************************************
*************************  chords start here  **********************
********************************************************************
********************************************************************
'''



# minor chords
def m(dictNotes):
    pattern = (dictNotes[1], dictNotes[4], dictNotes[8])
    return(pattern)

def m7(dictNotes):
    pattern = (dictNotes[1], dictNotes[4], dictNotes[8], dictNotes[11])
    return(pattern)

def m7b5(dictNotes):
    pattern = (dictNotes[1], dictNotes[4], dictNotes[7], dictNotes[11])
    return(pattern)

def mM7(dictNotes):
    pattern = (dictNotes[1], dictNotes[4], dictNotes[8], dictNotes[12])
    return(pattern)

def m6(dictNotes):
    pattern = (dictNotes[1], dictNotes[4], dictNotes[8], dictNotes[10])
    return(pattern)

def m9(dictNotes):
    pattern = (dictNotes[1], dictNotes[4], dictNotes[8], dictNotes[11], dictNotes[3])
    getOctaveList = octavizer(dictNotes, pattern)
    tupledOctave = listToTuple(getOctaveList)
    return(tupledOctave)

def m11(dictNotes):
    pattern = (dictNotes[1], dictNotes[4], dictNotes[8], dictNotes[11], dictNotes[3], dictNotes[6])
    getOctaveList = octavizer(dictNotes, pattern)
    tupledOctave = listToTuple(getOctaveList)
    return(tupledOctave)

def m13(dictNotes):
    pattern = (dictNotes[1], dictNotes[4], dictNotes[8], dictNotes[11], dictNotes[3], dictNotes[6], dictNotes[10])
    getOctaveList = octavizer(dictNotes, pattern)
    tupledOctave = listToTuple(getOctaveList)
    return(tupledOctave)



# 5, major and dom7 chords
def ch5(dictNotes):
    pattern = (dictNotes[1], dictNotes[8])
    return(pattern)

def major(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[8])
    return(pattern)

def ch7(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[8], dictNotes[11])
    return(pattern)

def ch7s5(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[9], dictNotes[11])
    return(pattern)

def ch9(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[8], dictNotes[11], dictNotes[3])
    getOctaveList = octavizer(dictNotes, pattern)
    tupledOctave = listToTuple(getOctaveList)
    return(tupledOctave)

def ch11(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[8], dictNotes[11], dictNotes[3], dictNotes[6])
    getOctaveList = octavizer(dictNotes, pattern)
    tupledOctave = listToTuple(getOctaveList)
    return(tupledOctave)

def ch13(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[8], dictNotes[11], dictNotes[3], dictNotes[6], dictNotes[10])
    getOctaveList = octavizer(dictNotes, pattern)
    tupledOctave = listToTuple(getOctaveList)
    return(tupledOctave)



# maj7 and 6 chords
def maj7(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[8], dictNotes[12])
    return(pattern)

def maj9(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[8], dictNotes[12], dictNotes[3])
    getOctaveList = octavizer(dictNotes, pattern)
    tupledOctave = listToTuple(getOctaveList)
    return(tupledOctave)

def maj13(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[8], dictNotes[12], dictNotes[3], dictNotes[10])
    getOctaveList = octavizer(dictNotes, pattern)
    tupledOctave = listToTuple(getOctaveList)
    return(tupledOctave)

def ch6(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[8], dictNotes[10])
    return(pattern)

def ch6_9(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[8], dictNotes[10], dictNotes[3])
    getOctaveList = octavizer(dictNotes, pattern)
    tupledOctave = listToTuple(getOctaveList)
    return(tupledOctave)



# add, sus, dim, aug
def add2(dictNotes):
    pattern = (dictNotes[1], dictNotes[3], dictNotes[5], dictNotes[8])
    return(pattern)

def add9(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[8], dictNotes[3])
    getOctaveList = octavizer(dictNotes, pattern)
    tupledOctave = listToTuple(getOctaveList)
    return(tupledOctave)

def sus2(dictNotes):
    pattern = (dictNotes[1], dictNotes[3], dictNotes[8])
    return(pattern)

def sus4(dictNotes):
    pattern = (dictNotes[1], dictNotes[6], dictNotes[8])
    return(pattern)

def dim(dictNotes):
    pattern = (dictNotes[1], dictNotes[4], dictNotes[7])
    return(pattern)

def dim7(dictNotes):
    pattern = (dictNotes[1], dictNotes[4], dictNotes[7], dictNotes[10])
    return(pattern)

def aug(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[9])
    return(pattern)

def aug7(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[9], dictNotes[11])
    return(pattern)



# End of chords

def selectKey():
    s = input("Select key: ")
    FC = firstCharUpperLower(s)
    s = stringSplitMerge(s, FC)
    return(s)

def firstCharUpperLower(s):
    first_char = s[0]
    if first_char.isupper():
        first_char = first_char.lower()
    else:
        pass
    return(first_char)

def firstCharLowerUpper(s):
    first_char = s[0]
    if first_char.islower():
        first_char = first_char.upper()
    else:
        pass
    return(first_char)

def stringSplitMerge(s, FC):
    stringSplitList = []
    for x in s:
        stringSplitList.append(x)
    stringSplitList[0] = FC
    str1 = ""
    for x in stringSplitList:
        str1 += x
    return(str1)

def checkIfValid(s):
    validList = ["c", "c#", "db", "d", "d#", "eb", "e", "f", "f#", "gb", "g", "g#", "ab", "a", "a#", "bb", "b"]
    while True:
        if s in validList:
            return(s)
        else:
            s = selectKey()

def stringSplitMerge2(s, FC):
    stringSplitList = []
    for x in s:
        stringSplitList.append(x)
    stringSplitList[1] = FC
    str1 = ""
    for x in stringSplitList:
        str1 += x
    return(str1)

def stringSplitMerge3(s, FC):
    stringSplitList = []
    for x in s:
        stringSplitList.append(x)
    stringSplitList[-2] = FC
    str1 = ""
    for x in stringSplitList:
        str1 += x
    return(str1)

def flatToSharp(s, fsToken):
    if lastChar(s) == "b" and len(s) > 1:
        s1 = stringSplitMerge2(s, "#")
        first_char = s[0]
        subst1 = alphabet(first_char)
        s2 = stringSplitMerge(s1, subst1)
        fsToken.append(s)
        return(s2)
    else:
        return(s)
        
def alphabet(first_char):
    alphabet = {"g":"f", "f":"e", "e":"d", "d":"c", "c":"b", "b":"a", "a":"g"}
    return(alphabet[first_char])

def alphabetRev(first_char):
    alphabet = {"f":"g", "e":"f", "d":"e", "c":"d", "b":"c", "a":"b", "g":"a"}
    return(alphabet[first_char])

def listToString(aList):
    str1 = ""
    for x in aList:
        str1 += x
    return(str1)

def chordTrigger(s, fsToken, hierarchyList):
    if len(fsToken) > 0:
        key = listToString(fsToken)
        FC = firstCharLowerUpper(key)
        newKey = stringSplitMerge(key, FC)
    else:
        key = s
        FC = firstCharLowerUpper(key)
        newKey = stringSplitMerge(key, FC)
    print()
    print("List of chords: ")
    print()
    print("1: " + newKey)
    print("2: " + newKey + "m")
    print("3: " + newKey + "m7")
    print("4: " + newKey + "m7b5")
    print("5: " + newKey + "mM7")
    print("6: " + newKey + "m6")
    print("7: " + newKey + "m9")
    print("8: " + newKey + "m11")
    print("9: " + newKey + "m13")
    print("10: " + newKey + "5")
    print("11: " + newKey + "7")
    print("12: " + newKey + "7#5")
    print("13: " + newKey + "9")
    print("14: " + newKey + "11")
    print("15: " + newKey + "13")
    print("16: " + newKey + "maj7")
    print("17: " + newKey + "maj9")
    print("18: " + newKey + "maj13")
    print("19: " + newKey + "6")
    print("20: " + newKey + "6/9")
    print("21: " + newKey + "add2")
    print("22: " + newKey + "add9")
    print("23: " + newKey + "sus2")
    print("24: " + newKey + "sus4")
    print("25: " + newKey + "dim")
    print("26: " + newKey + "dim7")
    print("27: " + newKey + "aug")
    print("28: " + newKey + "aug7")
    print()
    while True:
        chordBook = {1:"major", 2:"m", 3:"m7", 4:"m7b5", 5:"mM7", 6:"m6", 7:"m9", 8:"m11", 9:"m13", 10:"ch5", 11:"ch7", 12:"ch7s5", 13:"ch9", 14:"ch11", 15:"ch13", 16:"maj7", 17:"maj9", 18:"maj13", 19:"ch6", 20:"ch6_9", 21:"add2", 22:"add9", 23:"sus2", 24:"sus4", 25:"dim", 26:"dim7", 27:"aug", 28:"aug7"}
        i = input("Select a chord: ")
        if 1 <= int(i) <= 28:
            function_name = chordBook[int(i)]
            chord = eval(function_name)(hierarchyList)
            return(chord)
        else:
            pass

def displayCorrectChord(fsToken, chordTuple):
    if len(fsToken) > 0:
        tempChList = tupleToList(chordTuple)
        n = -1
        for x in tempChList:
            n = n+1
            if x[-2] == "#":
                y = stringSplitMerge3(x, "b")
                alphabet = alphabetRev(y[0])
                z = stringSplitMerge(y, alphabet)
                tempChList[n] = z
        n2 = -1
        for x in tempChList:
            n2 = n2+1
            capital = firstCharLowerUpper(x)
            proper = stringSplitMerge(x, capital)
            tempChList[n2] = proper
        return(tempChList)
    else:
        tempChList = tupleToList(chordTuple)
        n2 = -1
        for x in tempChList:
            n2 = n2+1
            capital = firstCharLowerUpper(x)
            proper = stringSplitMerge(x, capital)
            tempChList[n2] = proper
        return(tempChList)
            
# End of functions



'''
//////////////////////  GLOBAL AREA  //////////////////////
'''



while True:
    # Default lists
    dictNotes = {1:"a1", 2:"a#1", 3:"b1", 4:"c1", 5:"c#1", 6:"d1", 7:"d#1", 8:"e1", 9:"f1", 10:"f#1", 11:"g1", 12:"g#1"}
    listNotes = ["a1", "a#1", "b1", "c1", "c#1", "d1", "d#1", "e1", "f1", "f#1", "g1", "g#1"]
    dictNumbers = {"a":1, "a#":2, "b":3, "c":4, "c#":5, "d":6, "d#":7, "e":8, "f":9, "f#":10, "g":11, "g#":12}
    transList = []
    transListNotes = []
    fsToken = []

    # Start: input key (music) and transpose

    s = selectKey()
    s = checkIfValid(s)
    s = flatToSharp(s, fsToken)

    #print(fsToken)
    #print(s)

    n = dictNumbers[s]
    transpose(transList, dictNumbers, n)
    indexToNote(transListNotes, transList, listNotes)

    #print("Transposed scale: ")
    #print(transListNotes)
    #print()

    # Change dictionary according to transposition
    changeDictNotes(transListNotes, dictNotes)

    # Transposed note dictionary
    #print("New dictionary: ")
    #print(dictNotes)
    if s != "c": # OBS! för att c (default scale, all octave 1) ska fungera
        hierarchyList = hierarchy(dictNotes)
    #    print()
    #    print("Hierarkiskt dictionary för skalan: ")
    #    print()
    #    print(hierarchyList)
    else:
        hierarchyList = dictNotes # Hädanefter är hierarchyList main dictionary



    # Chord trigger
    '''
    >>>>>> send chordTuple to GUI
    '''

    chordTuple = chordTrigger(s, fsToken, hierarchyList)
    #print(chordTuple)
    


    '''
    |||||||||||||||||  Pre GUI   |||||||||||||||||
    '''








    '''
    |||||||||||||||||  Post GUI  |||||||||||||||||
    '''



    # Only for display

    displayChordList = displayCorrectChord(fsToken, chordTuple)
    displayChordTuple = listToTuple(displayChordList)
    print()
    print("Notes:")
    print()
    print(displayChordTuple)
    
    # Restart or exit
    
    print()
    while True:
        restart = input("Press r to try another chord, or press q to exit. ")
        if restart == "r":
            break
        elif restart == "q":
            break
        else:
            pass
    if restart == "r":
        print()
        pass
    elif restart == "q":
        break
