def filter_students_by_major(students, major):
    """Return a list of students filtered by major using list comprehension."""
    return [student for student in students if student[2] == major]