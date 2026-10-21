# cli.py — головний файл. Запуск: python cli.py <команда> [аргументи]
import sys
import functions


def run_command(command, arguments):
    """Виконує одну команду. arguments — список слів після команди."""
    if command == "add":
        functions.add_task(" ".join(arguments))
    elif command == "show":
        functions.show_tasks()
    elif command == "edit":
        if len(arguments) == 0:
            print("Помилка: вкажіть номер завдання.")
        else:
            functions.edit_task(arguments[0], " ".join(arguments[1:]))
    elif command == "done":
        if len(arguments) == 0:
            print("Помилка: вкажіть номер завдання.")
        else:
            functions.done_task(arguments[0])
    elif command == "delete":
        if len(arguments) == 0:
            print("Помилка: вкажіть номер завдання.")
        else:
            functions.delete_task(arguments[0])
    else:
        print("Невідома команда. Доступні: add, show, edit, done, delete, exit")


def interactive_mode():
    """Режим, коли користувач вводить команди по одній."""
    print("TaskHub CLI. Команди: add, show, edit, done, delete, exit")
    while True:
        line = input("> ").strip()
        if line == "":
            print("Введіть команду.")
            continue
        words = line.split()
        command = words[0]
        if command == "exit":
            break
        run_command(command, words[1:])
    print("Бувайте!")


def main():
    # sys.argv — список слів, які ввели в терміналі після python
    # python cli.py add Купити молоко  ->  ["cli.py", "add", "Купити", "молоко"]
    if len(sys.argv) > 1:
        run_command(sys.argv[1], sys.argv[2:])
    else:
        interactive_mode()


main()