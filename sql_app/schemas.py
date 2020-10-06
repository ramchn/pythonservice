from typing import List, Optional

from pydantic import BaseModel

class Result(BaseModel): 
    message: str

class JobBase(BaseModel):
    JobName: str
    CompanyName: str
    Location: str
    ApplyStatus: str

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    JobId: int
    JobName: str
    CompanyName: str
    Location: str

class JobApply(BaseModel):
    JobId: int
    ApplyStatus: str

class Job(JobBase):
    JobId: int
    
    class Config:
        orm_mode = True
