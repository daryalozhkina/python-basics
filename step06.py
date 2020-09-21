class_pupile = input('введите имена учеников через запятую')
# Полина, Антон, Арсений, Евгений, Алексей, Тимур
class_pupile = 'Полина, Антон, Арсений, Евгений, Алексей, Тимур'
correct_result = ['Полина', 'Антон', 'Арсений', 'Евгений', 'Алексей', 'Тимур']
#print('ученики класса:', class_pupile)

result = class_pupils.split(',')

assert result == correct_result, 'алгоритм реализован неверно'
#if not result == correct_result:
 #   ralse result == correct_result, 'алгоритм реализован неверно'
print(result)