'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

def majorityElement(arr, N):
   mp = {}
   for i in range(0, N):
      if arr[i] in mp.keys():
         mp[arr[i]] += 1
      else:
         mp[arr[i]] = 1
   for key in mp:
      if mp[key] > (N / 2):
         return key
   return -1
N = 6
arr = [2,1,1,2,2,2]
ans = majorityElement(arr, N)
if ans != -1:
   print("Majority Element is:",ans)
else:
   print("No majority element in array")