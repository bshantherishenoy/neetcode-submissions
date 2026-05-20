class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        special_chars = ['+' , 'D' , 'C']
        for i in operations:
            if i in special_chars:
                if i == "+" :
                    num1 = stack[-1]
                    num2 = stack[-2]
                    stack.append(num1+num2)
                elif i == "D":
                    num1 = stack[-1]
                    stack.append(num1*2)
                elif i == "C":
                    stack.pop()
                else:
                    print(f"Invalid operation:{i}\n Length of stack:{len(stack)}")
            else :
                stack.append(int(i))
        return sum(stack)