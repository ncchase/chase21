import random

form_class_num = int(input("How many forms: "))
students = []
picked_students = []
player_runner_dict = {}

for x in range(form_class_num):

    new_form = []
    
    form_length = int(input(str("How many students in form ") + str(x) + ": "))

    for y in range(form_length):

        new_form.append(int((str(x) + str(y))))
    
    students.append(new_form)

for form in students:

    print(picked_students, "picked students 1")
    # temp = other form classes

    students_temp = students
    students_temp.remove(form)

    for student in form:

        random_form = random.choice(students_temp)

        random_student = random.choice(random_form)

        while random_student not in picked_students:
            
            
            random_student = random.choice(random_form)
            picked_students.append(random_student)
        
        player_runner_dict[student] = random_student

        print(picked_students, "picked students list 2")
    

print(player_runner_dict)
print(len(player_runner_dict))

