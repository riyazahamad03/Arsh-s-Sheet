class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for _ in range(n)]
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices

        return prices[dst] if prices[dst] != float("inf") else -1


x = Solution()
print(x.findCheapestPrice(n=4, flights=[[0, 1, 100], [1, 2, 100], [
      2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0, dst=3, k=1))
