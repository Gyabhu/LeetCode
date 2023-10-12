'''
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters
    of a different word or phrase, typically using all the original
    letters exactly once.



        Example 1:

        Input: s = "anagram", t = "nagaram"
        Output: true

        Example 2:

        Input: s = "rat", t = "car"
        Output: false


        Constraints:

        1 <= s.length, t.length <= 5 * 104
        s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?  '''

'''
****Leet code solution 1 (sorting)***
def is_anagram(s,t):

    
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t
    
    '''





'''
         ****My solution****
    state = False
    s_sorted = "".join(sorted(s))
    t_sorted = "".join(sorted(t))
    if len(s) != len(t):
        return False
    else:
        for i in range(len(s)):
            if s_sorted[i]==t_sorted[i]:
                state = True
            else:
                state = False
        return state '''


# Using Hash map (Dictonary)
from collections import defaultdict

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        # Count the frequency of characters in string s
        for x in s:
            count[x] += 1
            print(count)

        # Decrement the frequency of characters in string t
        for x in t:
            count[x] -= 1
            print(count)

        # Check if any character has non-zero frequency
        for val in count.values():
            print(val)
            if val != 0:
                return False

        return True
answer = Solution()
print(answer.isAnagram("hamro","rhamo"))