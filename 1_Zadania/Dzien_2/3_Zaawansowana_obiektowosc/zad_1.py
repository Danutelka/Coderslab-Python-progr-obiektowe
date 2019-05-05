class Calculator:

    def __init__(self):
        self.operations =[]

    def add(self, a, b):
        operation = "added {} to {} got {}" .format(a, b, a + b)
        self.operations.append(operation)
        return a + b

    def multiply(self, a, b):
        operation = "multiplied {} with {} got {}" .format(a, b, a * b)
        self.operations.append(operation)
        return a * b

    def print_operations(self):
        for operation in self.operations:
            print(operation)

class AdvancedCalculator(Calculator):

    PI = 3.14159265

    @staticmethod
    def compute_circle_radius(r):
        return AdvancedCalculator.PI * (r ** 2)

    # lista nie jest zmienną statyczną, nie wiadomo do którego obiektu dopisać
    # funkcja nie wie do jakiego obiektu dopisac operacje


print(AdvancedCalculator.PI)
print(AdvancedCalculator.compute_circle_radius(5))