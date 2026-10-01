# Game Library API 

RESTful API для управления библиотекой видеоигр, разработанный с использованием **FastAPI**, **SQLAlchemy** и **Pydantic**. В качестве базы данных используется **SQLite**.

---

##  Технологии

* **Python 3.10+**
* **FastAPI** — веб-фреймворк для создания API
* **SQLAlchemy** — ORM для работы с базой данных
* **Pydantic v2** — валидация данных и сериализация
* **SQLite** — база данных
* **Uvicorn** — ASGI-сервер

---

##  Структура проекта

```text
.
├── main.py           # Точка входа приложения и роуты API
├── models.py         # Модели SQLAlchemy (таблицы БД)
├── schemas.py        # Схемы Pydantic (валидация данных)
├── database.py       # Подключение к БД и сессии
├── requirements.txt  # Зависимости проекта
└── test.db           # Файл базы данных SQLite (создается автоматически)
```

---

##  Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/naskarov1/your-repository-name.git
cd your-repository-name
```

### 2. Настройка виртуального окружения

Создайте и активируйте виртуальное окружение:

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запуск приложения

```bash
uvicorn main:app --reload
```

Приложение будет доступно по адресу: `http://127.0.0.1:8000`

---

##  Документация API (Swagger / ReDoc)

FastAPI автоматически генерирует интерактивную документацию:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Эндпоинты API

| Метод | Эндпоинт | Описание |
|---|---|---|
| `POST` | `/games/` | Добавить новую игру в библиотеку |
| `GET` | `/games/` | Получить список всех игр (с пагинацией `skip`, `limit`) |
| `GET` | `/games/{game_id}` | Получить информацию об игре по её ID |

### Пример тела запроса (POST `/games/`):

```json
{
  "title": "The Witcher 3: Wild Hunt",
  "platform": "PC",
  "year": 2015,
  "rating": 9.8
}
```

### Пример ответа (200 OK):

```json
{
  "id": 1,
  "title": "The Witcher 3: Wild Hunt",
  "platform": "PC",
  "year": 2015,
  "rating": 9.8
}
```