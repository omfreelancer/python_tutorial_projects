print("Hello to the Shopping Cart app \n")

foods = []
prices = []

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else: 
        price = float(input(f"Enter the price of {food} in MAD: "))
        foods.append(food)
        prices.append(price)

print("\n----- YOUR CART -----")
print(f"{'item':20} {'price (MAD)':>10}")

for x in range(len(foods)):
    print(f"{foods[x]:20} {prices[x]:>10.2f} MAD")