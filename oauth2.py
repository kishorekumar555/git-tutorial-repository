from jose import JWTError
from jose import jwt
from datetime import datetime,timedelta
import schemas,models,database
from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')
SECRET_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
def verify_access_token(token:str,credentials_exception):
    try:
        decode_data=jwt.decode(token,SECRET_KEY,[ALGORITHM])
        id:str=decode_data.get("user_id")
        if id is None:
            raise credentials_exception
        token_data=schemas.TokenData.id=id
    except JWTError:
        raise credentials_exception
    return token_data
def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(database.get_db)):
    credentials_exception=HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Could not validate your account",headers={"WWW-Authenticate":"Bearers"})
    Token=verify_access_token(token,credentials_exception)
    user=db.query(models.Teachers).filter(models.Teachers.id==Token).first()
    return user

    
