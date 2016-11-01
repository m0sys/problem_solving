def solution(s):
    # Checking odd or even
    if len(s) % 2 != 0:
        tempStr = s + "_"
    else:
        tempStr = s

    # Variables
    newList = []

    # Splitting string
    while tempStr != "":
        newList.append(tempStr[: 2])
        tempStr = tempStr[2 :]

    return newList

# Testing
print solution("asdfadsf")
print solution("asdfads")
print solution("")
print solution("x")
