def calculate_factorial(n):
    """Calculate the factorial of a number."""
    factorial_result = 1

    # Using a loop to perform multiplication
    for i in range(1, n + 1):
        factorial_result *= i

    return factorial_result

def main():
    # Get user input for a number
    user_input = input("Enter a number to calculate its factorial: ")

    try:
        # Convert user input to an integer
        number = int(user_input)

        # Check if the number is non-negative
        if number >= 0:
            result = calculate_factorial(number)
            print(f"The factorial of {number} is: {result}")
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
