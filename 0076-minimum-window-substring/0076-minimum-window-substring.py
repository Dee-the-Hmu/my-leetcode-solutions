"""
U: 
    input: 2 strings "s" and "t"
    output: string "minimum window substring" of s, return "" if no such string 
        substring = continuous "sliding window" 

M: sliding window
P: 
    1. a dict d where key = char of t, val = its count 
        curr_d = {}
    # num-required-chars = no of items in d 
    have = 0
    2. left, right = 0, 0 
    3. best_substring = ""
    4. count = len(s) + 1
    5. while right < len(s)
        6. right_char = s[right]
        7. curr_d[right_char] = curr_d.get(right_char, 0) + 1 
        8. if right_char in d and curr_d[right_char] == d[right_char]
            9: have += 1
        10. if have == num-required-chars: #curr_d has everything that is in d
            11. curr_substring = s[left:right]
            12. if count > len(curr_substring):
                    count = len(curr_substring)
                    best_substring = curr_substring
            13. remove left (update left) 
            if s[left] in d:
                have -= 1 
            left += 1 
            and curr_d[s[left]] -= 1 , if curr_d[s[left]] == 0, del curr_d[s[left]]

            left_char = s[left]

            14. while (left < right and left_char not in d): 
                if s[left] in d:
                    have -= 1 
                and curr_d[s[left]] -= 1 , if curr_d[s[left]] == 0, del curr_d[s[left]]
                left += 1 
            maybe repeat 10 here? 
        15. right += 1 

        16. return best_substring  
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d, curr_d = {}, {}
        left,right = 0, 0
        have = 0

        best_substring = ""
        best_substring_len = len(s) + 1 

        for char in t: 
            d[char] = d.get(char, 0) + 1 

        num_required_chars = len(d)

        while right < len(s): 
            right_char = s[right]
            curr_d[right_char] = curr_d.get(right_char, 0) + 1 

            if right_char in d and curr_d[right_char] == d[right_char]:
                have += 1 
            
            while have == num_required_chars: 
                curr_substring_len = right - left + 1 
                if curr_substring_len < best_substring_len: 
                    best_substring_len = curr_substring_len 
                    best_substring = s[left:right+1]
                # will remove the leftmost char
                left_char = s[left]
                curr_d[left_char] -= 1 

                if left_char in d and curr_d[left_char] < d[left_char]: 
                    have -= 1 
                
                if curr_d[left_char] == 0:
                    del curr_d[left_char]
                
                left += 1 
                    
            right += 1
        return best_substring

            



        