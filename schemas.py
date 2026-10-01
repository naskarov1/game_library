from pydantic import BaseModel

class GameCreate(BaseModel):
    title: str
    platform: str
    year: int
    rating: float = 0.0
class GameResponse(GameCreate):
    id: int

    class Config:
        from_attributes = True