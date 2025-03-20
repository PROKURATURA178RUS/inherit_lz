class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
    

    def info():
        return(print(f'Name:{self.name}; Position:{self.position}; Salary:{self.salary}'))


    def calc_salary(self,worked_days):
        month = input('Write month')
        if month == 'January':
            worked_days = 20
        elif month =='February':
            worked_days = 20
        elif month == 'March':
            worked_days = 21
        elif month == 'April':
            worked_days = 21
        elif month == 'May':
            worked_days = 20
        elif month == 'June':
            worked_days = 21
            
        return(print(position*salary*worked_days))


class Manager(Employee):
    def __init__(self,department,num_employees):
        super().__init__(name,position,salary)
        self.department = department
        self.num_employees = num_employees

    
    def info():
        return(print(f'Name:{self.name}; Position:{self.position}; Salary:{self.salary}; Department:{self.department}; Num employees{self.num_employees} '))

    def calc_salary():
        return(print(position*salary*worked_days + position*salary*worked_days*(1/num_employees)))

