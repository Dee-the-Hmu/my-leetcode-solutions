class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        lst = []
        cur_sum = 0
        cur_index = 0

        def backtrack(lst : List[int], cur_sum : int, cur_index : int): 
            #base case 
            if cur_sum == target:
                result.append(lst.copy())
                return

            if cur_sum > target: 
                return

            #choice (I can take every elements ONLY starting from the Current Element)
            for i in range(cur_index, len(nums)):
                num = nums[i]
                #condition (when to choose)
                #don't need this check if (cur_sum + num <= target):
                #instead just add and let the base case handle return and then pop or 
                #use the below condition (don't even enter into the recursive call and then pop  if the sum + num is > target)
                if cur_sum + num > target:
                    continue
                lst.append(num)
                cur_sum += num
                
                #explore
                backtrack(lst, cur_sum, i)

                #undo
                popped = lst.pop()
                cur_sum -= popped

        backtrack(lst, cur_sum, cur_index)
        return result