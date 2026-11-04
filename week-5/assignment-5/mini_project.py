numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    # OPTION 1: Find minimum
    if choice == "1":
        smallest = numbers[0]

        for num in numbers:
            if num < smallest:
                smallest = num

        print("Minimum number:", smallest)

    # OPTION 2: Find maximum
    elif choice == "2":
        largest = numbers[0]

        for num in numbers:
            if num > largest:
                largest = num

        print("Maximum number:", largest)

    # OPTION 3: Search for a number
    elif choice == "3":
        target = int(input("Enter a number to search: "))
        index = -1

        for i in range(len(numbers)):
            if numbers[i] == target:
                index = i
                break

        if index != -1:
            print(target, "found at index", index)
        else:
            print(target, "not found in the list.")

    # OPTION 4: Bubble sort
    elif choice == "4":
        swapped = True

        while swapped:
            swapped = False

            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True

        print("Sorted list:", numbers)

    # OPTION 5: Quit
    elif choice == "5":
        print("Thank you for using Number Cruncher. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose between 1 and 5.")