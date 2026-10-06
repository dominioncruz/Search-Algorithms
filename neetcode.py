import operator
import math


class Solution:
    def evalRPN(self, tokens):
        operators = {
            "+": operator.add, 
            "-": operator.sub, 
            "*": operator.mul, 
            "/": lambda a, b: int(a / b)
        }
        operands = []

        for char in tokens:
            if char in operators:
                elem1 = operands[-2]
                elem2 = operands[-1]
                operands.pop()
                operands.pop()
                operands.append(operators[char](elem1,elem2))
            else:
                operands.append(int(char))
        

minStack = Solution();
minStack.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])