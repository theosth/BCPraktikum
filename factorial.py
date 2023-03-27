import sys
from dotenv import load_dotenv

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Please provide an integer value.")
        sys.exit(1)

    if number < 0:
        print("Factorial is not defined for negative numbers.")
        sys.exit(1)

    result = factorial(number)
    with open("output.txt", "w") as output_file:
        output_file.write(f"Factorial of {number} is {result}\n")
