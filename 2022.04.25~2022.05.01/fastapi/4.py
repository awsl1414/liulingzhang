from fastapi import FastAPI
from enum import Enum
app = FastAPI()

#由于路径操作是按顺序依次运行的，你需要确保路径 /users/me 声明在路径 /users/{user_id}之前：否则，/users/{user_id} 的路径还将与 /users/me 相匹配，"认为"自己正在接收一个值为 "me" 的 user_id 参数。
@app.post("/user/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.post("/user/{user_id}")
async def read_user(user_id):
    return {"user_id":user_id}