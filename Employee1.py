# Импортируем библиотеку, которая поможет нам посчитать кол-во рабочих дней в месяце
import datetime 


#Создаем родительский класс
class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
    
#Создаем метод, который покажет всю информацию про класс
    def info(self):
        return(f'Name:{self.name}; Position:{self.position}; Salary:{self.salary}')
        

#Создаем метод, который посчитает зарплату
    def calc_salary(self,year,month):
    # Определяем первый и последний день месяца
            first_day = datetime.date(year, month, 1)
            if month == 12:
                last_day = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
            else:
                last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    
    # Считаем количество рабочих дней
            worked_days = 0
            current_day = first_day
            while current_day <= last_day:
                if current_day.weekday() < 5:  # Понедельник (0) - Пятница (4)
                    worked_days += 1
                current_day += datetime.timedelta(days=1)
       
            return(self.position*self.salary*worked_days)

#Создаем дочерний класс
class Manager(Employee):
    def __init__(self,department,num_employees,name,position,salary):
        super().__init__(name,position,salary)
        self.department = department
        self.num_employees = num_employees
        

#Создаем метод, который покажет всю информацию про класс
    def info(self):
        return(f'Name:{self.name}; Position:{self.position}; Salary:{self.salary}; Department:{self.department}; Num employees:{self.num_employees} ')


#Создаем метод, который посчитает зарплату
    def calc_salary(self,year,month):
    # Определяем первый и последний день месяца
            first_day = datetime.date(year, month, 1)
            if month == 12:
                last_day = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
            else:
                last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    
    # Считаем количество рабочих дней
            worked_days = 0
            current_day = first_day
            while current_day <= last_day:
                if current_day.weekday() < 5:  # Понедельник (0) - Пятница (4)
                    worked_days += 1
                current_day += datetime.timedelta(days=1)
       
            
            return(self.position*self.salary*worked_days + self.position*self.salary*worked_days*(1/self.num_employees))

