students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
highest_score = 0
top_scorer = ""

for student in students:
    if student["score"] > highest_score:
        highest_score = student["score"]
        top_scorer = student["name"]

print("Top scorer:", top_scorer)
print("Highest score:", highest_score)

total = 0

for student in students:
    total += student["score"]

class_average = total / len(students)

print("Class average:", class_average)

subjects = set()

for student in students:
    subjects.add(student["subject"])

print("Unique subjects:", subjects)

high_scorers = []

for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])

print("High scorers:", high_scorers)