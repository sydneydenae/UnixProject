import sys

# Set Cipher num equal to input num
shiftNum = int(sys.argv[1])

for line in sys.stdin:
    newString = ""
    shiftString = ""
    spacedString = ""
    line = line.upper()

    #Discard everything but letters
    for char in line:
        if ord(char) > 64 and ord(char) < 91:
            newString += char

    #Shift
    for char in newString:
        newASC = ord(char) + shiftNum
        #If out of bounds
        if newASC > 90:
            newASC -= 26
        shiftString += chr(newASC)

    #Formatting
    count = 0
    for char in shiftString:
        if count == 5:
            spacedString += " "
            count = 0
        spacedString += char
        count += 1
    print(spacedString)

