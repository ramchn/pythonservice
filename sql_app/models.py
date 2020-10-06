from sqlalchemy import Column, Integer, String

from .database import Base


class Job(Base):
    __tablename__ = "Jobs"

    JobId = Column(Integer, primary_key=True, index=True)
    JobName = Column(String)
    CompanyName = Column(String)
    Location = Column(String)
    ApplyStatus = Column(String)



