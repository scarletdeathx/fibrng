# fibrng11.py
import json
import random

def read_words_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def fibonacci_words(word_list, n):
    a, b = 0, 1
    total_words = 0
    while total_words < n:
        selected_words = random.sample(word_list, b)
        print(", ".join(selected_words))
        total_words += b
        a, b = b, a + b

if __name__ == "__main__":
    word_list = read_words_from_json('wordlist.json')
    fibonacci_words(word_list, 232)
