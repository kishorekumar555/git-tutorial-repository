from database import Base
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
class Students(Base):
    __tablename__="Students"
    id=Column(Integer,primary_key=True)
    Name=Column(String,nullable=False)
    Class=Column(String,nullable=False)
    English_marks=Column(Integer,nullable=False)
    Tamil_marks=Column(Integer,nullable=False)
    Maths_marks=Column(Integer,nullable=False)
    Science_marks=Column(Integer,nullable=False)
    Social_marks=Column(Integer,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),server_default=text('now()'),nullable=False)
class Teachers(Base):
    __tablename__="Faculty"
    id=Column(Integer,primary_key=True)
    Username=Column(String,nullable=False,unique=True)
    Password=Column(String,nullable=False)
    is_class_teacher=Column(String,nullable=False,server_default='FALSE')
    is_HM=Column(Boolean,nullable=False,server_default='FALSE')
    Department=Column(String,nullable=False)

