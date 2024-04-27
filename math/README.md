**Setup**
- Discussion here: [https://www.reddit.com/r/LocalLLaMA/comments/1cdxjax/comment/l1gq754/?context=3](source)
- Model: microsoft/Phi-3-mini-4k-instruct-gguf/Phi-3-mini-4k-instruct-q4.gguf
- Server: LMStudio
- Status: pre-alpha ^_^

```
(llmbench-env) MacBook-Pro:LLMbench fab$ python benchmark.py
Correctness Percentage: 85.00%

(llmbench-env) MacBook-Pro:LLMbench fab$ more results.json

[
    {
        "test_id": "1",
        "question": "54193 + 39540",
        "correct": true,
        "received_answer": "The sum of 54193 and 39540 is:\n\n54193 + 39540 = 93733\n\nSo, the result is 93733.",
        "final_answer": 93733
    },
    {
        "test_id": "2",
        "question": "21313 + 31416",
        "correct": true,
        "received_answer": "The sum of 21313 and 31416 is:\n\n21313\n+31416\n------\n52729\n\nSo, the result is 52729.",
        "final_answer": 52729
    },
    {
        "test_id": "3",
        "question": "65973 + 61556",
        "correct": true,
        "received_answer": "The sum of 65973 and 61556 is 127529.",
        "final_answer": 127529
    },
    {
        "test_id": "4",
        "question": "51299 + 50817",
        "correct": true,
        "received_answer": "The sum of 51299 and 50817 is:\n\n51299 + 50817 = 102116",
        "final_answer": 102116
    },

[...]
```
