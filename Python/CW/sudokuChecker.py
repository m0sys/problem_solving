def done_or_not(board): #board[i][j]
    """
    return 'Finished!'
    ..
    or return 'Try again!'
    """

    # Constants
    COL_LIST = [[] for i in range (9)]

    # Row Test
    for row in board:
        if sum(row) != 45:
            return "Try again!"

        # Creating column lists
        listIndex = 0
        for num in row:
            COL_LIST[listIndex].append(num)
            listIndex += 1
    
    # Column Test
    for col in COL_LIST:
        if sum(col) != 45:
            return "Try again!"

    # Sector Test
    numRow = 0
    rowLimit = 3 # total number of rows needed for 3 sectors in 'board' 
    sum1 = 0 
    sum2 = 0
    sum3 = 0
    for row in board:
        # Going through the 3 sectors of 'row'
        numRow += 1
        start = 0
        end = 3
        sum1 += sum(row[start : end]) # sector #1

        start +=3  
        end += 3
        sum2 += sum(row[start : end]) # sector #2

        start += 3
        end += 3
        sum3 += sum(row[start: end]) # sector #3 

        if numRow == rowLimit:
            if sum1 != 45 or sum2 != 45 or sum3 != 45:
                return "Try again!"
            # Reset for next 3 sectors of 'board'
            sum1 = 0
            sum2 = 0
            sum3 = 0
            numRow = 0
            
    return "Finished!"

# Testing
print done_or_not([
    [1, 3, 2, 5, 7, 9, 4, 6, 8],
    [4, 9, 8, 2, 6, 1, 3, 7, 5],
    [7, 5, 6, 3, 8, 4, 2, 1, 9],
    [6, 4, 3, 1, 5, 8, 7, 9, 2],
    [5, 2, 1, 7, 9, 3, 8, 4, 6],
    [9, 8, 7, 4, 2, 6, 5, 3, 1],
    [2, 1, 4, 9, 3, 5, 6, 8, 7],
    [3, 6, 5, 8, 1, 7, 9, 2, 4],
    [8, 7, 9, 6, 4, 2, 1, 5, 3]])

print done_or_not([
    [1, 3, 2, 5, 7, 9, 4, 6, 8],
    [4, 9, 8, 2, 6, 1, 3, 7, 5],
    [7, 5, 6, 3, 8, 4, 2, 1, 9],
    [6, 4, 3, 1, 5, 8, 7, 9, 2],
    [5, 2, 1, 7, 9, 3, 8, 4, 6],
    [9, 8, 7, 4, 2, 6, 5, 3, 1],
    [2, 1, 4, 9, 3, 5, 6, 8, 7],
    [3, 6, 5, 8, 1, 7, 9, 2, 4],
    [8, 7, 9, 6, 4, 2, 1, 3, 5]])

print done_or_not([
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]])

