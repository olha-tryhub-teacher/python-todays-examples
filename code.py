# ----- User Schemas -----

# Базова схема користувача, містить тільки логін
class UserBase(BaseModel):
    login: str

# Схема для роботи з БД, містить логін і пароль
class UserDB(UserBase):
    password: str

# Схема для створення нового користувача через API
class UserCreate(UserBase):
    password: str

# Схема для відповіді API, включає id користувача
class User(UserBase):
    id: int
    # Дозволяє створювати Pydantic-модель із об'єктів ORM
    class Config:
        from_attributes = True
