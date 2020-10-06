from sqlalchemy.orm import Session

from . import models, schemas

def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Job).offset(skip).limit(limit).all()

def get_job(db: Session, JobId: int):
    return db.query(models.Job).filter(models.Job.JobId == JobId).first()

def create_job(db: Session, Job: schemas.JobCreate):
    db_job = models.Job(JobName=Job.JobName, CompanyName=Job.CompanyName, Location=Job.Location, ApplyStatus=Job.ApplyStatus)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return schemas.Result(message="Created Successfully")

def update_job(db: Session, Job: schemas.JobUpdate):
    db.query(models.Job).filter(models.Job.JobId == Job.JobId).update({"JobName": Job.JobName, "CompanyName": Job.CompanyName, "Location": Job.Location})
    db.commit()
    return schemas.Result(message="Updated Successfully")

def delete_job(db: Session, JobId: int):
    db_job = db.query(models.Job).filter(models.Job.JobId == JobId).first()
    db.delete(db_job)
    db.commit()
    return schemas.Result(message="Deleted Successfully")

def apply_job(db: Session, Job: schemas.JobApply):
    db.query(models.Job).filter(models.Job.JobId == Job.JobId).update({"ApplyStatus": Job.ApplyStatus})
    db.commit()
    return schemas.Result(message="job applied successfully")