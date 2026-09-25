# Create a class ‘Employeeʼ and add salary and increment properties to it. Write a method
# ‘salaryAfterIncrementʼ method with a @property decorator with a setter which changes
# the value of increment based on the salary

class Employee:
    salary = 350
    increment = 20

    @property
    def salaryAfterIncremnet(self):
        return self.salary + self.salary * (self.increment/100)

    @salaryAfterIncremnet.setter
    def salaryAfterIncremnet(self,salary):
        self.increment = ((salary/self.salary)-1)*100

e = Employee()
print(f"Salary After increment :{e.salaryAfterIncremnet}")
e.salaryAfterIncremnet = 420
print(f"Incerment : {e.increment}")