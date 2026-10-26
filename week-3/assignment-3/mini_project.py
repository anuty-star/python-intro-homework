day = input("what day is it?: ").lower()
time = input("what time of a day?: ").lower()

if day == "monday" and time == "morning":
  print("Morning you have group mentorship. be ready ")
elif day == "monday" and time == "afternoon":
  print("Afternoon don't forget doctor's appointment")
elif day == "monday" and time == "evening":
  print("evening it's good time to watch movie")
elif day == "tuesday" and time == "morning":
  print("morning go to the gym")
elif day == "tuesday" and time == "afternoon":
  print("afternoon we will have lunch at home")
elif day == "tuesday" and time == "evening":
  print("evening we will watch football")
elif day == "sunday" and time == "morning":
  print("every morning I love to go to church")
elif day == "sunday" and time == "afternoon":
  print("afternoon good time to visit family")
elif day == "sunday" and time == "evening":
  print("evening good time to have dinner at the restaurant")
else:
  print("Sorry, I don't recognize that day or time. Try again.")
  