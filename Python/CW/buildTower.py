def tower_builder(n_floors):
    # Debugging
    toPrint = False

    # Variables
    towerList = ["*"]
    index = 1
    floor = None
    maxLen = (n_floors * 2) - 1

    if toPrint:
        print "Max Len: ", maxLen
    
    # CONSTANT
    BLOCK = "*"
    SPACE = " "

    # First Floor
    space = (maxLen - index) / 2
    floor = SPACE * space
    floor += BLOCK * index
    floor += SPACE * space
    towerList = [floor]
    if toPrint:
        print "Here: "
        print "Space: ", space
        print "Floor: ", floor
        print "Tower List: ", towerList
    
    # Building tower
    for i in range(n_floors - 1):
        index += 2
        space = (maxLen - index) / 2
        floor = SPACE * space
        floor += BLOCK * index
        floor += SPACE * space
        towerList.append(floor)

        if toPrint:
            print "\n"
            print "Here 2: "
            print "Space: ", space
            print "Index: ", index
            print "Floor: ", floor
            print "Tower List: ", towerList

    return towerList

# Testing
print tower_builder(1)
print tower_builder(2)
print tower_builder(3)

