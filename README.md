# Student Management System

A simple Python program that allows users to manage student records through the command line.

## Features

* Add students to the system
* Remove students by ID
* Display all students currently stored
* Simple and beginner-friendly Python code

## How It Works

Each student is stored as a dictionary containing:

* ID
* Name
* Age

The program keeps all student records in a list while it is running.

## Requirements

* Python 3.x

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/student-management-system.git
```

2. Navigate to the project folder:

```bash
cd student-management-system
```

3. Run the program:

```bash
python main.py
```

## Usage

When the program starts, it will:

1. Ask for a student's ID.
2. Ask for the student's age.
3. Ask for the student's name.
4. Add the student to the system.
5. Optionally remove a student by entering their ID.
6. Display all current students.
7. Allow the user to continue or exit.

### Example

```text
What is the students ID? 101
What is the student age? 12
what is the students name? Alex

student added successfully!

do you wish to remove any students(yes/no)? no

Name: Alex | ID: 101 | Age: 12
```

## Project Structure

```text
student-management-system/
│
├── main.py
└── README.md
```

## Future Improvements

* Save student data to a file
* Edit student information
* Search for students by ID or name
* Validate user input
* Create a menu-based interface
* Store ages and IDs as integers

## Author

Created as a beginner Python project for learning functions, loops, lists, dictionaries, and user input.
