item = input("What item would you like to buy?: ")
price = float(input(f"what is the price of {item}?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: {round (total,2)} MAD")