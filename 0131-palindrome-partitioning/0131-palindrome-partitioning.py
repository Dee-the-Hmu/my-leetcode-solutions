class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        lst = []
        start_index = 0

        def is_palindrome(s : str) -> bool:
            left = 0
            right = len(s) - 1

            while (left < right):
                if (s[left] != s[right]):
                    return False
                
                left += 1
                right -= 1
                
            return True

        def backtrack(lst, start_index):
            #base case
            if start_index == len(s):
                result.append(lst.copy())
                return

            #condition
            for i in range(start_index, len(s)):

                #find out possible substrings 
                substring = s[start_index:i+1]

                # if is_palidrome -> 
                    #explore    
                    #undo


                if(is_palindrome(substring)):
                    lst.append(substring)
                    backtrack(lst, i+1)

                    lst.pop()

        

        backtrack(lst, start_index)
        return result
        