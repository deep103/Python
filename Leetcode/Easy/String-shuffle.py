'''
You are given a string s and an integer array indices of the same length. 
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.
'''

class Solution():
    def stringShuffle(self,s,indices):
        temp = {}
        final = []
        for i in range(len(s)):
            if s[i] not in temp or i < len(s):
                temp[indices[i]] = s[i] 
        temp = sorted(temp.items())
        temp = dict(temp)
        for i in temp:
            if temp[i] not in final or 1==1:
                final.append(temp[i])
        final = tuple(final)
        final = "".join(final)
        return final
# s = "codeleet" 
# indices = [4,5,6,7,0,2,1,3]
s = "abc" 
indices = [0,1,2]
obj = Solution()
print(obj.stringShuffle(s,indices))
