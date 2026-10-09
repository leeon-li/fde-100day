class Task:
    pass

task = Task()
print(task)

class Task:
    def __init__(self, title):
        self.title = title

task1 = Task('py')
task2 = Task('js')

print(task1.title)
print(task2.title)

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

try:
    task_index = int(input("请输入编号："))
except ValueError:
    print("请输入正确数字")
