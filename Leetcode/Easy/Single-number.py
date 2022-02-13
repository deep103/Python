'''
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
'''
def single_num(nums):
    ans = []
    repeat = []
    for num in nums:
        for i in range(len(nums)):
            if num not in ans:
                ans.append(num)
                break
            if num in ans:
                repeat.append(num)
                ans.remove(num)
                break
    for i in repeat:
        for j in ans :
            if i == j:
                ans.remove(j)
    for i in ans:
        string = str(i)
    string = int(string)
    print(string)
nums = [4,1,2,1,2]
single_num(nums)