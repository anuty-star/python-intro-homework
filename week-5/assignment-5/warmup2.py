while True:
    try:
        number = int(input("Enter a positive integer: "))

        if number <= 0:
            print("That's not a positive integer. Try again.")
        else:
            print(f"Got it: {number}")
            break

    except:
        print("That's not a positive integer. Try again.")