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


def show_menu():
    print("\n===== Меню To-Do List =====")
    print("1. Добавить задачу")
    print("2. Выполнить задачу")
    print("3. Удалить задачу")
    print("4. Показать все задачи")
    print("5. Выйти")


def main():
    todo = ToDoList()

    while True:
        show_menu()
        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            task = input("Введите новую задачу: ").strip()
            if task:
                todo.add_task(task)
            else:
                print("Нельзя добавить пустую задачу.")

        elif choice == "2":
            task = input("Введите название задачи для выполнения: ").strip()
            if task:
                todo.complete_task(task)
            else:
                print("Название задачи не может быть пустым.")

        elif choice == "3":
            task = input("Введите название задачи для удаления: ").strip()
            if task:
                todo.remove_task(task)
            else:
                print("Название задачи не может быть пустым.")

        elif choice == "4":
            todo.list_tasks()

        elif choice == "5":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите число от 1 до 5.")


if __name__ == "__main__":
    main()
