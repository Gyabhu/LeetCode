"""
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using
    the letters from magazine and false otherwise.
    Each letter in magazine can only be used once in ransomNote.

"""
class Solution:
    def canConstruct(ransomNote, magazine):
        sort_note = "".join((sorted(ransomNote)))
        sort_magazine = (sorted(magazine))
        print(sort_note, type(sort_note))
        print(sort_magazine, type(sort_note))
        return sort_note in sort_magazine

    print(canConstruct("bg", "rtyhbnfghjrtyghbnjdfgvbuikjfgh"))
