students = []

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
    else:
       print("ERROR, no student with this id was found")
def display_students():
  if not students:
      print("No students currently in the system.\n")
      return
  for student in students:
    print(f"Name: {student['name']} | ID: {student['id']} | Age: {student['age']}")
while True:
  add_student()
  ask = input("do you wish to remove any students(yes/no)?")
  if ask == "yes":
    remove_student()
    display_students()
  else:
    display_students()
  leave = input("would you like to leave this program(yes/no)")
  if leave == "yes":
    break
  
