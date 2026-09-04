class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        prices.sort()

        return money if money < sum(prices[:2]) else money - sum(prices[:2])