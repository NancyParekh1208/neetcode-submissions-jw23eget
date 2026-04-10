class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []
        for op in operations:
            if op == '+':
                if stack and stack[-1] and stack[-2]:
                    newScore = stack[-1] + stack[-2]
                    stack.append(newScore)
            elif stack and op == 'C':
                stack.pop()
            elif stack and op == 'D':
                prevScore = stack[-1]
                stack.append(prevScore*2)
            else:
                stack.append(int(op))

        total = 0
        while stack:
            total += stack.pop()

        return total     
        