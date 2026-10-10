import asyncio
import time


# async def hello():
#     print("Hello FDE")


# asyncio.run(hello())

# async def learn_python():
#     print("开始学习 Python")

#     await asyncio.sleep(2)

#     print("Python 学习完成")


# asyncio.run(learn_python())

# async def learn_python1():
#     print('111-learn_python1')
#     await asyncio.sleep(2)
#     print('222-learn_python1')


# async def learn_fastapi():
#     print('111-learn_fastapi')
#     await asyncio.sleep(2)
#     print('222-learn_fastapi')



# async def main1():
#     # await learn_python1()
#     # await learn_fastapi()
#     starttime = time.perf_counter()
#     await asyncio.gather(
#         learn_python1(),
#         learn_fastapi()
#     )
#     endtime =  time.perf_counter()
#     # time = endtime - starttime: .2f
#     print(
#         f"耗时：{endtime - starttime:.2f} 秒"  # ⑤ 结束时刻 - 开始时刻 = 运行耗时，保留 2 位小数
#     )

# asyncio.run(main1())



async def ask_ai(question: str) -> str:
    print(
        f"正在向 AI 提问：{question}"
    )
    await asyncio.sleep(2)
    return f"AI 回答：{question}"

async def main():
    questions = [
        "什么是 FDE？",
        "什么是 RAG？",
        "什么是 Agent？",
        "什么是 MCP？"
    ]
    tasks = []
    for question in  questions:
        tasks.append(
            ask_ai(question)
        )
    starttime = time.perf_counter()
    res = await asyncio.gather(
        *tasks
    )
    endtime = time.perf_counter()
    for li  in res:
        print(li)

    print(f"耗时{endtime - starttime:.2f}")
asyncio.run(main())