# Guía completa sobre cómo usar Pydantic

# 1. Instalación de Pydantic
# Para comenzar a usar Pydantic, primero debes instalarlo. Puedes hacerlo con pip:
# pip install pydantic

# 2. Definición de Modelos Básicos
# Pydantic se basa en la definición de modelos usando `BaseModel`. Aquí te muestro cómo definir y usar un modelo básico:
from pydantic import BaseModel

# Definir un modelo de usuario
class User(BaseModel):
    name: str
    age: int

# Crear una instancia del modelo
user = User(name="Alice", age=30)

# Acceder a los datos
print(user.name)  # Alice
print(user.age)   # 30

# 3. Validación Automática
# Pydantic realiza validación automática basada en los tipos de datos definidos en el modelo:
from pydantic import ValidationError

class User(BaseModel):
    name: str
    age: int

# Crear una instancia con datos válidos
user = User(name="Bob", age=25)

# Intentar crear una instancia con datos inválidos
try:
    user = User(name="Charlie", age="invalid_age")
except ValidationError as e:
    print(e)

# 4. Modelos Anidados
# Puedes usar modelos anidados para estructuras de datos más complejas:
from typing import List

class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    address: Address
    friends: List[str]

# Crear una instancia con datos anidados
user = User(
    name="David",
    address=Address(city="New York", country="USA"),
    friends=["Alice", "Bob"]
)

print(user.address.city)  # New York

# 5. Valores Predeterminados y Opcionales
# Puedes establecer valores predeterminados y hacer que ciertos campos sean opcionales:
from pydantic import Field
from typing import Optional

class User(BaseModel):
    name: str
    age: Optional[int] = None
    email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')

# Crear una instancia con valores predeterminados y opcionales
user = User(name="Eve", email="eve@example.com")

print(user.age)  # None

# 6. Métodos de Configuración
# Pydantic permite configurar el comportamiento del modelo mediante la clase `Config`:
class User(BaseModel):
    name: str
    age: int

    class Config:
        min_anystr_length = 1  # Establece la longitud mínima para cualquier cadena

# Crear una instancia
user = User(name="Frank", age=40)

# 7. Validaciones Personalizadas
# Puedes agregar validaciones personalizadas usando métodos de clase y el decorador `@validator`:
from pydantic import validator

class User(BaseModel):
    name: str
    age: int

    @validator('age')
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Age must be positive')
        return v

# Intentar crear una instancia con una edad no válida
try:
    user = User(name="Grace", age=-5)
except ValidationError as e:
    print(e)

# 8. Serialización y Deserialización
# Pydantic facilita la conversión entre modelos y datos en formato JSON:
import json

class User(BaseModel):
    name: str
    age: int

# Crear una instancia
user = User(name="Hannah", age=22)

# Convertir a JSON
user_json = user.json()
print(user_json)

# Convertir de JSON a modelo
user_data = json.loads(user_json)
user_from_json = User(**user_data)
print(user_from_json)

# 9. Documentación y Recursos Adicionales
# Para obtener información más detallada y recursos adicionales, visita la documentación oficial de Pydantic:
# - Documentación Oficial: https://pydantic-docs.helpmanual.io/
# - GitHub Repository: https://github.com/pydantic/pydantic

# Pydantic es una herramienta poderosa para la validación de datos y el manejo de configuraciones en Python,
# y su documentación oficial proporciona una gran cantidad de ejemplos y explicaciones detalladas para ayudarte a sacar el máximo provecho de ella.
