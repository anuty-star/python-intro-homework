try:
    numerator = float(input("enter the numerator: "))
    denominator = float(input("enter the denominator: "))
    print(f"{numerator} / {denominator} = {numerator/denominator}")
except ZeroDivisionError:
    print("can't divide by zero. please enter non zero denominator")
  