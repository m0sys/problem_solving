# Global Variables
globalList = []

class Primes:
    @staticmethod
    def isPrime(n):
        if n <= 1:
            return False

        # Case handling
        if n == 2:
            return True

        # Exceptions to efficency factor below
        if n <= 9:
            for i in range(2, n):
                if n % i == 0:
                    return False

            return True

        else:
            for i in range(2, int(round(n ** 0.5)) + 1):
                if n % i == 0:
                    return False
            return True
        
    @staticmethod
    def first(amount):
        # Variables
        primeList = []
        currentNum = 3

        # Memoization
        if len(globalList) >= amount:
            return globalList[: amount]
        else:
            if globalList != []:
                primeList = list(globalList)
                
                if globalList[-1] == 2: # case handling
                    currentNum = 3
                else:
                    currentNum = globalList[-1] + 2

        # Main loop
        while len(primeList) != amount:
            # Case handling
            if len(primeList) == 0 and amount > 0:
                primeList.append(2)
                globalList.append(2) # memorizing
                
            else:
                if Primes.isPrime(currentNum):
                    primeList.append(currentNum)
                    globalList.append(currentNum) # memorizing
                    currentNum += 2
                else:
                    currentNum += 2
        return primeList

# Testing
print Primes.first(1)
print Primes.first(2)
print Primes.first(5)
print Primes.first(100)[99]
