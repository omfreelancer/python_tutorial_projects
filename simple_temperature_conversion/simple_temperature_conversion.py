unit = input("Enter a temperature unit in Celsius or fahrenheit (C/F): ").lower()
temp = float(input("Enter the temperature: "))

if unit == "c":
    temp = temp * 9 / 5 + 32 
    print(f"the temperature is {round(temp,2)} °F")
elif unit =="f":
    temp = (temp - 32) * 5/9 
    print(f"the temperature is {round(temp,2)} °C")
else:
    print({f"'{unit}' is not a valid unit"})
