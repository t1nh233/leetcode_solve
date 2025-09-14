class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for sym in s:
            if sym == '(' or sym == '{' or sym == '[':
                stack.append(sym)
            elif sym == ')' or sym == '}' or sym == ']':
                if len(stack) == 0:
                    return False
                else:
                    pop = stack.pop()
                    if not (sym == ')' and pop == '(' or sym == '}' and pop == '{' or sym == ']' and pop == '['):
                        return False
        return len(stack) == 0
