# GET STUDENTS


def get_students(number_of_students):
    students = []
    for i in range(number_of_students):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        student = (name, age)
        students.append(student)
    students.sort(key=lambda x: x[1])
    assistant = students[0][0]
    teacher = students[-1][0]
    return assistant, teacher


assistant, teacher = get_students(5)

print(f"The teacher is {teacher} and the assistant is {assistant}")
