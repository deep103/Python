'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
'''
class Solution():
    def fourSums(self,nums1,nums2,nums3,nums4):
        temp = {}
        ans = 0 
        for i in nums1:
            for j in nums2:
                s = i+j
                if s not in temp:
                    temp[s] = 0
                temp[s] += 1
        for i in nums3:
            for j in nums4:
                s = -(i + j)
                if s in temp:
                    ans += temp[s]
        return ans
nums1 = [1,2] 
nums2 = [-2,-1] 
nums3 = [-1,2] 
nums4 = [0,2]
# nums1 = [0] 
# nums2 = [0] 
# nums3 = [0] 
# nums4 = [0]
obj = Solution()
print(obj.fourSums(nums1,nums2,nums3,nums4))

