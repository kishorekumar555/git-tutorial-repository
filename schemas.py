from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
#request model for students
class createstudent(BaseModel):
    Name:str
    Class:str
    English_marks:float
    Tamil_marks:float
    Maths_marks:float
    Science_marks:float
    Social_marks:float
class teacherlogin(BaseModel):
    Username:str
    Password:str
    is_class_teacher:str
    is_HM:Optional[bool]=False
    Department:str
class Token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id:Optional[str]=None
class Userlogin(BaseModel):
    Username:str
    password:str





