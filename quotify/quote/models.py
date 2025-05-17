from sqlalchemy import (
    Boolean,
    Column,
    DECIMAL,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Table,
)
from ..settings.database import Base

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Quote(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    content = Column(Text,nullable=False)
    created_at = Column(DateTime,default=func.now(),nullable=False)
    updated_at=Column(DateTime,nullable=True,onupdate=func.now())
    tags = relationship("Tag",secondary='quote_tags',back_populates="quotes")


quote_tags=Table(
    'quote_tags',
    Base.metadata,
    Column('quote_id',Integer,ForeignKey('quotes.id'),nullable=False),
    Column('tag_id',Integer,ForeignKey('tags.id'),nullable=False)

)

metadata= Base.metadata
