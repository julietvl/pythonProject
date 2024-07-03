grades = [[5, 3, 3, 5, 4, 5, 3], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_students = list(students)
list.sort(list_students)

gpa_student_1 = (sum(grades[0])) / (len(grades[0]))
gpa_student_2 = (sum(grades[1])) / (len(grades[1]))
gpa_student_3 = (sum(grades[2])) / (len(grades[2]))
gpa_student_4 = (sum(grades[3])) / (len(grades[3]))
gpa_student_5 = (sum(grades[4])) / (len(grades[4]))

dict_students_top = {list_students[0]: gpa_student_1,
                     list_students[1]: gpa_student_2,
                     list_students[2]: gpa_student_3,
                     list_students[3]: gpa_student_4,
                     list_students[4]: gpa_student_5}

print(dict_students_top)
