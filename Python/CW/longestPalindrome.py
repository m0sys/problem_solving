def isPal(n):
    return str(n) == str(n)[:: -1]

def substrings(string):
    # Constants
    LENGTH = len(string)

    return [string[i : j + 1] for i in xrange(LENGTH) for j in xrange(i, LENGTH)] # enumerating a possible substrings

def longest_palindrome(s):

    # Simple cases
    if len(s) == 0:
        return 0

    if len(s) == 1:
        return 1

    if len(s) == 2:
        if isPal(s):
            return 2

    # Constants
    SUBSTR_LIST = substrings(s)

    # Variables
    ans = 0

    for string in SUBSTR_LIST:
        if isPal(string) and len(string) > ans:
            ans = len(string)

    return ans

# Testing
print longest_palindrome("a")
print longest_palindrome("aa")
print longest_palindrome("baa")
print longest_palindrome("aab")
print longest_palindrome("abcdefghba")
print longest_palindrome("baablkj12345432133d")



    



