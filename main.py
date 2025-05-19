class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        # Проверяем, нет ли уже такой задачи
        if any(t["description"] == task for t in self.tasks):
            print(f"Задача '{task}' уже существует.")
            return
        self.tasks.append({"description": task, "completed": False})

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
            print(f"Удалено {removed_count} задач с названием '{task}'.")

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        print("\nСписок задач:")
        for idx, t in enumerate(self.tasks, start=1):
            status = "[x]" if t["completed"] else "[ ]"
            print(f"{idx}. {status} {t['description']}")
