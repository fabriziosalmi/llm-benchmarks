# Simple MATH benchmark for LLMs

Discussion [https://www.reddit.com/r/LocalLLaMA/comments/1cdxjax/comment/l1gq754/?context=3](here)

## Requirements

- any LLM local inference server based on llama.cpp
- a quantized model like llama3 or phi3

## Testing

**generate_data.py**

You can change range by increasing max_number:

`max_number = 9999  # Maximum number for the math problems`

You can change operations for tests

```
# Example usage:
# create_test_cases('test.csv', 100, ['+'])
create_test_cases('test.csv', 10, ['+', '*'])
# create_test_cases('test.csv', 10, ['+', '-', '*', '/'])
```

**benchmark.py**

You can change number of iterations:

`def process_questions(filename, api_url, iterations=2):`


**Example test**

I'm testing on Apple MacBook Pro M2, tested up to 999999999 as max_number and up to 10 iterations per question.

```
(llmbench-env) MacBook-Pro:LLMbench fab$ python generate_test.py
(llmbench-env) MacBook-Pro:LLMbench fab$ python benchmark.py
Round 1 for question ID 1
Round 2 for question ID 1
Round 1 for question ID 2
Round 2 for question ID 2
Round 1 for question ID 3
Round 2 for question ID 3
Round 1 for question ID 4
Round 2 for question ID 4
Round 1 for question ID 5
Round 2 for question ID 5
Round 1 for question ID 6
Round 2 for question ID 6
Round 1 for question ID 7
Round 2 for question ID 7
Round 1 for question ID 8
Round 2 for question ID 8
Round 1 for question ID 9
Round 2 for question ID 9
Round 1 for question ID 10
Round 2 for question ID 10
Round 1 for question ID 11
Round 2 for question ID 11
Round 1 for question ID 12
Round 2 for question ID 12
Round 1 for question ID 13
Round 2 for question ID 13
Round 1 for question ID 14
Round 2 for question ID 14
Round 1 for question ID 15
Round 2 for question ID 15
Round 1 for question ID 16
Round 2 for question ID 16
Round 1 for question ID 17
Round 2 for question ID 17
Round 1 for question ID 18
Round 2 for question ID 18
Round 1 for question ID 19
Round 2 for question ID 19
Round 1 for question ID 20
Round 2 for question ID 20
Round 1 for question ID 21
Round 2 for question ID 21
Round 1 for question ID 22
Round 2 for question ID 22
Round 1 for question ID 23
Round 2 for question ID 23
Round 1 for question ID 24
Round 2 for question ID 24
Round 1 for question ID 25
Round 2 for question ID 25
Round 1 for question ID 26
Round 2 for question ID 26
Round 1 for question ID 27
Round 2 for question ID 27
Round 1 for question ID 28
Round 2 for question ID 28
Round 1 for question ID 29
Round 2 for question ID 29
Round 1 for question ID 30
Round 2 for question ID 30
Round 1 for question ID 31
Round 2 for question ID 31
Round 1 for question ID 32
Round 2 for question ID 32
Round 1 for question ID 33
Round 2 for question ID 33
Round 1 for question ID 34
Round 2 for question ID 34
Round 1 for question ID 35
Round 2 for question ID 35
Round 1 for question ID 36
Round 2 for question ID 36
Round 1 for question ID 37
Round 2 for question ID 37
Round 1 for question ID 38
Round 2 for question ID 38
Round 1 for question ID 39
Round 2 for question ID 39
Round 1 for question ID 40
Round 2 for question ID 40
Round 1 for question ID 41
Round 2 for question ID 41
Round 1 for question ID 42
Round 2 for question ID 42
Round 1 for question ID 43
Round 2 for question ID 43
Round 1 for question ID 44
Round 2 for question ID 44
Round 1 for question ID 45
Round 2 for question ID 45
Round 1 for question ID 46
Round 2 for question ID 46
Round 1 for question ID 47
Round 2 for question ID 47
Round 1 for question ID 48
Round 2 for question ID 48
Round 1 for question ID 49
Round 2 for question ID 49
Round 1 for question ID 50
Round 2 for question ID 50
Round 1 for question ID 51
Round 2 for question ID 51
Round 1 for question ID 52
Round 2 for question ID 52
Round 1 for question ID 53
Round 2 for question ID 53
Round 1 for question ID 54
Round 2 for question ID 54
Round 1 for question ID 55
Round 2 for question ID 55
Round 1 for question ID 56
Round 2 for question ID 56
Round 1 for question ID 57
Round 2 for question ID 57
Round 1 for question ID 58
Round 2 for question ID 58
Round 1 for question ID 59
Round 2 for question ID 59
Round 1 for question ID 60
Round 2 for question ID 60
Round 1 for question ID 61
Round 2 for question ID 61
Round 1 for question ID 62
Round 2 for question ID 62
Round 1 for question ID 63
Round 2 for question ID 63
Round 1 for question ID 64
Round 2 for question ID 64
Round 1 for question ID 65
Round 2 for question ID 65
Round 1 for question ID 66
Round 2 for question ID 66
Round 1 for question ID 67
Round 2 for question ID 67
Round 1 for question ID 68
Round 2 for question ID 68
Round 1 for question ID 69
Round 2 for question ID 69
Round 1 for question ID 70
Round 2 for question ID 70
Round 1 for question ID 71
Round 2 for question ID 71
Round 1 for question ID 72
Round 2 for question ID 72
Round 1 for question ID 73
Round 2 for question ID 73
Round 1 for question ID 74
Round 2 for question ID 74
Round 1 for question ID 75
Round 2 for question ID 75
Round 1 for question ID 76
Round 2 for question ID 76
Round 1 for question ID 77
Round 2 for question ID 77
Round 1 for question ID 78
Round 2 for question ID 78
Round 1 for question ID 79
Round 2 for question ID 79
Round 1 for question ID 80
Round 2 for question ID 80
Round 1 for question ID 81
Round 2 for question ID 81
Round 1 for question ID 82
Round 2 for question ID 82
Round 1 for question ID 83
Round 2 for question ID 83
Round 1 for question ID 84
Round 2 for question ID 84
Round 1 for question ID 85
Round 2 for question ID 85
Round 1 for question ID 86
Round 2 for question ID 86
Round 1 for question ID 87
Round 2 for question ID 87
Round 1 for question ID 88
Round 2 for question ID 88
Round 1 for question ID 89
Round 2 for question ID 89
Round 1 for question ID 90
Round 2 for question ID 90
Round 1 for question ID 91
Round 2 for question ID 91
Round 1 for question ID 92
Round 2 for question ID 92
Round 1 for question ID 93
Round 2 for question ID 93
Round 1 for question ID 94
Round 2 for question ID 94
Round 1 for question ID 95
Round 2 for question ID 95
Round 1 for question ID 96
Round 2 for question ID 96
Round 1 for question ID 97
Round 2 for question ID 97
Round 1 for question ID 98
Round 2 for question ID 98
Round 1 for question ID 99
Round 2 for question ID 99
Round 1 for question ID 100
Round 2 for question ID 100
Processing questions: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [03:18<00:00,  1.98s/it]
+---------+--------------+------------+------------------------+
| test_id | correct_runs | total_runs | correctness_percentage |
+---------+--------------+------------+------------------------+
|    1    |      0       |     2      |          0.0           |
|    2    |      2       |     2      |         100.0          |
|    3    |      2       |     2      |         100.0          |
|    4    |      2       |     2      |         100.0          |
|    5    |      2       |     2      |         100.0          |
|    6    |      2       |     2      |         100.0          |
|    7    |      2       |     2      |         100.0          |
|    8    |      2       |     2      |         100.0          |
|    9    |      2       |     2      |         100.0          |
|   10    |      2       |     2      |         100.0          |
|   11    |      2       |     2      |         100.0          |
|   12    |      0       |     2      |          0.0           |
|   13    |      2       |     2      |         100.0          |
|   14    |      2       |     2      |         100.0          |
|   15    |      2       |     2      |         100.0          |
|   16    |      2       |     2      |         100.0          |
|   17    |      2       |     2      |         100.0          |
|   18    |      0       |     2      |          0.0           |
|   19    |      2       |     2      |         100.0          |
|   20    |      2       |     2      |         100.0          |
|   21    |      2       |     2      |         100.0          |
|   22    |      2       |     2      |         100.0          |
|   23    |      0       |     2      |          0.0           |
|   24    |      2       |     2      |         100.0          |
|   25    |      0       |     2      |          0.0           |
|   26    |      0       |     2      |          0.0           |
|   27    |      0       |     2      |          0.0           |
|   28    |      0       |     2      |          0.0           |
|   29    |      0       |     2      |          0.0           |
|   30    |      2       |     2      |         100.0          |
|   31    |      2       |     2      |         100.0          |
|   32    |      2       |     2      |         100.0          |
|   33    |      2       |     2      |         100.0          |
|   34    |      2       |     2      |         100.0          |
|   35    |      2       |     2      |         100.0          |
|   36    |      2       |     2      |         100.0          |
|   37    |      0       |     2      |          0.0           |
|   38    |      0       |     2      |          0.0           |
|   39    |      2       |     2      |         100.0          |
|   40    |      0       |     2      |          0.0           |
|   41    |      2       |     2      |         100.0          |
|   42    |      0       |     2      |          0.0           |
|   43    |      2       |     2      |         100.0          |
|   44    |      2       |     2      |         100.0          |
|   45    |      2       |     2      |         100.0          |
|   46    |      2       |     2      |         100.0          |
|   47    |      2       |     2      |         100.0          |
|   48    |      2       |     2      |         100.0          |
|   49    |      0       |     2      |          0.0           |
|   50    |      2       |     2      |         100.0          |
|   51    |      0       |     2      |          0.0           |
|   52    |      2       |     2      |         100.0          |
|   53    |      2       |     2      |         100.0          |
|   54    |      0       |     2      |          0.0           |
|   55    |      2       |     2      |         100.0          |
|   56    |      2       |     2      |         100.0          |
|   57    |      2       |     2      |         100.0          |
|   58    |      2       |     2      |         100.0          |
|   59    |      0       |     2      |          0.0           |
|   60    |      0       |     2      |          0.0           |
|   61    |      0       |     2      |          0.0           |
|   62    |      2       |     2      |         100.0          |
|   63    |      0       |     2      |          0.0           |
|   64    |      0       |     2      |          0.0           |
|   65    |      2       |     2      |         100.0          |
|   66    |      2       |     2      |         100.0          |
|   67    |      2       |     2      |         100.0          |
|   68    |      2       |     2      |         100.0          |
|   69    |      2       |     2      |         100.0          |
|   70    |      2       |     2      |         100.0          |
|   71    |      2       |     2      |         100.0          |
|   72    |      2       |     2      |         100.0          |
|   73    |      0       |     2      |          0.0           |
|   74    |      2       |     2      |         100.0          |
|   75    |      0       |     2      |          0.0           |
|   76    |      0       |     2      |          0.0           |
|   77    |      2       |     2      |         100.0          |
|   78    |      0       |     2      |          0.0           |
|   79    |      2       |     2      |         100.0          |
|   80    |      2       |     2      |         100.0          |
|   81    |      0       |     2      |          0.0           |
|   82    |      0       |     2      |          0.0           |
|   83    |      0       |     2      |          0.0           |
|   84    |      2       |     2      |         100.0          |
|   85    |      0       |     2      |          0.0           |
|   86    |      2       |     2      |         100.0          |
|   87    |      2       |     2      |         100.0          |
|   88    |      2       |     2      |         100.0          |
|   89    |      2       |     2      |         100.0          |
|   90    |      0       |     2      |          0.0           |
|   91    |      2       |     2      |         100.0          |
|   92    |      2       |     2      |         100.0          |
|   93    |      0       |     2      |          0.0           |
|   94    |      2       |     2      |         100.0          |
|   95    |      0       |     2      |          0.0           |
|   96    |      2       |     2      |         100.0          |
|   97    |      0       |     2      |          0.0           |
|   98    |      2       |     2      |         100.0          |
|   99    |      0       |     2      |          0.0           |
|   100   |      2       |     2      |         100.0          |
+---------+--------------+------------+------------------------+
```

```
(llmbench-env) MacBook-Pro:LLMbench fab$ more results.json
[
    {
        "test_id": "1",
        "iteration": 1,
        "question": "42216 + 20801",
        "correct": false,
        "received_answer": "62017",
        "final_answer": 62017,
        "correct_answer": 63017
    },
    {
        "test_id": "1",
        "iteration": 2,
        "question": "42216 + 20801",
        "correct": false,
        "received_answer": "62017",
        "final_answer": 62017,
        "correct_answer": 63017
    },
    {
        "test_id": "2",
        "iteration": 1,
        "question": "76138 + 50572",
        "correct": true,
        "received_answer": "126710",
        "final_answer": 126710,
        "correct_answer": 126710
    },
    {
        "test_id": "2",
        "iteration": 2,
        "question": "76138 + 50572",
        "correct": true,
        "received_answer": "126710",
        "final_answer": 126710,
        "correct_answer": 126710
    },

[...]

```
