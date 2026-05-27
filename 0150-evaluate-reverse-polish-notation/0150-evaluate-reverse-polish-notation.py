"""
U: 
    input: an array of strings "tokens" 
    output: return int (value of the expression)

    valid operations = + - * /
    no division by zero 
    no decimals (2.9 -> 2)


M: stack (store numbers)
P: 
    1. create a stack s 
    2. iterate tokens 
        3. if numbers, add to stack 
        4. else: pop=b, pop=a, do a operators b 
            add back to the stack 
    5. return pop

"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens: 
            if token.isdigit() or token.lstrip('-').isdigit(): # count -numbers as digit (strip - and is the remainder a digit?)
                stack.append(int(token))
            else: 
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(float(a) / b)) #truncate towards zero 

        return int(stack.pop())
        