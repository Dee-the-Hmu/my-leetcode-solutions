"""
U:
    input: a string "s" 
    output: boolean 

    a palindrome = a string that reads the same forward and backward
    note: case-insensitive, ignores all NON-alphanumeric characters 

Match: 2 pointers 
Plan: 
    edge case: if s.length = 1, return True

    1. left = 0, right = len(s) - 1
    2. while (left < right)
        3. if !s[left].isalnum()
                left += 1 
                continue
            if !s[right].isalnum()
                right -= 1
                continue 
            if s[left] != s[right]
                return False
            left += 1 # update
            right -= 1
    4. return True
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1: 
            return True
        
        left = 0
        right = len(s) - 1 

        while (left < right): 
            if not s[left].isalnum():
                left += 1 
                continue
            if not s[right].isalnum():
                right -= 1
                continue 
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
