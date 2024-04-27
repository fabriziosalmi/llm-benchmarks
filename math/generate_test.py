import csv
import random

def create_test_cases(filename, number_of_cases, operations):
    """
    Generate a CSV file with math problems.

    Args:
    filename (str): The name of the CSV file to be created.
    number_of_cases (int): The number of math test cases to generate.
    operations (list): A list of operations to include, e.g., ['+', '-', '*', '/'].
    """
    max_number = 90000  # Maximum number for the math problems
    min_number = 10000     # Minimum number for the math problems

    # Prepare list to ensure unique questions
    questions = set()

    while len(questions) < number_of_cases:
        num1 = random.randint(min_number, max_number)
        num2 = random.randint(min_number, max_number)
        op = random.choice(operations)

        # Ensure no division by zero
        if op == '/' and num2 == 0:
            num2 += 1

        # Formulate the question and add to the set
        question = f"{num1} {op} {num2} ?"
        # question = f"Prepend prompt if you want here.. {num1} {op} {num2} ?"
        questions.add(question)

    # Write to CSV
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['test_id', 'test_content'])
        for idx, question in enumerate(questions, start=1):
            writer.writerow([idx, question])

# Example usage:
create_test_cases('test.csv', 100, ['+'])
# create_test_cases('test.csv', 10, ['+', '-', '*', '/'])
