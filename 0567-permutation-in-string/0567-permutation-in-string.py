"""
U: 
    input: 2 strings "s1" and "s2" 
    output: boolean 
M: 2 pointers and 2 dict ***make use of len(s1) a valid permutation must have exactly that len, if not, increment left 

P: 
    1. create 2 dict, org_dict key = char of s1, val = its count
        curr_dict
    2. left ptr, right ptr starts at 0 
    3. while right < len(s2) 
        right_char = s2[right]
        curr_d[right_char] = curr_d.get(right_char, 0) + 1 
        if (right - left + 1) > len(s1) *****
            left_char = s2[left]
            if left_char in d: #safe check
                d[left_char] -= 1 
            if d[left_char] == 0
                del d[left char]
            left += 1 
        if org_dict == curr_dict: 
            return True 
        right += 1
    return False 
"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        org_dict = {}
        curr_d = {}
        left, right = 0, 0

        for char in s1: 
            org_dict[char] = org_dict.get(char, 0) + 1 

        while right < len(s2):
            right_char = s2[right]
            curr_d[right_char] = curr_d.get(right_char, 0) + 1 

            if (right - left + 1) > len(s1): #valid window can't be longer than s1
                left_char = s2[left]
                if left_char in curr_d: 
                    curr_d[left_char] -= 1 
                    if curr_d[left_char] == 0:
                        del curr_d[left_char]
                left += 1 
                
            if curr_d == org_dict: 
                return True 
            right += 1
                
        return False
            

        