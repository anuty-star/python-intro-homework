
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93,
           31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


# 1. Find the minimum number
def find_min(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


# 2. Find the maximum number
def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


# 3. Search for a number
def search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


# 4. Bubble sort (returns a new sorted list)
def bubble_sort(numbers):
    sorted_numbers = numbers.copy()

    for i in range(len(sorted_numbers)):
        for j in range(len(sorted_numbers) - 1 - i):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1], sorted_numbers[j]
                )

    return sorted_numbers


# 5. Display the menu
def show_menu():
    print("\n===== NUMBER CRUNCHER =====")
    print("1. Find Minimum")
    print("2. Find Maximum")
    print("3. Search for a Number")
    print("4. Bubble Sort")
    print("5. Exit")

    choice = input("Enter your choice: ")
    return choice


# 6. Main program
def main():
    while True:
        choice = show_menu()

        if choice == "1":
            print("Minimum:", find_min(numbers))

        elif choice == "2":
            print("Maximum:", find_max(numbers))

        elif choice == "3":
            target = int(input("Enter number to search: "))
            result = search(numbers, target)

            if result != -1:
                print(f"Found at index {result}")
            else:
                print("Not found")

        elif choice == "4":
            print("Original list:", numbers)
            print("Sorted list:", bubble_sort(numbers))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()
