def sort_array(source_array):
    # Variables
    newList = ["" for i in range(len(source_array))]
    index = 0
    oddList = []

    # Sorting out odd numbers
    for number in source_array:
        if number % 2 != 0:
        
            oddList.append(number)
    oddList.sort()

    # Appending even and zero numbers
    for number in source_array:
        if number == 0: # zero case
            newList[index] = number

        elif number % 2 == 0: # even case
            newList[index] = number
        index += 1

    # Appending odd numbers
    for number in oddList:
        if "" in newList:
            index = newList.index("")
            newList[index] = number
            
    return newList

# Testing
print sort_array([5, 3, 2, 8, 1, 4])
print sort_array([5, 3, 1, 8, 0])
