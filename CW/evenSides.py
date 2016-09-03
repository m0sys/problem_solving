def find_even_index(arr):
    for index in range(len(arr)):
        if sum(arr[: index]) == sum(arr[index + 1 :]): # if left == right
            return index
            
    return -1

# Testing
print find_even_index([1,2,3,4,3,2,1])
print find_even_index(range(-100,-1))
