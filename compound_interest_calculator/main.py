print("Hello to compound interest calculator\n")

principal= float(input("Enter the principle amount: "))

while True:
    if principal < 0:
        print("Principle can't be less then 0")
        principal= float(input("Enter the principle amount: "))
    else:
        break

rate = float(input("Enter the rate amount: "))

while True:
    if rate < 0:
        print("Rate can't be less then 0")
        rate = float(input("Enter the rate amount: "))
    else:
        break

time = int(input("Enter the time in Year: "))

while True:
    if time < 0:
        print("Time can't be less then 0")
        time = int(input("Enter the time in Year: "))
    else:
        break

total = principal * pow(1 + rate / 100 , time)

print(f"Your balance after {time} year/s : {total:.2f}")