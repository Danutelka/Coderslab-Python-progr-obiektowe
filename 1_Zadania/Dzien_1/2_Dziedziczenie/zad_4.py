class Employee:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def set_salary(self, salary):
        try:
            if salary > 0:
                self.set_salary = salary
        except Exception:
                self.salary = 0

class Salar(Employee):

    def compute_payment(self,):
        return self.salary * 190

he = HourlyEmployee(12, "imie", "nazwisko")
he.set_salary(20)
print(he.compute_payment(8))
