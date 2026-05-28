"""
U
    input: an array of integers "temperatures" 
        temperatures[i] = temp of the ith day
    output: return an array "answer" 

    answer[i] = # of days AFTER ith day to get a warmer temperature 

    if no future warmer day, answer[i] = 0

M: stack with index in the stack
Plan: 
    1. create a stack
    2. create a list answers[] same length as temperatures, every index with value 0
    3. iterate temperatures (temp, index)
        for each temp, 
        if the stack is empty, append/add the index to the stack 
        else: 
            if the top is > the current_temp: 
                add the index to the stack 
                continue
            while the top is < the current_temp: 
                pop from the stack 
                curr_index - popped val 
                store that in answers[popped]

            add index to the stack 

    4. return answers
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        answers = [0] * len(temperatures)

        for i,temp in enumerate(temperatures):
            if not stack or temperatures[stack[len(stack) - 1]] >= temp:
                stack.append(i)
                continue
            
            while stack and temperatures[stack[len(stack)-1]] < temp: 
                prev_index = stack.pop()
                days = i - prev_index 
                answers[prev_index] = days 

            stack.append(i)
        return answers


            
        