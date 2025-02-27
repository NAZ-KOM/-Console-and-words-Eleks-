import sys
from collections import Counter
import re


def count_word_frequency(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = re.findall(r'\b\w+\b', text)
            word_counts = Counter(words)

            sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

            for word, count in sorted_words:
                print(f"{word}: {count}")
    except FileNotFoundError:
        print("Файл не знайдено!")
    except Exception as e:
        print(f"Сталася помилка: {e}")


if __name__ == "__main__":
    file_path = input("Введіть шлях до файлу: ")
    count_word_frequency(file_path)
