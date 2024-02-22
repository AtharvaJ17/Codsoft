class Task:
    def __init__(self, name ):
        self.name = name
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, name):
        self.tasks.append(Task(name))
    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}.  {task.name}")
    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]

def main():
    task_manager = TaskManager()
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Delete Task\n4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            task_manager.add_task(task_name)
        elif choice == '2':
            task_manager.list_tasks()

        elif choice == '3':
            index = int(input("Enter task index to delete: "))
            task_manager.delete_task(index)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
