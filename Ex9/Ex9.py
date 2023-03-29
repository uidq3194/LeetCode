'''
Link : https://leetcode.com/problems/palindrome-number/

Difficulty : Easy

Title : 9. Palindrome Number

Description:
    Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False 
        copyx = x
        ogl = 0
        while x>0:
            ogl = ogl * 10 + x % 10
            x = x // 10
        return ogl == copyx

        
problem = Solution()
print(problem.isPalindrome(121))
print(problem.isPalindrome(-121))
print(problem.isPalindrome(10))
print(problem.isPalindrome(0))
print(problem.isPalindrome(1))