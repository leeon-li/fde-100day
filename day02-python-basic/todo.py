class Task:
    def __init__(self, title: str):
        self.title: str = title
        self.completed: bool = False

    def mark_completed(self) -> None:
        self.completed = True


tasks: list[Task] = []


def show_tasks() -> None:
    print("\n===== TODO LIST =====")

    if len(tasks) == 0:
        print("暂无任务")
        return

    for index, task in enumerate(tasks, start=1):

        if task.completed:
            status = "[x]"
        else:
            status = "[ ]"

        print(f"{index}. {status} {task.title}")


def add_task() -> None:
    title = input("请输入任务：").strip()

    if title == "":
        print("任务内容不能为空")
        return

    task = Task(title)

    tasks.append(task)

    print(f"已添加任务：{task.title}")


def delete_task() -> None:
    if len(tasks) == 0:
        print("暂无任务")
        return

    show_tasks()

    try:
        task_number = int(
            input("请输入删除任务编号：")
        )
    except ValueError:
        print("请输入正确的数字")
        return

    index = task_number - 1

    if 0 <= index < len(tasks):

        deleted_task = tasks.pop(index)

        print(
            f"已删除任务：{deleted_task.title}"
        )

    else:
        print("任务编号不存在")


def complete_task() -> None:
    if len(tasks) == 0:
        print("暂无任务")
        return

    show_tasks()

    try:
        task_number = int(
            input("请输入完成任务编号：")
        )
    except ValueError:
        print("请输入正确的数字")
        return

    index = task_number - 1

    if 0 <= index < len(tasks):

        task = tasks[index]

        task.mark_completed()

        print(
            f"任务已完成：{task.title}"
        )

    else:
        print("任务编号不存在")


def show_menu() -> None:
    print("\n===== FDE TODO =====")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 完成任务")
    print("5. 退出")


while True:

    show_menu()

    choice = input("请选择：")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        complete_task()

    elif choice == "5":
        print("Bye!")
        break

    else:
        print("输入错误，请重新选择")