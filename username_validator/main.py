user_name = input("Enter your name: ")

if len(user_name) > 12:
    print("Your user name should not be more then 12 characters")
elif not user_name.find(" ") == -1:
    print("Your user name should not have space")
elif not user_name.isalpha():
    print("Your user name should not have numbers")
else:
    print(f"Welcome {user_name}")