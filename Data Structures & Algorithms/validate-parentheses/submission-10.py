class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[" or not len(stack):
                stack.append(i)
            else:
                print(stack)
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(i)
        
        if not len(stack):
            print(len(stack))
            return True
        else:
            return False

        