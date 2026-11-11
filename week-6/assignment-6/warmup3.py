def show_message():
    message = "Hello, Python!"
    print("Inside function:", message)


show_message()
#print(message)
#NameError: name 'message' is not defined


def get_message():
    message = "Hello, Python!"
    return message


result = get_message()

print("Outside function:", result)