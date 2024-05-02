from fastapi import FastAPI,Response,HTTPException,status,APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import sys
sys.path.append("..")
from database import get_db
import models,schemas,utils,oauth2
router=APIRouter()
@router.post('/login',response_model=schemas.Token,tags=["Login Authorization"])
def userlogin(user_credential:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.Teachers).filter(models.Teachers.Username==user_credential.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    if not utils.verify(user_credential.password,user.Password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token":access_token,"token_type":"bearer"}

