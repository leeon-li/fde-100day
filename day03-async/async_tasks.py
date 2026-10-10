import  asyncio
import  time

async def get_user(user_id:int)->dict:
    print('查询用户中')
    await asyncio.sleep(1)
    return {
        "id":user_id,
        "name":'Leeon'
    }

async def get_order(user_id:int)->list[str]:
    print('查询订单中')
    await asyncio.sleep(2)
    return [
        "dingdan1",
        "dingdan2"
    ]

async def search_knowledge():
    print('查询知识库')
    await asyncio.sleep(3)
    return "退款期限为 7 天"

async def ask_ai(
    user: dict,
    orders: list[str],
    knowledge: str
    )-> str:
    print('调用ai')
    await asyncio.sleep(2)
    return (
        f"用户 {user['name']}，"
        f"订单：{orders}，"
        f"政策：{knowledge}"
    )

async def main():
    starttime= time.perf_counter()
    user, orders, knowledge = (
        await asyncio.gather(
            get_user(1),
            get_order(1),
            search_knowledge()
        )
    )
    endtime =  time.perf_counter()
    res = await ask_ai(user,orders,knowledge)
    print("\n最终结果：")
    print(res)
    print(f"{endtime - starttime:.2f}")

asyncio.run(main())