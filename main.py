from Employee1 import Employee
from Employee1 import Manager 


name1 = input('Wtite name:')
pos = float(input('Write position:'))
sal = float(input('Write salary:'))
days = int(input('Write working days amount:'))
Emp =Employee(name1,pos,sal)

print(f'Employee info:',Emp.info())
print(f'Slary:',Emp.calc_salary(days))

department = input('Write departmant:')
num = int(input('Write number of employees:'))
name2 = input('Write name:')
pos1 = float(input('Write position:'))
sal1 = float(input('Write salary:'))
man = Manager(department,num,name2,pos1,sal1,days)

print(f'Manager info:',man.info())
print(f'Slary:',man.calc_salary())
