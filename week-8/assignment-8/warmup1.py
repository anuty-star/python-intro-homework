while True:

  try:
  
    number = float(input("enter a number: "))

  except ValueError:

    print("invalid number. Try again!")

  else:

    print("your number is:", number)
    break