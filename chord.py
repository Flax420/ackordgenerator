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
        

# Chord patterns start here


def chordMajor(dictNotes):
    pattern = (dictNotes[1], dictNotes[5], dictNotes[8])
    return(pattern)



# End of functions



# Default lists
dictNotes = {1:"a", 2:"a#", 3:"b", 4:"c", 5:"c#", 6:"d", 7:"d#", 8:"e", 9:"f", 10:"f#", 11:"g", 12:"g#"}
listNotes = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]
dictNumbers = {"a":1, "a#":2, "b":3, "c":4, "c#":5, "d":6, "d#":7, "e":8, "f":9, "f#":10, "g":11, "g#":12}
transList = []
transListNotes = []

# Start: input key (music) and transpose
s = input("Select key: ")
print()
n = dictNumbers[s]
transpose(transList, dictNumbers, n)
indexToNote(transListNotes, transList, listNotes)

# Print transposed notes
print("Transposed scale: ")
print(transListNotes)
print()

# Change dictionary according to transposition
changeDictNotes(transListNotes, dictNotes)

# Print transposed note dictionary
print("New dictionary: ")
print(dictNotes)
print()

# Print major chord
print("Major chord: ")
major = chordMajor(dictNotes)
print(major)
