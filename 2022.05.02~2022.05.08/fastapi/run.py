
import uvicorn
from fastapi import FastAPI
from imp import reload
from tutorial import app03,app04,app05,app06

app = FastAPI()

app.include_router(app03,prefix='/l3',tags=['第三章 请求参数和验证'])
app.include_router(app04,prefix='/l4',tags=['第四章 相应处理和FastAPI配置'])
app.include_router(app05,prefix='/l5',tags=['第五章 FastAPI的依赖注入系统'])
# app.include_router(app06,prefix='/l6',tags=[''])

if __name__ == '__main__':
    uvicorn.run('run:app',host='127.0.0.1',port=8000,reload=True,debug=True)