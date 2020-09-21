student_marks = []
while True:
    mark = input('введите оценку студента:\n')
    if not mark:
        break
    mark = int(mark)
    if 1 <= mark <= 5:
            student_marks.append(mark)
    elif mark > 5:
        print('Оценка больше 5')
    elif mark < 1:
        print('Оценка больше 1')

print('ввод завершен')

# mark = "7"
# [ ] True
# students_marks = [4, 4, 3, 2, 4, 5, 5, 4, 2]
# mark = 7
# students_marks = [4, 4, 3, 2, 4, 5, 5, 4, 2, 7]
# True
# students_marks.remove [mark] -> students_marks.remove(7)
# remove() -> search in list (brute force, lineaf search)
# [4, 4, 3, 2, 4, 5, 5, 4, 2, 7], n - len(students_marks)
# [7, 4, 4, 3, 2, 4, 5, 5, 4, 2]
# list search complesity O(n)
# O(n) - о большое n