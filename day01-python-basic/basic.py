name = "Leeon"
age = 28
is_developer = True

print(name)
print(age)
print(is_developer)

name = "Leeon"           # str
age = 28                 # int
price = 19.99            # float
is_active = True         # bool
value = None             # None

print(type(name))
print(type(age))

skills = [
    "JavaScript",
    "React",
    "Python",
]
# 添加
skills.append('test01') 
# 移除
skills.remove('React')
# 获取长度
print(len(skills))

if "Python" in skills:
    print ('xuexi中')

print(skills)
print(skills[0])
print(skills[1])
print(skills[2])


user = {
    "name": "Leeon",
    "age": 28,
    "skills": ["React", "Python"],
}

print(user);
user["age"]= 30
user['city'] = 'chengdu'
print(user);

city = user.get("city")
country = user.get("country", "jinniu")
print(city)
print(country)


age = 28

if age >= 18:
    print("成年")
else:
    print("未成年")


skills = ["React", "Python", "FastAPI"]

for skill in skills:
    print(skill)

# 遍历 enumerate 把列表变成 "带序号" 的枚举对象，每一项是 (索引, 元素) 元组
for index, skill in enumerate(skills, start=0):
    print(index, skill)

def add(a, b):
    return a + b

res = add(10,20);
print(res) 

# 函数简写  def定义函数的关键字（define 的缩写）
def add1(a:int,b:int)-> int:
    return a + b;
newres = add1(11,23);
print(newres)

name = "Python"
day = 1

print(f"今天是 FDE 第 {day} 天，正在学习 {name}")

name = input("请输入你的名字：")

print(f"你好，{name}")

age = int(input("请输入年龄："))

print(type(age))