"""
understand
    INPUT: string s
    output: longest substring w/o repeating character

    edge case:
        if empty, 0
        if len==1, 1

match: sliding window and a set 
plan:
    handle edge cases
        max = 1
    1. s_et = set()
    2. s_et.add(s[0])
    3. l = 0
    4. iterate the string 
        5. curr_char
        6. while s_et and curr_char in s_et:
            if len(s_et) > max
                max = len(s_et)
            s_et.remove(s[l])
            l += 1

        7. s_et.add(curr_char)
    8. return max

implement, review
evaluate: O(n) time, O(n) space
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
       

        if not s:
            return 0
        if len(s) == 1:
            return 1

        s_et = set()
        s_et.add(s[0])
        max_len = 1
        l = 0
 
        for i in range(1, len(s)):
            curr_char = s[i]
            while s_et and curr_char in s_et:
                if len(s_et) > max_len:
                    max_len = len(s_et)
                s_et.remove(s[l])
                l += 1

            s_et.add(curr_char)
        
        return max(max_len, len(s_et))
        