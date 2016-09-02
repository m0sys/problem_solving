def reverseWords(str):
    # Variables
    newStr = ""
    strList = str.split()

    strList.reverse() # reversing list

    # Adding words backwards
    for e in strList:
        newStr += e + " "
        
    newStr = newStr[: -1] # removing final space
    return newStr

# Testing
print reverseWords("hello world!")

