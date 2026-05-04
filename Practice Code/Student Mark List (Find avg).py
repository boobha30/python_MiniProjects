
mark_list={}
number_of_students=int(input("Enter the number of students: "))
for i in range(number_of_students):
    name=input(f"Enter the name of student {i+1}: ")
    mark=float(input(f"Enter the mark for student {i+1}: "))
    mark_list[name]=mark
print("Student Mark List:")
for name, mark in mark_list.items():
    print(f"{name}: {mark}")
average_mark=sum(mark_list.values())/number_of_students
print(f"The average mark of the students is: {average_mark:.2f}")
