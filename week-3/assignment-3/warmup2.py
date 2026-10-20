age = int(input("Enter your age: "))
if age >= 0 and age <= 12:
  print("you are a Child.")
elif age >= 13 and age <=17:
  print("you are a Teen.")
elif age >= 18 and age <= 64:
  print("you are an Adult.")
elif age >= 65:
  print("you are a Senior")
else:
  print("invalid age")