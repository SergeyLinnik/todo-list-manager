class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"description": task, "completed": False})

    def complete_task(self, task):
        for t in self.tasks:
            if t["description"] == task:
                t["completed"] = True
                return
        print(f"Задача '{task}' не найдена.")

    def remove_task(self, task):
        for i, t in enumerate(self.tasks):
            if t["description"] == task:
                del self.tasks[i]
                return
        print(f"Задача '{task}' не найдена.")

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        for t in self.tasks:
            status = "[x]" if t["completed"] else "[ ]"
            print(f"{status} {t['description']}")
