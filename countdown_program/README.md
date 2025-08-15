# Countdown Program

A simple Python script that counts down from a user-specified number of seconds, displaying the time in `HH:MM:SS` format.

## Features
- Prompts the user to enter a countdown time in seconds
- Displays the countdown in hours, minutes, and seconds (zero-padded)
- Updates every second using `time.sleep(1)`
- Prints **"Time's up!"** when finished

## How to Run
1. Make sure you have **Python 3** installed.
2. Open your terminal and navigate to the project folder:
   ```bash
   cd countdown_program
3. Run the script:
    python countdown_program.py
4. Enter the countdown time in seconds and watch the timer run.

Example:
    Enter the time in seconds: 75
    00:01:15
    00:01:14
    ...
    00:00:02
    00:00:01
    Time's up!

Notes

Time is displayed in HH:MM:SS format using zero-padding (02 formatting).

The program uses time.sleep(1) for real-time countdown updates.