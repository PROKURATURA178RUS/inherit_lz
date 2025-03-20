#Импортируем классы из файла
from Employee1 import Employee
from Employee1 import Manager 

#Команды, дающие возможность пользователю самостоятельно ввести данные
name1 = input('Wtite name:')
pos = float(input('Write position:'))
sal = float(input('Write salary:'))
date = int(input('Write year:'))
date1 = int(input('Write month:'))
Emp =Employee(name1,pos,sal)

#Вывод значений
print(f'Employee info:',Emp.info())
print(f'Slary:',Emp.calc_salary(date,date1))

#Команды, дающие возможность пользователю самостоятельно ввести данные
department = input('Write departmant:')
num = int(input('Write number of employees:'))
name2 = input('Write name:')
pos1 = float(input('Write position:'))
sal1 = float(input('Write salary:'))
man = Manager(department,num,name2,pos1,sal1)

#Вывод значений
print(f'Manager info:',man.info())
print(f'Slary:',man.calc_salary(date,date1))
