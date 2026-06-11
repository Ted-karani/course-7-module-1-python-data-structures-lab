def format_student_data(student):
    """Return a formatted string for a given student tuple."""
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"

def display_students(students):
    """Loop through all students and print each student's details."""
    for student in students:
        print(format_student_data(student))