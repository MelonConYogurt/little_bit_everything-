from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)


if __name__ == "__main__":
    contrasena = get_password_hash("admin")
    print(contrasena)