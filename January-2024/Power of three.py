"""
    Given an integer n, return true if it is a power of three. Otherwise, return false.
    An integer n is a power of three, if there exists an integer x such that n == 3x.

"""
class Solution:
    def isPowerOfThree(n):
        if n == 1:
            return True
        power = 1
        while (3**power <= n):
            if (3**power == n):
                return True
            else:
                power += 1
        return False
    print(isPowerOfThree(1))
