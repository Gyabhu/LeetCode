class Solution:
    def reverseString(s):
        print(s[:])
        s[:] = s[::-1]
        return s


    arr = ["h","e","l","l", "o"]
    print(reverseString(arr))
