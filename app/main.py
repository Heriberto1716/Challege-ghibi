from fastapi import FastAPI, HTTPException
from app.models import Usuario
from app.database import usuarios_db
from app.utils import obtener_datos_ghibli_por_rol
import uuid

app = FastAPI(title="API de Usuarios y Ghibli")

@app.post("/usuarios")
def crear_usuario(datos_usuario: Usuario):
    id_unico = str(uuid.uuid4())
    usuarios_db[id_unico] = datos_usuario.dict()
    return {"id": id_unico, "usuario": datos_usuario}

@app.get("/usuarios")
def obtener_todos_usuarios():
    return usuarios_db

@app.get("/usuarios/{usuario_id}")
def obtener_usuario_por_id(usuario_id: str):
    if usuario_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuarios_db[usuario_id]

@app.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: str, datos_actualizados: Usuario):
    if usuario_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuarios_db[usuario_id] = datos_actualizados.dict()
    return {"id": usuario_id, "usuario": datos_actualizados}

@app.delete("/usuarios/{usuario_id}")
def borrar_usuario(usuario_id: str):
    if usuario_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    del usuarios_db[usuario_id]
    return {"mensaje": f"Usuario con id {usuario_id} borrado correctamente"}

@app.get("/usuarios/{usuario_id}/ghibli")
def consumir_datos_ghibli(usuario_id: str):
    if usuario_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    rol_usuario = usuarios_db[usuario_id]["rol"]
    return obtener_datos_ghibli_por_rol(rol_usuario)
