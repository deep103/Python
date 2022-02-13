'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character 
while preserving the order of characters. No two characters may map to the same character, 
but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''

class Solution():
    def isoStrings(self,s,t):
        store = {}
        if len(t) != len(s) or len(set(s)) != len(set(t)):
            print(False)
        elif len(t) == len(s) or len(set(s)) == len(set(t)):
            for char in range(len(t)):
                if t[char] not in store:
                    store[t[char]] = s[char]
                elif store[t[char]] != s[char]:
                    print(False)
            print(True)
s = "egg"
t = "add"
ob1 = Solution()
ob1.isoStrings(s,t)