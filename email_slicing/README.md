# Email Parser

A simple Python script that extracts the **username** and **domain** parts from an email address.

## Features
- Prompts the user to enter an email address
- Finds the position of the `@` symbol
- Extracts:
  - **Username** (everything before `@`)
  - **Domain** (everything after `@`)
- Displays the extracted parts in a readable format

## How to Run
1. Make sure you have **Python 3** installed.
2. Open your terminal and navigate to the project folder:
   ```bash
   cd email_slicing
3. Run the script:
    python email_slicing.py
4. Follow the prompt to enter an email address.

Example:
    Enter your email: example@gmail.com
    Your user_name is example and your domain is gmail.com

Notes:

    The script uses str.index("@") to locate the @ symbol.

    It assumes the input contains exactly one @ symbol and does not include advanced email validation.