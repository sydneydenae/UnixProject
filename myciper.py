import sys
 
newString = ""

# Set Cipher num equal to input num
shiftNum = int(sys.argv[1])

for line in sys.stdin:
    newString = ""
    shiftString = ""
    line = line.upper()

    #Discard everything but letters
    for char in line:
        if ord(char) > 64 and ord(char) < 91:
            newString += char
    print(newString)

    #Shift
    for char in newString:
        newASC = ord(char) + shiftNum
        shiftString += chr(newASC)
    print(shiftString)
