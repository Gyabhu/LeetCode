"""
    Given an integer n, return true if it is a cubic root.
    PS: This is a modification of the power of three problem

"""
class Solution:
    def isCubeRoot(n):
        i = 1
        while (i**3 <= n):
            if i**3 == n:
                return True
            else:
                i += 1
        return False
    print(isCubeRoot(1000))
