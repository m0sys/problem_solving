# Find the sum of the digits of 
# all the numbers from 1 to N (both ends included).
def compute_sum(n):
    # Variables
    sumN = 0

    for num in range(1, n + 1):
        if num >= 10: # the 'twisted' part
            num = str(num)
            for index in range(len(num)):
                sumN += int(num[index])
        else:
            sumN += num

    return sumN
    pass

# Testing
print compute_sum(1)
print compute_sum(2)
print compute_sum(3)
print compute_sum(4)
print compute_sum(10)
print compute_sum(11)
