import random

form_class_num = int(input("How many forms: "))
students = []
player_runner_dict = {}

for x in range(form_class_num):

    new_form = []
    
    form_length = int(input(str("How many students in form ") + str(x) + ": "))

    for y in range(form_length):

        new_form.append(int((str(x) + str(y))))
    
    students.append(new_form)

for form in students:

    # temp = other form classes

    students_temp = students
    students_temp.pop(form)

    for student in form:

        random_form = random.choice(students)

        random_student = random.choice(random_form)

        player_runner_dict[student] = random_student

        students[students.index(random_form)].remove(random_student)

print(player_runner_dict)

