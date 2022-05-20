#导入fastapi
from fastapi import FastAPI
#建立api实例
app = FastAPI()
#定义一个路径操作装饰器
@app.get("/")
#定义路径操作函数
async def root():
    #返回内容
    return {"key":"value"}