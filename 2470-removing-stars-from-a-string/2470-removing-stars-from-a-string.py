class Solution:
    def removeStars(self, s: str) -> str:

        stack = []
        for letter in s:
            if letter == '*':
                if len(stack) >= 0:
                    del stack[-1]
            else:
                stack.append(letter)
        result = []
        # for letter in stack:
        #     result.insert(0, letter)
        # print(result)
        return "".join(stack)


        