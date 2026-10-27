def school_age(students):
    result = []
    for student in students:
        if student["age"] >= 5:
            result.append(student["name"])
    return result

kids = [
    {"name": "Maithreyi", "age": 5},
    {"name": "Aarav", "age": 4},
    {"name": "Ananya", "age": 6},
]
print(school_age(kids))
