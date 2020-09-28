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

#lesson_dates_and_marks = [
 #   ['19.05.15', 5],
  #  ['19.05.18', 4],
   # ['19.05.19', 3],
for lesson_date, mark, mark_2 in zip(lesson_dates, student_2_marks, student_marks):
    print(lesson_date, 'оценка', mark, mark_2)

#user_full_name = ['Иван', 'Иванов']


#user_full_name = ['Иван', 'Иванов']
#first_name, second_name = user_full_name[0]
#print(first_name, second_name)

#a, b, c, d, e = [15, 45, 87, 96, 4]
#print(a, b, c, d, e)