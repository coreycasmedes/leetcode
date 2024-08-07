class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_waters=numBottles
        n = numBottles
        while n >= numExchange:
            exchange_returns = n // numExchange
            max_waters += exchange_returns
            n = exchange_returns + (n % numExchange)
        return max_waters
            



        