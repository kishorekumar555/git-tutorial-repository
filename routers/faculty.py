from fastapi import FastAPI,APIRouter,Depends,HTTPException,Response,status
from sqlalchemy.orm import Session
from database import get_db
import sys
sys.path.append("..")
from database import get_db
import models,schemas,utils,oauth2
router=APIRouter()
@router.get("/faculties",tags=["Faculties"])
def get_faculties(db:Session=Depends(get_db)):
    faculties=db.query(models.Teachers).all()
    return faculties
@router.get("/faculties/{id}",tags=["Faculties"])
def get_one_faculty(id:int,db:Session=Depends(get_db)):
    one_faculty=db.query(models.Teachers).filter(models.Teachers.id==id).first()
    if not one_faculty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The faculty with id:{id} is not found")
    return one_faculty
@router.post("/faculties",tags=["Faculties"])
def create_faculty(faculty:schemas.teacherlogin,db:Session=Depends(get_db)):
    hashed_password=utils.hash(faculty.Password)
    faculty.Password=hashed_password
    new_faculty=models.Teachers(**faculty.dict())
    db.add(new_faculty)
    db.commit()
    db.refresh(new_faculty)
    return "Faculty account successfully created"
@router.put("/faculties/{id}",tags=["Faculties"])
def update_faculty(id:int,faculty:schemas.teacherlogin,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    hashed_password=utils.hash(faculty.Password)
    faculty.Password=hashed_password
    updatefaculty=db.query(models.Teachers).filter(models.Teachers.id==id)
    up_faculty=updatefaculty.first()
    if updatefaculty == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The faculty with id:{id} is not found")
    updatefaculty.update(faculty.dict(),synchronize_session=False)
    db.commit()
    updatefaculty=db.query(models.Teachers).filter(models.Teachers.id==id).first()
    return "Faculty account successfully updated"
@router.delete("/faculties/{id}",tags=["Faculties"])
def delete_faculty(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    deletefaculty=db.query(models.Teachers).filter(models.Teachers.id==id)
    if deletefaculty.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The faculty with id:{id} is not found")
    deletefaculty.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
