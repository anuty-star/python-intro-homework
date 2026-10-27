student = {"name": "tigist", "grade": "A", "subjects": ["english", "math", "economics"]}
for key, value in student.items():
    print(key, value)

student["graduated"] = False

print(student)