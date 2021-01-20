import random

form_class_num = int(input("How many forms: "))
students = []


for x in range(form_class_num):

    new_form = []
    
    form_length = int(input(str("How many students in form ") + str(x) + ": "))

    for y in range(form_length):

        new_form.append(int((str(x) + str(y))))
    
    students.append(new_form)

print(students)

