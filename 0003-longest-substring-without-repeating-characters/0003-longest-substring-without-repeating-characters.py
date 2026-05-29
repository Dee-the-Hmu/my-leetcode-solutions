"""
U: 
    input: a string "s" 
    output: int (the len of the longest substring without duplicate characters)

M: subtracting the repeating char from the set ****
P: 
    1. if s.len == 0: return 0, if 1, return 1
    2. create a set, longest_len = 0, left_ptr = 0 
    3. iterate s, for each char 
        4. if curr_char not in s: 
            5. add curr_char to the set 
            6. if len(set) > longest_len, update longest len
        7. else: 
            while curr_char in s: 
                set.remove(s[left_ptr])
                left_ptr += 1 
    8. return longest_len

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: 
            return 0
        if len(s) == 1: 
            return 1 

        s_et = set()
        longest_substring_len = 0
        left_ptr = 0

        for curr_char in s: 
            if curr_char not in s_et:
                s_et.add(curr_char)
            else: # char in s 
                while curr_char in s_et:
                    s_et.remove(s[left_ptr])
                    left_ptr += 1
                s_et.add(curr_char)
                
            if len(s_et) > longest_substring_len: 
                    longest_substring_len = len(s_et)

        return longest_substring_len