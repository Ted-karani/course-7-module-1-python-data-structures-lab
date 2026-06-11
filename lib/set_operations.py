def unique_majors(students):
    """Return a set of unique student majors using set comprehension."""
    return {student[2] for student in students}