class RevenueCalculator:
    @staticmethod
    def calculate(product_price: float, discount: int) -> float:
        discounted_price: float = float(product_price * (1 - discount / 100.0))
        return max(discounted_price, 0.0)
