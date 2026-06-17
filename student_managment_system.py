def add_student():
  student_ID = input("What is the students ID?")
  student_age = input("What is the student age?")
  student_name = input("what is the students name?")

  student = {
      "id": student_ID,
      "age": student_age,
      "name": student_name
  }
  students.append(student)
  print("student added successfully!")
def remove_student():
  remove_id = input("enter the ID of the student you wish to remove")
  for student in students:
    if student["id"] == remove_id:
      students.remove(student)
      print("student has been removed")
      return
while True:
  add_student()
  ask = input("do you wish to remove any students?")
  if ask == "yes":
    remove_student()
    print(students)
  else:
    print(students)
