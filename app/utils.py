import requests
from fastapi import HTTPException

def obtener_datos_ghibli_por_rol(rol: str):
    base_url = "https://ghibliapi.vercel.app"
    rutas_por_rol = {
        "films": "/films",
        "people": "/people",
        "locations": "/locations",
        "species": "/species",
        "vehicles": "/vehicles"
    }

    if rol in rutas_por_rol:
        respuesta = requests.get(base_url + rutas_por_rol[rol])
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            raise HTTPException(status_code=502, detail="Error al consultar la API de Ghibli")
    elif rol == "admin":
        return {"mensaje": "El rol admin puede realizar cualquier acción, pero no consume Ghibli directamente"}
    else:
        raise HTTPException(status_code=400, detail="Rol no reconocido")
