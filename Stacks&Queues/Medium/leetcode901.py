class StockSpanner:
    def __init__(self) -> None:
        self.stack = []

    def next(self, price: int):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack[-1][1]
            self.stack.pop()
        return res


stockSpanner = StockSpanner()
stockSpanner.next(100)
stockSpanner.next(80)
stockSpanner.next(60)
stockSpanner.next(70)
stockSpanner.next(60)
stockSpanner.next(75)
stockSpanner.next(85)
