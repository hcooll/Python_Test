from object.Employee import Employee

emp1 = Employee("Jack", "12222")
emp2 = Employee("Rose", "23432423")

print(emp1.displayCount())
print(emp1.displayEmployee())

# 动态添加属性
emp1.age = 25

print('getattr: ', getattr(emp1, 'age'))

# 动态删除属性
delattr(emp1, 'age')

print('hasattr: ', hasattr(emp1, 'age'))

# 默认属性
print(emp1.__class__)
print(emp1.__dict__)
print(emp1.__doc__)
print(emp1.__module__)


