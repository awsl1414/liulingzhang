from fastapi import FastAPI,Header,Body,Form

app = FastAPI()

#修改响应状态码
@app.get("/user")
def user():
    return {"msg":"get user"}