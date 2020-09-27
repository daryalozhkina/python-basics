#class_pupile = input('введите имена учеников через запятую')
# Полина, Антон, Арсений, Евгений, Алексей, Тимур
class_pupils = 'Полина, Антон, Арсений, Евгений, Алексей, Тимур'
correct_result = ['Полина', 'Антон', 'Арсений', 'Евгений', 'Алексей', 'Тимур']
#print('ученики класса:', class_pupile)

#_result = class_pupils.split(', ')
#result = []
#for item in _result:
    #print(item, '->', item.strip())
#    result.append(item.strip())

#result = list(map(str.strip, class_pupils.split(',')))
result = [item.strip() for item in class_pupils.split(',')]

print(result)
assert result == correct_result, 'алгоритм реализован неверно'
#if not result == correct_result:
 #   ralse result == correct_result, 'алгоритм реализован неверно'
#print(result)