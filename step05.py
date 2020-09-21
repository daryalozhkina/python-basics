a = 'всем привет'
print(type(a))
print(dir(a))

print(a.isdigit())

b = '15.7'
print(b.isdigit())

c = '157'
print(c.isdigit())

e = '15e7'
print(e.isdigit())

avg_mark = input('введите средний балл студента: ')

try:
    avg_mark = float (avg_mark)
    print ('ввод корректен', type(avg_mark), avg_mark)
except ValueError:
    print('некорректное значение', avg_mark)