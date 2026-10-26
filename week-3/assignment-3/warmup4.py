number = int(input("Enter a number: "))
if number < 0:
  print(f"{number} is Negative.")
elif number == 0:
  print(f"{number} is Zero.")
else:
  print(f"{number} is Positive.")

if number %2 == 0:
  print(f"{number} is Even.")
else:
  print(f"{number} is Odd.")
