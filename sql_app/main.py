from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/jobs", response_model=List[schemas.Job])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jobs = crud.get_jobs(db, skip=skip, limit=limit)
    return jobs

@app.get("/job/{id}", response_model=schemas.Job)
def read_job(id: int, db: Session = Depends(get_db)):
    db_job = crud.get_job(db, JobId=id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

@app.post("/jobs", response_model=schemas.Result)
def create_job(Job: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db=db, Job=Job)

@app.put("/jobs", response_model=schemas.Result)
def update_job(Job: schemas.JobUpdate, db: Session = Depends(get_db)):
    return crud.update_job(db=db, Job=Job)

@app.delete("/jobs/{id}", response_model=schemas.Result)
def delete_job(id: int, db: Session = Depends(get_db)):
    return crud.delete_job(db=db, JobId=id)

@app.post("/job/{id}/apply", response_model=schemas.Result)
def apply_job(id: int, db: Session = Depends(get_db)):
    Job = schemas.JobApply
    Job.JobId = id
    Job.ApplyStatus = "True"
    return crud.apply_job(db=db, Job=Job)
