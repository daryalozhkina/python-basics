student_marks = []
while True:
    mark = input('введите оценку студента:\n')
    if not mark:
        break
    if len(mark) != 1:
        print('вы ввели не один символ')
        continue
   # if not 48 <- ord(mark) <- 57:
    #    print('вы ввели не число')
    #    continue

    if mark.isdigit():
        mark = int(mark)
        if 1 <= mark <= 5:
            student_marks.append(mark)
        elif mark > 5:
            print('Оценка больше 5')
        elif mark < 1:
            print('Оценка меньше 1')
    else:
        print('ошибка', mark)
    try:
        mark = int(mark)
        if 1 <= mark <= 5:
             student_marks.append(mark)
        elif mark > 5:
            print('Оценка больше 5')
        elif mark < 1:
            print('Оценка меньше 1')
    except ValueError as e:
        print('ошибка значения', e)
    except TypeError as e:
        print('ошибка значения', e)
    except Exception as e:
        print('была допущена ошибка', e)

print('ввод завершен', student_marks)