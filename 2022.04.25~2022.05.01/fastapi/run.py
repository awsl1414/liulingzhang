from fastapi import FastAPI
import uvicorn
app = FastAPI()

if __name__=='__main__':
    uvicorn.run('run:app',host='127.0.0.1',port=8000,reload=True,debug=True,woker=1)