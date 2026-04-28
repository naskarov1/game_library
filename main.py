from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

# Создаем таблицы в БД (для начала пойдет, но в будущем лучше Alembic)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Game Library API")

@app.post("/games/", response_model=schemas.GameResponse)
def create_game(game: schemas.GameCreate, db: Session = Depends(database.get_db)):
    db_game = models.Game(**game.model_dump())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

@app.get("/games/", response_model=list[schemas.GameResponse])
def read_games(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    games = db.query(models.Game).offset(skip).limit(limit).all()
    return games

@app.get("/games/{game_id}", response_model=schemas.GameResponse)
def read_game(game_id: int, db: Session = Depends(database.get_db)):
    game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if game is None:
        raise HTTPException(status_code=404, detail="Игра не найдена")
    return game