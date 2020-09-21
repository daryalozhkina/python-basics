lesson_dates = ['19.05.15', '19.05.18', '19.05.19', '19.05.22']
lesson_dates_2 = ['19.05.15', '19.05.18', '19.05.19', '19.05.22']
student_marks = [
    5,
    4,
    3,
    2,
    5
]
student_2_marks = [
    4,
    3,
    5,
    5,
    4
]

for lesson_date, mark, mark_2 in zip(lesson_dates, student_2_marks, student_marks):
    print(lesson_date)

curren_date = input('введите дату:\n')
if not lesson_dates.count(curren_date):
    date_index = lesson_dates.index(curren_date)
    print(lesson_dates[date_index], ':', student_marks[date_index], student_2_marks[data_index])
else:
    print('ошибка', curren_date)

#print(student_marks[data_index], student_2_marks[data_index], lesson_dates[data_index])