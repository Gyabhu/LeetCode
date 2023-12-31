class Solution:
    def isPalindrome(s):
        string= ""
        for char in s:
            if char.isalnum():
                string += char.lower()
        print(string)

        return string == string[::-1]


    arr = "A man, a plan, a canal: Panama"
    print(isPalindrome(arr))
