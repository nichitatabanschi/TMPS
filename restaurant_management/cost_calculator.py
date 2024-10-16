from abc import ABC, abstractmethod

# Abstract Class for Cost Calculation
class CostCalculator(ABC):
    @abstractmethod
    def calculate_total(self, order):
        pass

# Regular Cost Calculation
class RegularCostCalculator(CostCalculator):
    def calculate_total(self, order):
        total = 0
        for item in order.items:
            total += item[1] * item[2]  # quantity * price_per_item
        return total

# Discounted Cost Calculation
class DiscountedCostCalculator(CostCalculator):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def calculate_total(self, order):
        total = 0
        for item in order.items:
            total += item[1] * item[2]
        discount = total * self.discount_percentage / 100
        return total - discount
