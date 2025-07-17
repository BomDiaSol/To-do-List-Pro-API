import datetime
import uuid
from sqlalchemy import Column, DateTime, ForeignKey, String, Enum, UUID, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref

from app.infra.database.base import Base
from app.domain.model.user import User

from enum import Enum as PyEnum

class TaskStatus(PyEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    
class TaskPriority(PyEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Task(Base):
    
    __tablename__ = "task"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey(User.id), nullable=False)
    title = Column(String, nullable = False)
    description = Column(String, nullable = False)
    status = Column(Enum(TaskStatus), nullable = False, default=TaskStatus.PENDING)
    priority = Column(Enum(TaskPriority), nullable= False, default=TaskPriority.LOW)
    due_date = Column(Date, nullable = False)
    tag = Column(String, nullable= True)
    created_at = Column(DateTime, default= datetime.utcnow)
    updated_at = Column(DateTime, default= datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="tasks")