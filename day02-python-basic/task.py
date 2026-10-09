class User:
    def __init__(self,name:str,age:int):
        self.name:str = name
        self.age:int= age

    def introduce(self)->None:
        print(f'大家好，我叫 {self.name}，今年 {self.age} 岁。')
        

user = User('Leeon','28')
user.introduce()
print(user.name)
print(user.age)


class Product:
    def __init__(self,name,price,num):
        self.name:str = name
        self.price:float = price
        self.num:int = num
    def buy(self,count:int)->None:
        if count > self.num:
            print('库存不够了')
            return
        self.num = self.num - count
        print(f'购买成功：{self.name}-{count}')
        print(f'还有库存：{self.num}')

product = Product('书',19.9,20)
product.buy(10)