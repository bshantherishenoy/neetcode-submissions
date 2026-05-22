class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        special_chars = "+-*/"
        stack = []
        for token in tokens:
            if token not in special_chars:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                print(f"{num1} {token} {num2}")
                if token == "+":
                    ans = num1 + num2
                elif token == "-":
                    ans = num1 - num2
                elif token == "/":
                    ans = int(num1 / num2)
                elif token == "*":
                    ans = num1 * num2
                stack.append(ans)
        
        return stack[-1]
