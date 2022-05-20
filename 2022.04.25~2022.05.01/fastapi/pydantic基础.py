from pydoc import doc
from typing import List,Optional
from pydantic import BaseModel,ValidationError,constr
from datetime import datetime
from typing import List
from requests import patch
from sympy import Domain, public
from tomlkit import date
from wechaty import Friendship
from sqlalchemy import Column,Integer,String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path

class User(BaseModel):
    id:int  # 必填字段
    name:str = "John Snow"    # 有默认值，选填字段
    signup_ts:Optional[datetime] = None
    friends:List[int] = []  # 列表中元素是int类型或者可以转换成int类型

external_data = {
    "id":"123",
    "signup_ts":"2022-12-22 12:22",
    "friends":[1,2,"3"] # "3"是可以int("3")的
}
user = User(**external_data)
print(user.id,user.friends) # 实例后调用属性
print(repr(user.signup_ts))
print(user.dict())

#校验失败处理
try:
    User(id=1,signup_ts=datetime.today(),friends=[1,2,"not number"])
except ValidationError as e:
    print(e.json())

# 模型的属性和方法
print(user.dict())
print(user.json())
print(user.copy())  # 这里是浅copy
print(User.parse_obj(obj=external_data))
print(User.parse_raw('{"id": 123, "name": "John Snow", "signup_ts": "2022-12-22T12:22:00", "friends": [1, 2, 3]}'))

path = Path('pydantic_tutorial.json')
path.write_text('{"id": 123, "name": "John Snow", "signup_ts": "2022-12-22T12:22:00", "friends": [1, 2, 3]}')
print(User.parse_file(path))

print(user.schema())
print(user.schema_json())

# 不校验数据直接创建模型类，不建议在construct方法中传入未校验的数据
user_date = {"id": 123, "name": "John Snow", "signup_ts": "2022-12-22T12:22:00", "friends": [1, 2, 3]}
print(User.construct(**user_date))

# 定义模型类的时候，所以字段都注明类型，字段就不会乱
print(User.__fields__.keys())

# 递归模型
class Sound(BaseModel):
    sound: str

class Dog(BaseModel):
    birthday: date
    weight: float = Optional[None]
    # 不同的狗不同的叫声。递归模型就是一个嵌套一个
    sound: List[Sound]

dogs = Dog(birthday=date.today(), weight=6.66, sound=[{"sound":"wang wang ~"},{"sound":"ying ying ~"}])

print(dogs.dict())

#ORM模型：从类实例创建符合ORM对象的模型
Base = declarative_base()
class CompanyOrm(Base):
    __tablename__ = 'companies'
    id = Column(Integer,primary_key=True,nullable=False)
    public_key = Column(String(20),index=True,nullable=False,uniqe=True)
    name  = Column(String(63),uniqe=True)
    Domains = Column(ARRAY(String(255)))

class ComoanyMode(BaseModel):
    id:int
    public_key = constr(max_length=20)
    name:constr(max_length=63)
    Domains:List[constr(max_length=255)]
    
    class Config:
        orm_mode = True

co_orm = CompanyOrm(
    id=123,
    public_key='foobar',
    name='Testing',
    Domains=['example.com']
)


print(ComoanyMode.from_orm(co_orm))