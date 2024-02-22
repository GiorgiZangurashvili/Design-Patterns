import unittest

from pos.app.calculator.revenue_calculator import RevenueCalculator


class TestRevenueCalculator(unittest.TestCase):
    def test_calculate(self) -> None:
        product_price = 100.0
        discount = 18
        result = RevenueCalculator.calculate(product_price, discount)
        expected_result = 82.0
        self.assertAlmostEqual(result, expected_result, delta=0.001)

    def test_calculate_with_zero_discount(self) -> None:
        product_price = 100.0
        discount = 0
        result = RevenueCalculator.calculate(product_price, discount)
        expected_result = 100.0
        self.assertAlmostEqual(result, expected_result, delta=0.001)

    def test_calculate_with_big_discount(self) -> None:
        product_price = 100.0
        discount = 150
        result = RevenueCalculator.calculate(product_price, discount)
        expected_result = 0
        self.assertAlmostEqual(result, expected_result, delta=0.001)


if __name__ == "__main__":
    unittest.main()
