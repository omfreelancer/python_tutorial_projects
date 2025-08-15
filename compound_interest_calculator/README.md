# Compound Interest Calculator

A simple Python script that calculates the future balance based on the **compound interest formula**:

\[
A = P \times \left(1 + \frac{R}{100}\right)^T
\]

Where:  
- **P** = Principal amount  
- **R** = Annual interest rate (%)  
- **T** = Time in years  
- **A** = Amount after T years

## Features
- Prompts for **principal**, **rate**, and **time** in years
- Validates that inputs are non-negative
- Calculates compound interest using the formula
- Displays the result rounded to 2 decimal places

## How to Run
1. Make sure you have **Python 3** installed.
2. Open your terminal and navigate to the project folder:
   ```bash
   cd compound_interest_calculator
3. Run the script:
    python compound_interest_calculator.py
4. Follow the prompts to enter principal, rate, and time.

Example:
    Hello to compound interest calculator

    Enter the principle amount: 1000
    Enter the rate amount: 5
    Enter the time in Year: 3
    Your balance after 3 year/s : 1157.63

Notes:

    Validates inputs to ensure they are non-negative.

    Interest is compounded once per year.