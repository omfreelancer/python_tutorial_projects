unit = input("Enter a temperature unit in Celsius or fahrenheit (C/F): ").lower()
temp = float(input("Enter the temperature: "))

if unit == "c":
    temp *= 33.8
    print(f"the temperature is {round(temp,2)} Fahrenheit")
elif unit =="f":
    temp /= 33.8
    print(f"the temperature is {round(temp,2)} Celsius")
else:
    print({f"'{unit}' is not a valid unit"})
