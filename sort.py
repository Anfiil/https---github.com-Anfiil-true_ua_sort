import string
import re # Бібліотека для регулярних виразів

# Функція для зчитування тексту з файлу
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return None
    except IOError:
        print("Помилка: проблеми з читанням файлу.")
        return None

# Функція для отримання першого речення
def get_first_sentence(text):
    # Розбиваємо текст на речення
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences[0] if sentences else ""

# Функція для сортування слів по українським та латинським літерам
def custom_sort_key(word):
    ukr_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    word = word.lower()
    
    # Словник для українських та латинських літер 
    ukr_order = {char: idx for idx, char in enumerate(ukr_alphabet)}
    eng_order = {char: idx for idx, char in enumerate(eng_alphabet)}
    
    # Сортування: українські літери раніше, англійські пізніше
    sorted_word = []
    for char in word:
        if char in ukr_order:
            sorted_word.append((0, ukr_order[char]))  # Українські літери
        elif char in eng_order:
            sorted_word.append((1, eng_order[char]))  # Англійські літери
        else:
            sorted_word.append((2, char))  # Інші символи (якщо є)
    
    return sorted_word

# Функція для сортування слів за алфавітом
def sort_words(text):
    # Видаляємо знаки пунктуації
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Розбиваємо на слова
    words = text.split()
    
    # Сортуємо слова за допомогою кастомного ключа
    words.sort(key=custom_sort_key)
    
    return words

# Головна функція
def main():
    file_path = "text.txt"  # Шлях до вашого файлу

    text = read_file(file_path)
    if text is None:
        return
    
    # Виведення першого речення
    first_sentence = get_first_sentence(text)
    print("Перше речення:", first_sentence)
    
    # Отримання та сортування слів
    sorted_words = sort_words(text)
    
    # Виведення відсортованих слів
    print("Відсортовані слова:", sorted_words)
    
    # Виведення кількості слів
    print("Кількість слів:", len(sorted_words))

if __name__ == "__main__":
    main()

