"""
U
    input: a string "s" containing () {} []
    output: boolean 

M: stack to store open brackets 
P: 
    1. create a stack
    2. iterate s 
        3. if open bracket: add to stack 
        4. if close bracket:
            5. if stack is empty -> F
            6. if stack.pop() is not the correct opening bracket -> F
    7. retrun true if stack is empty 
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opening_set = {'(', '[' , '{'}

        for char in s: 
            if char in opening_set: 
                stack.append(char)
            else: 
                if not stack: 
                    return False
                opening_char = stack.pop()
                if (char == '}' and opening_char != '{') or (char == ']' and opening_char != '[') or (char == ')' and opening_char != '('):
                    return False

        return not stack
            
        