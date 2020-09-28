mock_student_marks = [5, 4, 3, 2, 5]
#print(dir(mock_student_marks))

print (mock_student_marks)
mock_student_marks.append(5)
print(mock_student_marks)

print('5 count', mock_student_marks.index(5, 1))
print('2 count', mock_student_marks.index(5, 5))

num = 2
if mock_student_marks.count(15):
    print(num, 'found', mock_student_marks.count(num), 'times, first index',  mock_student_marks.index(num))

else:
    print(num, 'not found')


