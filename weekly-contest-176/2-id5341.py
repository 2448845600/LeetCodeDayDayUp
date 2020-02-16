class ProductOfNumbers:

    def __init__(self):
        self.numbers = []
        self.products = []

    def add(self, num: int) -> None:
        self.numbers.append(num)
        if num == 0:
            self.products = []
        else:
            if len(self.products) == 0:
                self.products.append(num)
            else:
                self.products.append(num * self.products[-1])

    def getProduct(self, k: int) -> int:
        if len(self.products) < k:
            return 0
        elif len(self.products) == k:
            return self.products[-1]
        else:
            return int(self.products[-1] / self.products[-k - 1])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)