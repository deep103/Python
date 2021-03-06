'''
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. 
If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

 

Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 
Example 2:

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
'''

# class Solution():
#     def fkthDistinct(self,arr,k):
#         temp = []
#         for i in range(len(arr)):
#             if arr[i] not in temp:
#                 temp.append(arr[i])
#             elif arr[i] in temp:
#                 temp.remove(arr[i])
#         if len(temp)>=k:
#             return temp[k-1]
#         else:
#             return ""
# arr = ["a","b","a"] 
# k = 3
# # arr = ["d","b","c","b","c","a"] 
# # k = 2
# # arr = ["aaa","aa","a"] 
# # k = 1
# obj = Solution()
# print(obj.fkthDistinct(arr,k))

from collections import defaultdict
class Solution():
    def fkthDistinct(self,arr,k):
        n = len(arr)
        dd = defaultdict(int)
        for c in arr:
            dd[c] += 1
        
        distinct = []
        for i in range(n):
            if dd[arr[i]] == 1:
                distinct.append(arr[i])
                
        if len(distinct) < k:
            return ""
        else:
            return distinct[k-1]
arr = ["aaa","aa","a"] 
k = 1
obj = Solution()
print(obj.fkthDistinct(arr,k))