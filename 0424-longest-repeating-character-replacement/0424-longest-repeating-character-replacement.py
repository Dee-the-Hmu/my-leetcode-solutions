"""
U: 
    input: a string "s" , an int "k" 
    output: the len of the longest substring containing the same letter you can get after performing the above operation 

    k = # of replacing/operation we can do to get the longest repeating char substring 

    ***window length - count of most frequent char in window <= k***
M: dict, key = char, value = its count
P: 
    1. create a dict, a variable "longest-repeating-count", a variable "max-freq" 
    2. create left ptr, right ptr 
    3. while right ptr < len: 
        4. add s[right] to the dict -- d[s[right]] = d.get(s[right], 0) + 1 

        //how do i update max-freq? 
        looping thru dict will make this n^2 to find the max val 
        4.1. max_freq = max(max_freq, d[s[right]])

        5. if window_length - max_freq <= k: (valid) #window_length = (right_ptr - left_ptr + 1)
                6. if window_length > longest-repeating-count, update longest-repeating count 
            right += 1 

        7.else: (not valid)
            8. while(left < right and all the vallues in Dict - max_freq > k)
                left_char = s[left]
                d[left_char] in dict: 
                    d[left_char] -= 1
                    if d[left_char] <= 0: 
                        del d[left_char]
                left += 1
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = {}
        left = 0
        right = 0
        
        max_repeating_freq = 0
        longest_repeating_char_replacement = 0

        while (right < len(s)):
            right_char = s[right]
            d[right_char] = d.get(right_char, 0) + 1

            max_repeating_freq = max (max_repeating_freq, d[right_char])

            if (right - left + 1) - max_repeating_freq <= k: #valid window
                longest_repeating_char_replacement = max (longest_repeating_char_replacement, (right-left+1))
            
            else: #not valid window
                while (left < right and (right-left+1) - max_repeating_freq > k):
                    left_char = s[left]
                    if left_char in d: #safe guard
                            d[left_char] -= 1
                            if d[left_char] <= 0:
                                del d[left_char]
                    left += 1 
            right += 1
            
        return longest_repeating_char_replacement