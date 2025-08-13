weight = float(input ("Enter the weight: "))
unit = input("Enter the unit: (K or L): ").upper()

if unit == "K":
    lbs = weight * 2.205
    print(f"{weight}kg = {round(lbs,3)}lbs")
elif unit == "L":
    kg = weight / 2.205
    print(f"{weight}lbs = {kg}kg")
else:
    print(f"'{unit}' is not a valid unit enter either \"k\" or \"L\"")