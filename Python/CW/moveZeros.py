def move_zeros(array):
    # Variables
    newList = ["" for i in range(len(array))]
    zeroIndex = len(array) - 1
    charIndex = 0

    # Looking for zeros
    for e in array:                        
        if e == 0 and str(e) != "False" and str(e) != "True":
            newList[zeroIndex] = 0
            zeroIndex -= 1

        # Adding the other characters to list
        else:
            newList[charIndex] = e
            charIndex += 1

    return newList

# Testing
print move_zeros([1,2,0,1,0,1,0,3,0,1])
print move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])
print move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9])
print move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
print move_zeros([0,1,None,2,False,1,0])
print move_zeros(["a","b"])
print move_zeros(["a"])
print move_zeros([0,0])
print move_zeros([0])
print move_zeros([])
