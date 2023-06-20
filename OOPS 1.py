class employee:
    increment=1.5
    def __init__(self,fname, lname, salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    def increase(self):
        self.salary=employee.increment*self.salary
    def change_increment(cls,amount):
        cls.increment=amount
Atishay=employee("Atishay", "Jain", 145000)
#print(Atishay.salary)
Atishay.increase()
print("New salary is", Atishay.salary)

