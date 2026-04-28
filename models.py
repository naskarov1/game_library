from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    platform = Column(String)
    year = Column(Integer)
    rating = Column(Float, default=0.0)