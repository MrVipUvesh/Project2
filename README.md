# Pattern Generator and Number Analyzer

A simple menu-driven Python program that can generate a star pattern and analyze a range of numbers.

This project is made for practicing basic Python concepts like loops, conditional statements, user input, ranges, arithmetic operations, and formatted output.

## Features

- Generate a star pattern based on the number of rows
- Check whether numbers are Even or Odd
- Calculate the sum of numbers within a given range
- Interactive menu system
- Continue using the program until the user chooses to exit

## How It Works

When the program starts, it displays a menu with three options:

1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

### 1. Generate a Pattern

The program asks the user for the number of rows and generates a simple star pattern.

For example, if the user enters `5`, the output will look like:

    Pattern:
    *
    **
    ***
    ****
    *****

This part of the program uses nested `for` loops to generate the pattern.

### 2. Analyze a Range of Numbers

The program asks the user for a starting number and an ending number.

It then goes through every number in the given range, checks whether it is Even or Odd, and calculates the sum of all the numbers.

Example:

    Enter the start of the range: 1
    Enter the end of the range: 5

    Number 1 is Odd
    Number 2 is Even
    Number 3 is Odd
    Number 4 is Even
    Number 5 is Odd

    Sum of all numbers from 1 to 5 is: 15

### 3. Exit

Selecting option `3` exits the program.

    Exiting the program. Goodbye!

## Concepts Used

### User Input

The `input()` function is used to take values from the user.

### Type Conversion

`int()` is used to convert user input into integers so that the values can be used for calculations and ranges.

### While Loop

A `while True` loop keeps the program running and repeatedly displays the menu until the user chooses to exit.

### For Loop

`for` loops are used to generate the pattern and process numbers within the selected range.

### Nested Loops

The pattern generator uses a `for` loop inside another `for` loop to print the required number of stars.

### Conditional Statements

`if`, `elif`, and `else` are used to perform different actions depending on the user's choice.

### Modulus Operator

The `%` operator is used to check whether a number is even or odd.

    i % 2 == 0

If the remainder is `0`, the number is Even. Otherwise, it is Odd.

### Ternary Conditional Expression

The program uses a short conditional expression to display either `Even` or `Odd`.

    "Even" if i % 2 == 0 else "Odd"

### Range

The `range()` function is used to generate a sequence of numbers.

    range(start, end + 1)

Using `end + 1` makes sure that the ending number is also included.

### Running Sum

A variable is used to keep adding each number and calculate the final sum.

    sum = 0

    for i in range(start, end + 1):
        sum += i

## Requirements

You only need Python installed on your computer.

You can check whether Python is installed by running:

    python --version

## How to Run

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Run the Python file using:

       python main.py

4. Select an option from the menu.
5. Enter the required values.
6. Continue using the program or choose `3` to exit.

## Program Flow

    Start
      |
      v
    Display Menu
      |
      v
    Choose Option
      |
      +---- 1 --> Generate Pattern
      |             |
      |             v
      |         Enter Rows
      |             |
      |             v
      |        Display Pattern
      |
      +---- 2 --> Analyze Number Range
      |             |
      |             v
      |       Enter Start & End
      |             |
      |             v
      |       Check Even / Odd
      |             |
      |             v
      |        Calculate Sum
      |
      +---- 3 --> Exit
                    |
                    v
                   End

## Purpose

This project is a small practice program created to understand and apply basic Python programming concepts in an interactive way.

It brings together loops, conditions, user input, arithmetic operations, ranges, and formatted output in one simple program.

---

Made for learning Python through practice. 🐍
