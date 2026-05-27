"""
U: 
    input: unsorted array of int "nums"
    output: int -> the len of the longest consecutive elements sequence 

    edge case: if len(nums) == 0, return 0

    constraint: O(n) runtime 

Match: set for O(1) look up and for each num, if num-1 not in the set, it is the start of a sequence
Plan: 
    edge case 
    1. create a set and populate by iterating nums 
    1.2. longest_consecutive_len = 1, curr_seq_len = 1
    2. iterate nums 
        3. if num-1 is not in the set #start of the seq 
        4. start = num 
        while (start+1 in set)
            
            start = start +1 
            curr_seq_len += 1 

            if curr_seq_len > longest_con_len: 
                update longest_con_len 

        curr_seq_len = 1

    return longest_con_len        
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0 

        s = set()
        for num in nums: 
            s.add(num)
        
        longest_con_len = 1
        curr_seq_len = 1 

        for num in s: 
            if (num - 1) not in s: #start of the sequence 
                start = num 
                while (start + 1) in s: 

                    start = start + 1
                    curr_seq_len += 1

                    if curr_seq_len > longest_con_len: 
                        longest_con_len = curr_seq_len
                
                curr_seq_len = 1

        return longest_con_len
        


            

        