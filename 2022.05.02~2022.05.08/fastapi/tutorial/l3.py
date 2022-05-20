
from doctest import Example
from enum import Enum
from typing import Optional,List
from fastapi import APIRouter,Path,Query
from pydantic import BaseModel,Field

app03 = APIRouter()

# 参数路径和数字验证
@app03.get("/path/parameters")
async def path_params01():
    return {"msg":"this is a message"}

# 函数的顺序就是路由的顺序
@app03.get("/path/{parameters}")
async def path_params01(parameters:str):
    return {"msg":parameters}

class CityNane(str,Enum):
    Beijing = "Beijing China"
    Shanghai = "Shanghai China"

#枚举类型参数
@app03.get("/enum/{city}")
async def latest(city:CityNane):
    if city == CityNane.Shanghai:
        return {"city_name":city,"confirmed":1492,"death":7}
    if city == CityNane.Beijing:
        return {"city_name":city,"confirmed":971,"death":9}
    return {"city_name":city,"latest":"unknown"}

# 传递文件路径
@app03.get("/files/{file_path:path}")
async def filepath(file_path:str):
    return f"The file path is {file_path}"  # python3.6+的新特性

# 长度和正则表达式验证（使用频繁）
@app03.get("/path_/{num}")
async def path_params_validate(
    num:int = Path(...,title="Your number",
                description="不可描述",
                ge=1,le=10)
):
    return num

# 查询参数和字符串验证
def page_limit(page:int = 1,limit:Optional[int] = None):    # 给了默认参数就是选填参数，没给默认值就是必填参数
    if limit:
        return {"page":page,"limit":limit}
    return {"page":page}

# bool类型转换
@app03.get("/query/bool/conversion")
async def type_conversion(param:bool = False):
    return param

# 验证一个字符串
@app03.get("/query/validate")
async def quary_params_validations(
    value:str = Query(...,min_length=8,max_length=16,regex="^a"),
    values:List[str] = Query(default=["v1","v2"],alias="alias_name")
):  # 多个查询参数的列表。参数别名
    return value,values

# 请求体和字段
class CityInfo(BaseModel):
    name:str = Field(...,example="beijing") # example是注解的作用，值不会被验证
    country:str
    country_code:str = None # 给一个默认值
    country_population:int = Field(default=800,title="人口数量",description="国家的人口数量",ge=800)
    
    class Config:
        schema_extra = {
            "example":{
                "name":"shanghai",
                "country":"China",
                "country_code":"CN",
                "country_popolation":1400000000
            }
        }

@app03.post("/request_body/city")
async def city_info(city:CityInfo):
    print(city.name,city.country)
    return city.dict()

# 多参数混合
@app03.put("/request_body/city/{name}")

async def mix_city_info(
    # 路径参数
    name:str,
    # body
    city01:CityInfo,
    city02:CityInfo,    # body是可以定义多个的
    # 查询参数
    confirmed:int = Query(ge=0,description="确诊数",default=0),
    death:int = Query(ge=0,description="死亡数",default=0)
):
    if name =="shanghai":
        return {"shanghai":{"confirmed":confirmed,"death":death}}
    return city01.dict(),city02.dict()