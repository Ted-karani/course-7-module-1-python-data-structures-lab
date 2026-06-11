def student_generator(students, major):
    """Return a generator expression for all students filtered by major."""
    return (student for student in students if student[2] == major)