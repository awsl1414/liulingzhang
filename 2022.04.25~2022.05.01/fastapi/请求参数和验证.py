
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class CityInfo(BaseModel):
    province:str
    country:str
    is_affected:Optional[bool] = None # 与bool的区别是可以不传，默认值是null

@app.get('/')
async def hello_word():
    return {"hello":"word"}

@app.get('/city/{city}')
async def result(city:str,query_string:Optional[str]=None):
    return {'city':city,'query_string':query_string}

@app.put('city/{city}')
async def reslut(city:str,city_info:CityInfo):
    return {'city':city,'country':city_info.country,'is_affected':city_info.is_affected}