class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        special_chars = ['+' , 'D' , 'C']
        for i in operations:
            if i in special_chars:
                if i == "+" and len(stack) >= 2:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.extend([num2,num1,num1+num2])
                    print(stack)
                elif i == "D" and len(stack)>=1:
                    num1 = stack[-1]
                    stack.append(num1*2)
                    print(stack)
                elif i == "C" and len(stack):
                    stack.pop()
                    print(stack)
                else:
                    print(f"Invalid operation:{i}\n Length of stack:{len(stack)}")
            else :
                stack.append(int(i))
        return sum(stack)