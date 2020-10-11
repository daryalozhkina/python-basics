import students_parse

students_log = students_parse.parse_marks('students_log.txt')
students_parse.show_marks(students_log, raw=False)
# students_parse.show_marks(students_log, raw=False, sep =' | ')
# students_parse.parse_marks('students_log_2.txt')

# print(students_log)
# print(students_log_2)

# students_parse.parse_marks(students_log)
# students_parse.save_marks('students_log.csv)