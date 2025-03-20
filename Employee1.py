class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
    

    def info(self):
        return(f'Name:{self.name}; Position:{self.position}; Salary:{self.salary}')


    def calc_salary(self,worked_days):           
        return(self.position*self.salary*worked_days)


class Manager(Employee):
    def __init__(self,department,num_employees,name,position,salary,worked_days):
        super().__init__(name,position,salary)
        self.department = department
        self.num_employees = num_employees
        self.worked_days = worked_days

    
    def info(self):
        return(f'Name:{self.name}; Position:{self.position}; Salary:{self.salary}; Department:{self.department}; Num employees{self.num_employees} ')

    def calc_salary(self):
        return(self.position*self.salary*self.worked_days + self.position*self.salary*self.worked_days*(1/self.num_employees))

