# Simple Temperature Conversion

A basic Python script that converts temperatures between Celsius and Fahrenheit.

## Features
- Accepts temperature in **Celsius (C)** or **Fahrenheit (F)**
- Converts the entered temperature to the other unit
- Rounds the result to 2 decimal places
- Handles invalid unit inputs

## How to Run
1. Make sure you have **Python 3** installed.
2. Open your terminal and navigate to the project folder.
3. Run the script:
   ```bash
   python simple_temperature_conversion.py
4. Follow the prompts to enter the temperature unit and value.

Example:

   Enter a temperature unit in Celsius or fahrenheit (C/F): C
   Enter the temperature: 25
   the temperature is 845.0 Fahrenheit

Note:
   This script currently uses a multiplier/divider of 33.8 instead of the usual formula   for C↔F conversion.
   The standard formulas are:

   Celsius → Fahrenheit: (C * 9/5) + 32

   Fahrenheit → Celsius: (F - 32) * 5/9