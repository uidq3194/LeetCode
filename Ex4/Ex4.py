'''
Link : https://leetcode.com/problems/median-of-two-sorted-arrays/

Difficulty : Hard

Title : 4. Median of Two Sorted Arrays

Description : 
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).
    
Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
'''

class Solution(object):
    def mergeArray(self, num1, size1, num2, size2):
        i = 0
        j = 0
        mergedArray = []
        while i < size1 and j< size2:
            if num1[i]<num2[j]:
                mergedArray.append(num1[i])
                i+=1
            elif num1[i]>num2[j]:
                mergedArray.append(num2[j])
                j+=1
            else:
                mergedArray.append(num1[i])
                mergedArray.append(num2[j])
                i+=1
                j+=1
        
        while i < size1:
            mergedArray.append(num1[i])
            i+=1
        while j < size2:
            mergedArray.append(num2[j])
            j+=1

        return mergedArray

    def computeMedian(self, nums, arrSize):
        if (arrSize % 2) == 1:
            return nums[arrSize/2]
        else:
                return (nums[(arrSize//2)-1] + nums[(arrSize//2)])/ 2.0

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mergedArray = []
        size1 = len(nums1)
        size2 = len(nums2)

        if size1 != 0 and size2 != 0:
            mergedArray = self.mergeArray(nums1, size1, nums2, size2)
            return self.computeMedian(mergedArray,size1+size2)           
        elif size1 != 0 and size2 == 0:
            return self.computeMedian(nums1, size1)
        elif size1 == 0 and size2 != 0:
            return self.computeMedian(nums2, size2)
        else:
            return 0


problem = Solution()
print(problem.findMedianSortedArrays([1,2],[3,4]))
