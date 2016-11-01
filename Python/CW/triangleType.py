import math
# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):

    # Sanity check
    if 0 in {a, b , c}:
        return 0

    # Junk 
    j1 = float(b**2 + c**2 - a**2) / float(2*b*c)
    j2 = float(a**2 + c**2 - b**2) / float(2*a*c)
    j3 = float(a**2 + b**2 - c**2) / float(2*a*b)

    # Sanity check
    if j1 > 1 or j1 <= -1:
        return 0
    
    if j2 > 1 or j2 <= -1:
        return 0
    
    if j3 > 1 or j3 <= -1:
        return 0
      
    # Calculating angles
    x = math.degrees(math.acos(j1))
    y = math.degrees(math.acos(j2))
    z = math.degrees(math.acos(j3))

    # Acute test
    if x < 90 and y < 90 and z < 90:
        return 1
      
    # Right angle test
    ## if x == 90 or y == 90 or z == 90:
    if 90 in {x, y, z}:
        return 2
      
    # Obtuse angle test
    if x > 90 or y > 90 or z > 90:
        return 3
    
    # Sanity check
    if x + y + z > 180 or 180 in {x, y, z}: 
        return 0
