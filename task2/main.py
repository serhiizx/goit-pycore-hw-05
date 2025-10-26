from typing import Callable
import re

# Function to find and yield numbers from text
def generator_numbers(text: str):
    # Find all numbers (like 1000.01, 27.45, or .5) in the text
    result = re.findall(r' (?:\d+\.\d*|\.\d+) ', text)

    # Remove extra spaces from each number
    stripped_result = [x.strip() for x in result]

    # Convert each number to float and yield it
    for element in stripped_result:
        yield float(element)

# Function to sum up all numbers from the generator
def sum_profit(text: str, func: Callable):
    result = 0

    for num in func(text):
        result += num

    return result


# Sample text with numbers
text = ("Загальний дохід працівника складається з"
        " декількох частин: 1000.01 як основний дохід, доповнений"
        " додатковими надходженнями 27.45 і 324.00 доларів.")

# Calculate total income using the function
total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}") # Expected: Загальний дохід: 1351.46


