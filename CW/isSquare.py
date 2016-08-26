def is_square(n):    
    import math
    
    # Checking to see if n is a negative number
    if n < 0:
      return False
      
    # Taking the integer part of the sqrt of n
    x = int(math.sqrt(n))
    
    # Testing to see if square of x is equal to n
    return n == x * 
