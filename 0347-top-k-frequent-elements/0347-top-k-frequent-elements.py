"""
UMPIRE
U: 
    Input: int array "nums", int "k" 
    Output: return "k" most frequent elements in any order 

    condition: guaranteed that the answer is unique

M: dict to count frequency, bucket list where index is the count, each element is list of lists that have that frequency 
P:
    create dict 
    1. loop nums, populate dict where key = num, value = frequency 
    create bucket_list = [ [] nums.length]
    2. loop the dict, for all same val (same frequeny), populate buckelist[val] with the key
    create result = []
    3. iterate the bucket list backward, populate result list, decrement k, stops when k = 0
    4. return result
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1 
        
        bucket_list = [ [] for _ in range(len(nums) + 1)] #because freq goes up to index = len + 1

        for key,value in d.items():
            bucket_list[value].append(key)

        result = []

        for i in range(len(bucket_list) - 1 , -1, -1): #or use for lst in reversed(my_list)
            if k == 0: 
                return result
            
            current_list = bucket_list[i]

            for num in current_list: 
                result.append(num)
                k -= 1
        
        return result