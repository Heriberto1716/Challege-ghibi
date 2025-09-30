from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    nombre: str
    correo: EmailStr
    rol: str  # admin, films, people, locations, species, vehicles
