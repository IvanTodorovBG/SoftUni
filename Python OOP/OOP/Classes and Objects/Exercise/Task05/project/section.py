from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for current_task in self.tasks:
            if current_task.name == task_name:
                current_task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for current_task in self.tasks:
            if current_task.completed:
                self.tasks.remove(current_task)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        return f"Section {self.name}:\n" + '\n'.join([x.details() for x in self.tasks])

