class Solution:
    def hammingWeight(self, n: int) -> int:
        hamming_weight = 0
        for exp in range(31, -1, -1):

            if n >= 2**exp:
                hamming_weight += 1
                n -= 2**exp
        return hamming_weight
        