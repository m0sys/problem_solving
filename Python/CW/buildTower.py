def tower_builder(n_floors):
    # Variables
    towerList = ["*"]
    index = 1
    floor = None
    maxLen = (n_floors * 2) - 1
    
    # CONSTANT
    BLOCK = "*"
    SPACE = " "

    # First Floor
    space = (maxLen - index) / 2
    floor = SPACE * space
    floor += BLOCK * index
    floor += SPACE * space
    towerList = [floor]
    
    # Building tower
    for i in range(n_floors - 1):
        index += 2
        space = (maxLen - index) / 2
        floor = SPACE * space
        floor += BLOCK * index
        floor += SPACE * space
        towerList.append(floor)

    return towerList

# Testing
print tower_builder(1)
print tower_builder(2)
print tower_builder(3)

