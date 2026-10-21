# cli.py — головний файл з диспетчером команд
import sys
import functions


def handle_add(arguments):
    """Обробник команди add."""
    functions.add_task(" ".join(arguments))


def handle_show(arguments):
    """Обробник команди show."""
    functions.show_tasks()


def handle_edit(arguments):
    """Обробник команди edit."""
    if len(arguments) == 0:
        print("Помилка: вкажіть номер завдання.")
    else:
        functions.edit_task(arguments[0], " ".join(arguments[1:]))


def handle_done(arguments):
    """Обробник команди done."""
    if len(arguments) == 0:
        print("Помилка: вкажіть номер завдання.")
    else:
        functions.done_task(arguments[0])


def handle_delete(arguments):
    """Обробник команди delete."""
    if len(arguments) == 0:
        print("Помилка: вкажіть номер завдання.")
    else:
        functions.delete_task(arguments[0])


# СЛОВНИК КОМАНД (Dispatch Table)
# Ключ — назва команди, значення — відповідна функція-обробник
COMMANDS = {
    "add": handle_add,
    "show": handle_show,
    "edit": handle_edit,
    "done": handle_done,
    "delete": handle_delete,
}


def run_command(command, arguments):
    """Диспетчер команд: знаходить потрібну функцію у словнику та викликає її."""
    if command in COMMANDS:
        # Отримуємо функцію зі словника і викликаємо її з аргументами
        handler = COMMANDS[command]
        handler(arguments)
    else:
        available = ", ".join(COMMANDS.keys())
        print(f"Невідома команда. Доступні: {available}, exit")


def interactive_mode():
    """Інтерактивний режим."""
    print("TaskHub CLI. Команди: add, show, edit, done, delete, exit")
    while True:
        line = input("> ").strip()
        if not line:
            continue
        words = line.split()
        command = words[0]
        if command == "exit":
            break
        run_command(command, words[1:])
    print("Бувайте!")


def main():
    if len(sys.argv) > 1:
        run_command(sys.argv[1], sys.argv[2:])
    else:
        interactive_mode()


if __name__ == "__main__":
    main()