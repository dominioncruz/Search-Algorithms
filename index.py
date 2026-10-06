#from collections import stack


class MatchingBraces:
    keyValue = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    def __init__(self, input):
        self.input = input

    def __str__(self):
        return self.input
    
    def check(self):
        stack = []
        
        for i in range(len(self.input)):
            print(stack)
            if i == 0:
                stack.append(self.input[i])
            else:
                if self.input[i] in self.keyValue.keys():
                    if len(stack) != 0 and stack[-1] == self.keyValue[self.input[i]]:
                        stack.pop()
                    else:
                        stack.append(self.input[i])
                else:
                    stack.append(self.input[i])
        if(len(stack) == 0):
            return "Valid"
        else:
            return "Not valid"
    
myMatchingBraces = MatchingBraces("[}{]()")

print(myMatchingBraces.check())





