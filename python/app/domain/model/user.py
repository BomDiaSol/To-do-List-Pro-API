import datetime
import uuid
from sqlalchemy import Column, DateTime, String, Enum, UUID, Date
from sqlalchemy.orm import relationship

from app.infra.database.base import Base

class User(Base):
    
    __tablename__ = "user"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable= False)
    email = Column(String, unique= True, nullable= False)
    password = Column(String, nullable= False)
    created_at = Column(DateTime, default= datetime.utcnow)
    

    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")