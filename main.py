import math

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    return math.factorial(n)

def main():
    print("Welcome to the Factorial Calculator!")
    try:
        num = int(input("Enter a non-negative integer: "))
        result = factorial(num)
        print(f"The factorial of {num} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()