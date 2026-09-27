class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []

        for i, ch in enumerate(s):

            if ch == '(':
                open_stack.append(i)

            elif ch == '*':
                star_stack.append(i)

            else:  # ')'
                if open_stack:
                    open_stack.pop()

                elif star_stack:
                    star_stack.pop()

                else:
                    return False

        # Match remaining '(' with '*' that occur after them
        while open_stack:

            if not star_stack:
                return False

            open_pos = open_stack.pop()
            star_pos = star_stack.pop()

            if star_pos < open_pos:
                return False

        return True