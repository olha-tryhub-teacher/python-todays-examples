# ----- User -----
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login).first()


def authenticate_user(db: Session, login: str, password: str):
    user = get_user(db, login)
    if not user:
        return False
    # додаємо сіль перед перевіркою
    if not verify_password(password + user.salt, user.password):
        return False
    return user


def create_user(db: Session, login: str, password: str):
    salt = secrets.token_hex(16)
    hashed_password = get_password_hash(password + salt)

    db_user = models.User(
        login=login,
        password=hashed_password,  # тут зберігається саме hash
        salt=salt,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
