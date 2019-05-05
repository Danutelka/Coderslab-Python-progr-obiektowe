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

c1 = Calculator()

c1.add(2, 2)
c1.multiply(2, 3)

c2 = Calculator()

c2.multiply(1, 3)
c2.add(2, 5)
c2.multiply(6, 3)

c1.print_operations()

print("c1")
c1.print_operations()

print("c2")
c2.print_operations()