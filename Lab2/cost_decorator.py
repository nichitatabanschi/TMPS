from cost_calculator import RegularCostCalculator

class OrderCostDecorator:
    def __init__(self, calculator):
        self.calculator = calculator

    def calculate_total(self, order):
        return self.calculator.calculate_total(order)

class TaxDecorator(OrderCostDecorator):
    def __init__(self, calculator, tax_rate):
        super().__init__(calculator)
        self.tax_rate = tax_rate

    def calculate_total(self, order):
        total = super().calculate_total(order)
        tax = total * self.tax_rate / 100
        return total + tax

class ServiceChargeDecorator(OrderCostDecorator):
    def __init__(self, calculator, service_charge):
        super().__init__(calculator)
        self.service_charge = service_charge

    def calculate_total(self, order):
        total = super().calculate_total(order)
        return total + self.service_charge
