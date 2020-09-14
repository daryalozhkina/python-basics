student_marks = []
while True:
    mark = input('введите оценку студента: ')
    if mark:
        student_marks.append(int(mark))
    else:
        break
print('ввод завершен')
print(student_marks)