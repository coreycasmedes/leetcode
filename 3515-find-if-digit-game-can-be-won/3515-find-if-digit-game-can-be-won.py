class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(map(lambda n: n if n < 10 else -n, nums)) != 0