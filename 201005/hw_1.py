with open('students_log.txt', 'r', encoding='utf-8') as f:
    for row in f.read().splitlines():
        last_name, first_name, patronymic, row_marks = row.split(maxsplit=3)
        patronymic = patronymic.strip(',')
        marks = list(map(int, map(str.strip, row_marks.split(','))))
        # marks = []
        # for mark in row_marks.split(','):
        #     marks.append(mark.strip())
        # map(callback_1, iterable)
        # map(callback_2, iterable)
        avg_mark = sum(marks) / len(marks)
        print(last_name, first_name, patronymic, ':', marks, 'средний балл', avg_mark)
        # for row in f:
        # for sym in row:
        #     print(sym)
        # shadow = []
        # for sym in row:
        # while i < l:
        #     s_int = ''
        #     a = row[i]
            # while '0' <= a <= '9':
            #     s_int += a
            #     i += 1
            #     if i < l:
            #         a = row[i]
            #     else:
            #         break
                  # print(row.split()[0], row.split()[1], row.split()[2].replace(",", ":"), integ)


        # avg = statistics.mean(integ)
        # print(avg