from fastapi import FastAPI,APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
import sys
sys.path.append("..")
from database import get_db
import models,schemas,utils,oauth2,database
router=APIRouter()
@router.get("/students",tags=["Students"])
def getallstudents(db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    students=db.query(models.Students).all()
    return students
@router.get("/students/{id}",tags=["Students"])
def getonestudent(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    students=db.query(models.Students).filter(models.Students.id==id).first()
    if not students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The student with id:{id} not found")
    return students
@router.post("/students",tags=["Students"])
def createstudent(student:schemas.createstudent,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    new_student=models.Students(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
@router.put("/students/{id}",tags=["Students"])
def update_student(id:int,student:schemas.createstudent,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    updatestudent=db.query(models.Students).filter(models.Students.id==id)
    up_student=updatestudent.first()
    if up_student==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The post with id:{id} not found")
    updatestudent.update(student.dict(),synchronize_session=False)
    db.commit()
    updatestudent=db.query(models.Students).filter(models.Students.id==id).first()
    return {"updated student":updatestudent}
@router.delete("/students/{id}",tags=["Students"])
def delete_student(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    deletestudent=db.query(models.Students).filter(models.Students.id==id)
    if deletestudent.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The post with id:{id} not found")
    deletestudent.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)