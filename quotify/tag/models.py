from sqlalchemy import (
    Column,
    Integer,
    String,
)
from ..settings.database import Base

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(30),unique=True,nullable=False)
    quotes=relationship('Quote',secondary='quote_tags',back_populates='tags')

metadata= Base.metadata
