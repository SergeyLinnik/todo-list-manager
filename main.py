def main():
    todo = ToDoList()

    menu = {
        "1": ("Добавить задачу", lambda: todo.add_task(input("Введите новую задачу: ").strip())),
        "2": ("Выполнить задачу", lambda: todo.complete_task(input("Введите название задачи для выполнения: ").strip())),
        "3": ("Удалить задачу", lambda: todo.remove_task(input("Введите название задачи для удаления: ").strip())),
        "4": ("Показать все задачи", todo.list_tasks),
    }

    while True:
        print("\n===== Меню To-Do List =====")
        for key in sorted(menu.keys()):
            print(f"{key}. {menu[key][0]}")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ").strip()

        if choice == "5":
            print("Выход из программы. До свидания!")
            break

        action = menu.get(choice)
        if action:
            try:
                action[1]()  # Выполняем лямбду
            except Exception as e:
                print(f"Ошибка при выполнении действия: {e}")
        else:
            print("Неверный выбор. Пожалуйста, выберите число от 1 до 5.")

        print("-" * 40)
