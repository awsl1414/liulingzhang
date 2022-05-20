
from fastapi import FastAPI,Header,Body,Form

app = FastAPI()

# @app.get("/user/{id}")
# def user(id):
#     return {"id":id}

#通过header传递参数
@app.get("/user")
def user(id,token=Header(None)):
    return {"id":id,"token":token}

# @app.post("/login")
# def login(data=Body(None)):
#     return {"data":data}

#通过form-data传递参数
@app.post("/login")
def login(username=Form(None),password=Form(None)):
    return {"data":{"username":username,"password":password}}
