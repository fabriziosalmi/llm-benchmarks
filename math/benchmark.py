import csv
import requests
import json
import re
from collections import defaultdict
import pandas as pd
from tabulate import tabulate
from tqdm import tqdm

def send_question(api_url, question):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "microsoft/Phi-3-mini-4k-instruct-gguf",
        "messages": [
            {"role": "system", "content": "Calculate the result. Provide the result only."},
            {"role": "user", "content": question}
        ],
        "temperature": 0,
        "max_tokens": 128,
        "stream": False
    }
    response = requests.post(api_url, headers=headers, json=data)
    return response.json()

def extract_numeric_answer(text):
    match = re.findall(r"[-+]?\d*\.?\d+", text)
    if match:
        result = match[-1]
        try:
            return float(result) if '.' in result else int(result)
        except ValueError:
            return None
    return None

def process_questions(filename, api_url, iterations=2):
    results = []
    summary_stats = defaultdict(lambda: {'correct_count': 0, 'responses': []})
    question_count = sum(1 for _ in open(filename, 'r')) - 1  # Adjusting for header

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in tqdm(reader, total=question_count, desc="Processing questions"):
            question = row['test_content'].strip()
            parts = re.findall(r"(\d+)\s*([\+\-\*\/])\s*(\d+)", question)
            if not parts:
                tqdm.write(f"Skipping improperly formatted question: {question}")
                continue
            num1, operator, num2 = int(parts[0][0]), parts[0][1], int(parts[0][2])
            math_question = f"{num1} {operator} {num2}"
            local_answer = eval(math_question)  # Calculate the correct answer once per question
            for i in range(iterations):
                tqdm.write(f"Round {i+1} for question ID {row['test_id']}")
                response = send_question(api_url, math_question)
                if response and 'choices' in response and response['choices']:
                    answer_text = response['choices'][0]['message']['content']
                    answer = extract_numeric_answer(answer_text)
                    correct = answer == local_answer
                    results.append({
                        "test_id": row['test_id'],
                        "iteration": i + 1,
                        "question": math_question,
                        "correct": correct,
                        "received_answer": answer_text,
                        "final_answer": answer,
                        "correct_answer": local_answer  # Store the correct calculated answer
                    })
                    summary_stats[row['test_id']]['correct_count'] += correct
                    summary_stats[row['test_id']]['responses'].append(answer)

    # Data summarization for table
    df_summary = pd.DataFrame([{
        "test_id": key,
        "correct_runs": value['correct_count'],
        "total_runs": iterations,
        "correctness_percentage": (value['correct_count'] / iterations) * 100
    } for key, value in summary_stats.items()])

    print(tabulate(df_summary, headers='keys', tablefmt='pretty', showindex=False))

    # Save detailed results to JSON
    with open('results_detailed.json', 'w') as jsonfile:
        json.dump(results, jsonfile, indent=4)

# Example usage:
process_questions('test.csv', 'http://localhost:1234/v1/chat/completions')
