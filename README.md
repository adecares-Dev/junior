````markdown name=README.md
# Simple Calculator Program

Welcome to the Simple Calculator Program!  
This program allows you to add, subtract, multiply, and divide two numbers with ease. It supports decimal numbers using Python's `float` type, making it versatile for a wide range of calculations.

## Features

- **Addition** (`+`)
- **Subtraction** (`-`)
- **Multiplication** (`*`)
- **Division** (`/`) with division-by-zero protection

## How It Works

1. **User Input**:  
   - The program asks you to enter the first number.
   - Then, it asks for the second number.
   - Finally, you choose the operation you want to perform (`+`, `-`, `*`, or `/`).

2. **Calculation**:  
   - Based on your chosen operation, the program performs the calculation.
   - If you attempt to divide by zero, the program will notify you that it's not allowed.

3. **Result**:  
   - The result is displayed in a readable format:  
     `<first number> <operation> <second number> = <result>`

## Example Usage

```shell
Enter the first number: 12.5
Enter the second number: 4.3
Enter the operation(+,-,*,/): +
12.5 + 4.3 = 16.8
```

## Error Handling

- If you enter an invalid operation (anything other than `+`, `-`, `*`, `/`), the program will print an error message.
- If you try to divide by zero, you'll see an error about division by zero.

## How to Run

1. Save the code to a file, for example, `calculator.py`.
2. Open your terminal or command prompt.
3. Run the program with:  
   ```shell
   python calculator.py
   ```

## Notes

- The program uses `float` for number inputs, so you can use both integers and decimals.
- Make sure you have Python installed on your computer.

---

Enjoy calculating like a pro!
````
