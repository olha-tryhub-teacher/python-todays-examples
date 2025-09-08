SECRET_KEY = "super_secret_key"   # краще брати з env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


@app.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Перевіряємо, чи існує користувач
    existing_user = crud.get_user(db, login=user.login)
    if existing_user:
        raise HTTPException(status_code=409, detail="User already exists")

    # Створюємо користувача
    new_user = crud.create_user(db, login=user.login, password=user.password)

    # Повертаємо дані користувача (без пароля)
    return schemas.User(id=new_user.id, login=new_user.login)


@app.post("/token")
async def token_get(
    form_data: OAuth2PasswordRequestForm = Depends(),  # отримує дані з форми логіну (username & password)
    db: Session = Depends(get_db)                       # підключення до бази даних через залежність
):
    # перевіряємо користувача та пароль у БД
    user = crud.authenticate_user(db, login=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    # створюємо JWT токен з терміном дії
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.login},       # "sub" зберігає у токені логін користувача
        expires_delta=access_token_expires
    )

    # повертаємо токен клієнту
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/protected")
async def protected(token: str = Depends(oauth2_scheme),  # отримує токен із заголовка Authorization
                    db: Session = Depends(get_db)):
    try:
        # розшифровуємо токен та отримуємо login користувача
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        login: str = payload.get("sub")
        if login is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    # перевіряємо наявність користувача у БД
    user = crud.get_user(db, login=login)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # повертаємо захищене повідомлення
    return {"msg": f"{user.login}, welcome to the admin panel!"}


# pip install "uvicorn[standard]"
# uvicorn main:app --reload
# main - назва вашого файлу

# pip install python-multipart
# pip install "python-jose[cryptography]"
# pip install "passlib[bcrypt]"

# python-multipart → потрібна для обробки форм у POST-запитах, особливо для OAuth2PasswordRequestForm у FastAPI.
# python-jose[cryptography] → реалізація JWT-токенів (шифрування, підпис, декодування).
# passlib[bcrypt] → для хешування паролів безпечним алгоритмом bcrypt.
