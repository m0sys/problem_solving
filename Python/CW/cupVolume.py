def cup_volume(d1, d2, height):
    import math

    # Volume of a truncated cone: v = 1/3pi * (r_1 ** 2 + r_1 * r_2 + r_2 ** 2) * h

    # Calculating radius as a float
    r1 = float(d1) / 2
    r2 = float(d2) / 2
    height = float(height)

    # Calculating vol of cup
    v = math.pi * (1.0 / 3.0) * (r1 ** 2 + r1 * r2 + r2 ** 2) * height
    
    # Rounding to two decimal places and returning result
    return round (v, 2)

# Testing
print cup_volume(1, 1, 1)
print "\n"
print cup_volume(10, 8, 10)
print "\n"
print  cup_volume(1000, 1000, 1000)
