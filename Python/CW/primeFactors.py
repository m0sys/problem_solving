def primeFactors(n):
    # Variables
    strFact = ""
    tempNum = n
    factor = 2
    power = 0

    # Case handling
    while (n % factor) == 0:
        n /= factor
        power += 1

    if power != 0:
        if power == 1:
            strFact += "(" + str(factor) + ")"
        else:
            strFact += "(" + str(factor) + "**" + str(power) + ")"

    factor = 3
    power = 0

    # Main loop
    while factor * factor <= n: # no reason in continuing if 'current factor ** 2' > n since 'current factor + 1 ** 2' > 'current factor * current factor + 1' > 'current factor ** 2' > n
        while (n % factor) == 0: # counting number of 'current factor' in n
            power += 1
            n /= factor

        if power != 0:
            if power == 1:
                strFact += "(" + str(factor) + ")"
            else:
                strFact += "(" + str(factor) + "**" + str(power) + ")"

        factor += 2 # odd numbers only
        power = 0

    if n > 1: # n is now a prime factor
        strFact += "(" + str(n) + ")"

    return strFact
