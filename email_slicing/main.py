email = input("Enter your email: ")

index = email.index("@")

user_name = email[:index]

domain = email[index+1:]

print(f"Your user_name is {user_name} and your domain is {domain}")