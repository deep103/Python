'''
Given a string array words, return an array of all characters 
that show up in all strings within the words (including duplicates). 
You may return the answer in any order.
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
'''
from collections import Counter

class Solution():
    def commonCharacters(self,words):
        result = Counter(words[0])
        for word in words:
            result &= Counter(word)
            print(result)
        print(list(result.elements()))
words = ["bella","label","roller"]
# words = ['cool','lock','cook']
obj = Solution()
obj.commonCharacters(words)
