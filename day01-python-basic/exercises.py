name = 'leeon'
age = '28'
city = 'chengdu'
zhiye = '前端开发'

print(f"我叫{name}今年 {age}岁，目前在{city}，从事 {zhiye}。")


skills = [
    "JavaScript",
    "React",
    "Vue",
]
skills.append('Python');
skills.append('FastAPI');
skills.remove('Vue')

for index,el in enumerate(skills,start=0):
    print(index, el)

user = {
    "username": "leeon",
    "role": "developer",
    "active": False,
}
if user.get("active") == True:
    print("用户 leeon 当前处于激活状态")
else :
    print('jingyong')

def calculate_price(price, count):
    return price*count;

res = calculate_price(int(199),int(3))
print(res)

def check_score(score):
    if score>= 90 and score<=100:
        return(f"A");
    if score>= 80 and score<89:
        return(f"B");
    if score>= 60 and score<79:
        return(f"C");
    if score>= 0 and score<59:
        return(f"D");

res1 = check_score(86);
print(res1)