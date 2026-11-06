class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        lst = []
        cur_sum = 0
        start_index = 0 

        candidates.sort()

        def backtrack(lst, cur_sum, start_index):
            #base case 
            if cur_sum > target:
                return  
            if cur_sum == target:
                result.append(lst.copy())

            #chocie (can take every element from the next available index)
            for i in range(start_index, len(candidates)):

                if (candidates[i] + cur_sum) > target:
                    continue

                if (i > start_index and candidates[i] == candidates[i-1]):
                    continue

                #choose
                lst.append(candidates[i])
                cur_sum += candidates[i]

                #explore
                backtrack(lst, cur_sum, i + 1)

                #undo
                cur_sum -= lst.pop()

        backtrack(lst, cur_sum, start_index)
        return result


            
        