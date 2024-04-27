import csv
import requests
import json
import re

def send_question(api_url, question):
    """
    Send a math question to the specified API and receive the response.
    Args:
    api_url (str): The API endpoint for sending questions.
    question (str): The math question to send.
    Returns:
    str: The response from the API.
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "microsoft/Phi-3-mini-4k-instruct-gguf",
        "messages": [
            {"role": "system", "content": "Calculate the result."},
            {"role": "user", "content": question}
        ],
        "temperature": 0,
        "max_tokens": 128,
        "stream": False
    }
    response = requests.post(api_url, headers=headers, json=data)
    return response.json()

def extract_numeric_answer(text):
    """
    Extract the numeric result from a string response.
    Args:
    text (str): The text from which to extract the numeric result.
    Returns:
    float: The extracted numeric result, rounded if decimal is zero.
    """
    match = re.findall(r"[-+]?\d*\.?\d+", text)
    if match:
        result = float(match[-1])
        return result if result % 1 != 0 else int(result)
    return None

def process_questions(filename, api_url):
    """
    Process all questions from a CSV file, interact with API, and save results along with correctness statistics.
    Args:
    filename (str): The CSV file containing math questions.
    api_url (str): The API endpoint for interaction.
    """
    results = []
    correct_count = 0
    total_questions = 0
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            question = row['test_content'].strip()
            # Extract the arithmetic part from the question using regex
            parts = re.findall(r"(\d+)\s*([\+\-\*\/])\s*(\d+)", question)
            if not parts:
                print(f"Skipping improperly formatted question: {question}")
                continue
            num1, operator, num2 = int(parts[0][0]), parts[0][1], int(parts[0][2])  # Correctly map to int
            total_questions += 1
            math_question = f"{num1} {operator} {num2}"
            response = send_question(api_url, math_question)
            if response and 'choices' in response and response['choices']:
                answer_text = response['choices'][0]['message']['content']
                answer = extract_numeric_answer(answer_text)
                local_answer = eval(math_question)
                correct = answer == local_answer
                results.append({
                    "test_id": row['test_id'],
                    "question": math_question,
                    "correct": correct,
                    "received_answer": answer_text,
                    "final_answer": answer
                })
                if correct:
                    correct_count += 1
            else:
                print(f"No valid response for question: {math_question}")

    # Calculate and print correctness percentage to the terminal
    if total_questions > 0:
        correctness_percentage = (correct_count / total_questions) * 100
        print(f"Correctness Percentage: {correctness_percentage:.2f}%")

    # Save results to JSON
    with open('results.json', 'w') as jsonfile:
        json.dump(results, jsonfile, indent=4)

# Example usage:
process_questions('test.csv', 'http://localhost:1234/v1/chat/completions')
