class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if any(t["description"] == task for t in self.tasks):
            print(f"Задача '{task}' уже существует.")
            return
        self.tasks.append({"description": task, "completed": False})
        print(f"Задача '{task}' добавлена.")

    def complete_task(self, task):
        found = False
        for t in self.tasks:
            if t["description"] == task:
                if t["completed"]:
                    print(f"Задача '{task}' уже выполнена.")
                else:
                    t["completed"] = True
                    print(f"Задача '{task}' отмечена как выполненная.")
                found = True
                break
        if not found:
            print(f"Задача '{task}' не найдена.")

    def remove_task(self, task):
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["description"] != task]
        removed_count = initial_count - len(self.tasks)

        if removed_count == 0:
            print(f"Задача '{task}' не найдена.")
        elif removed_count == 1:
            print(f"Задача '{task}' удалена.")
        else:
            print(f"Удалено {removed_count} задач(и) с названием '{task}'.")

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        print("\nСписок задач:")
        for idx, t in enumerate(self.tasks, start=1):
            status = "[x]" if t["completed"] else "[ ]"
            print(f"{idx}. {status} {t['description']}")
        print()


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


if __name__ == "__main__":
    main()
