from pydantic import BaseModel

# Что мы ждем от пользователя при создании
class GameCreate(BaseModel):
    title: str
    platform: str
    year: int
    rating: float = 0.0

# Что мы отдаем пользователю (с ID)
class GameResponse(GameCreate):
    id: int

    class Config:
        from_attributes = True # Позволяет Pydantic работать с моделями SQLAlchemy