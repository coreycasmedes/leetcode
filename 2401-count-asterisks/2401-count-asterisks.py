class Solution:
    def countAsterisks(self, s: str) -> int:
        on = True
        asterik_count = 0
        for letter in s:
            if letter == '|':
                on = not on
            if letter == '*' and on:
                asterik_count += 1
        return asterik_count
        