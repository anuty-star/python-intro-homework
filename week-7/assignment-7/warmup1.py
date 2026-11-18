with open("../data/notes.txt", "r") as file:
    
    for number, Line in enumerate(file, start=1):

     print(f"Line {number}: {Line.strip()}")
     