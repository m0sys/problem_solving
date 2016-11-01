import itertools

def findsubsets(s, m):
    return set(itertools.combinations(s, m))

def closest_sum(ints, num):
    # Constants
    SUB_SETS = findsubsets(ints, 3)

    # Variables
    delta = None
    myList = None

    for s in SUB_SETS:
        if delta == None:
            delta = abs(sum(s) - num)
            myList = s

        else:
            if abs(sum(s) - num) < delta:
                delta = abs(sum(s) - num)
                myList = s

    return (list(myList), sum(myList))

# Testing
print closest_sum([-1, 2, 1, -4], 1)
print closest_sum([5, 4, 0, 3], 3)
print closest_sum([1, 2, 3, 4], 4)
print closest_sum([-2, 2, -3, 1], 3)
