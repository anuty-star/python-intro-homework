names = ["hana", "meron", "tigist", "helen", "zele"]

search_name = input("Enter a name to search for: ")

found = False

for i in range(len(names)):
    if names[i] == search_name:
        print(f'Found "{search_name}" at index {i}.')
        found = True
        break

if not found:
    print(f'"{search_name}" was not found in the list.')