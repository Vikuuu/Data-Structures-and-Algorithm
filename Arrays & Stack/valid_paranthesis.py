class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap_for_parentheses = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in hashmap_for_parentheses:
                if stack and stack[-1] == hashmap_for_parentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
