# functions.py — функції для роботи зі списком завдань
import json
import os

FOLDER = "data"
FILEPATH = "data/tasks.json"


def load_tasks():
    """Читає завдання з файлу. Якщо файлу немає або він пошкоджений — повертає порожній список."""
    if not os.path.exists(FILEPATH):
        return []
    try:
        with open(FILEPATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, ValueError):
        print("Помилка: файл JSON пошкоджений або порожній. Створюємо новий список.")
        return []


def save_tasks(tasks):
    """Записує список завдань у файл JSON."""
    os.makedirs(FOLDER, exist_ok=True)  # створюємо папку data, якщо її немає
    with open(FILEPATH, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def check_number(number_text, tasks):
    """Перевіряє номер завдання. Повертає число або None, якщо номер поганий."""
    if not number_text.isdigit():
        print("Помилка: номер має бути цілим числом.")
        return None
    number = int(number_text)
    if number < 1 or number > len(tasks):
        print("Помилка: завдання з таким номером немає.")
        return None
    return number


def add_task(text):
    """Додає нове завдання."""
    text = text.strip()  # Видаляємо зайві пробіли на початку та в кінці
    if text == "":
        print("Помилка: текст завдання не може бути порожнім.")
        return
    tasks = load_tasks()
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print("Завдання додано.")


def show_tasks():
    """Показує всі завдання."""
    tasks = load_tasks()
    if len(tasks) == 0:
        print("Список порожній.")
        return
    number = 1
    for task in tasks:
        if task["done"]:
            mark = "[x]"
        else:
            mark = "[ ]"
        print(number, mark, task["text"])
        number += 1


def edit_task(number_text, new_text):
    """Змінює текст завдання."""
    tasks = load_tasks()
    number = check_number(number_text, tasks)
    if number is None:
        return
    new_text = new_text.strip()  # Видаляємо зайві пробіли з нового тексту
    if new_text == "":
        print("Помилка: новий текст не може бути порожнім.")
        return
    tasks[number - 1]["text"] = new_text
    save_tasks(tasks)
    print("Завдання змінено.")


def done_task(number_text):
    """Позначає завдання виконаним."""
    tasks = load_tasks()
    number = check_number(number_text, tasks)
    if number is None:
        return
    tasks[number - 1]["done"] = True
    save_tasks(tasks)
    print("Завдання виконано.")


def delete_task(number_text):
    """Видаляє завдання."""
    tasks = load_tasks()
    number = check_number(number_text, tasks)
    if number is None:
        return
    tasks.pop(number - 1)
    save_tasks(tasks)
    print("Завдання видалено.")