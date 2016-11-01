def order(sentence):
    # Debugging
    toPrint = True

    # Constants
    STR_LIST = sentence.split()
    STR = "".join(STR_LIST)
    NUMBERS = "123456789"

    # Variables
    newList = [0 for i in range(len(STR_LIST))]
    newString = ""

    # Main loop
    for word in STR_LIST:
        if toPrint:
            print "My word: ", word
        for char in word:
            ## if type(char) == int:
            if char in NUMBERS:
                newList[int(char) - 1] = word
                if toPrint:
                    print "My Char: ", char
                    print "New List: ", newList
                    print "\n"

    # Building new string
    for word in newList:
        newString += word + " "
        if toPrint:
            print "Word = ", word
            print "New String = ", newString
            print "\n"


    newString = newString[: -1] # removing final space
    print "My New String: ", newString
    return newString

    

# Testing
print order("is2 Thi1s T4est 3a")
