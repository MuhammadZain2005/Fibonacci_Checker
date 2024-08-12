"""
FIBONACCI CHECKER
Difficulty : 1/10
Comments:
Iterative Fibonacci Calculation: This method is more efficient than the recursive approach.
Input Validation: Ensures the user inputs a valid non-negative integer.
Fibonacci Number Check: The program now checks if the user’s input is a Fibonacci number and informs them accordingly.
Helper Function: The is_perfect_square function checks if a number is a perfect square, which is used to determine if a number is a Fibonacci number.
"""


def is_fibonacci_number(n):
    # A function to check if a number is a perfect square
    def is_perfect_square(x):
        s = int(x ** 0.5)
        return s * s == x

    # A number is a Fibonacci number if and only if one or both of
    # (5 * n^2 + 4) or (5 * n^2 - 4) is a perfect square
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Input validation
while True:
    try:
        user_input = int(input("Enter a non-negative number > "))
        if user_input < 0:
            raise ValueError("Please enter a non-negative number.")
        break
    except ValueError as e:
        print(e)

fib_value = fibonacci(user_input)
print(f"Fibonacci({user_input}) = {fib_value}")

# Check if the number itself is a Fibonacci number
if is_fibonacci_number(user_input):
    print(f"{user_input} is a Fibonacci number.")
else:
    print(f"{user_input} is not a Fibonacci number.")
