tasks = []


def show_tasks():
    
    print("\n===== TODO LIST =====")
    if len(tasks) == 0:
        print("暂无任务")
        return
    for index,el in enumerate(tasks,start=1):
        print(f"{index}.{el}")
    

def add_task():
    task = input("请输入任务:")
    tasks.append(task)
    print(f"已添加任务：{task}");


def delete_task():
    task_index = int(input("请输入删除的任务:"))
    if type(task_index) == int :
        index = task_index - 1
        if index >= 0 and index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"已删除任务：{deleted_task}")
        else:
            print("任务编号不存在")
    else :
        print("任务编号不符合")
    # for index,el in enumerate(tasks,start=1):
    #     if task == index:
    #         return el;
    # tasks.remove(el)
    # print(f"已删除任务：{el}")

# 展示
def show_menu():
    print("\n===== FDE TODO =====")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 退出")


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
        print("Bye!")
        break

    else:
        print("输入错误，请重新选择")