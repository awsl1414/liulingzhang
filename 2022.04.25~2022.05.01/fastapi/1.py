#
from fastapi import FastAPI
import uvicorn
#
app = FastAPI()
#添加首页
@app.get("/")
def index():
    """这是首页"""
    return "this is home pase."

@app.get("/users")
def users():
    return {"msg":"get all users","code":2001}

@app.get("/projects")
def projects():
    return ["1","2","3"]

@app.get("/projects/test")
def test():
    return (1,2,3,4,5)

#发送post请求
# @app.post("/login")
# def login():
#     return {"msg":"success"}

#既支持post请求又支持get请求
@app.api_route("/login",methods=("GET","POST","PUT"))
def login():
    return {"msg":"success"}

#获取url参数





# if __name__ == "__main__":
#     uvicorn.run(app,host = "127.0.0.1",port=8080)