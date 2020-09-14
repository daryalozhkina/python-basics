lesson_dates = ['19.05.15', '19.05.18', '19.05.19', '19.05.22']

student_marks = [5, 4, 3, 2, 5]


#i = 0
#while i < len(student_marks):
   # print(lesson_dates[i], 'оценка', student_marks[i])
   # i += 1
for item in student_marks:
     print('оценка', item)


for item in enumerate(student_marks):
     print('оценка', item)
     i, mark = item
     print('оценка', item, 'или', i, mark)

     for i, mark in enumerate(student_marks):
         print('оценка', i,mark)
  #  print(lesson_dates())

#user_full_name = ['Иван', 'Иванов']


#user_full_name = ['Иван', 'Иванов']
#first_name, second_name = user_full_name[0]
#print(first_name, second_name)

#a, b, c, d, e = [15, 45, 87, 96, 4]
#print(a, b, c, d, e)