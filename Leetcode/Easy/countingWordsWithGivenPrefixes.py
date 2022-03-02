'''
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
'''

class Solution():
    def prefixCount(self, words, pref):
        c = j = 0
        for word in words:
            if pref in word[j:len(pref)]:
                c+=1
            else:
                continue
        return c
words = ["pay","attention","practice","attend"]
pref = "at"
obj = Solution()
print(obj.prefixCount(words, pref))
