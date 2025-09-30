# Challenge Backend - API de Usuarios y Studio Ghibli

Este proyecto es una solución al reto técnico de ingeniería backend.  
La aplicación expone un **API REST** para la gestión de usuarios y permite consumir la **Studio Ghibli API** dependiendo del rol asignado a cada usuario.

## 🚀 Tecnologías usadas
- Python 3.10+
- FastAPI
- Uvicorn
- Requests

## 📂 Estructura del proyecto
```
app/
├── main.py
├── models.py
├── database.py
├── utils.py
```

## ⚙️ Instalación y ejecución

```bash
git clone <repo-url>
cd backend-challenge-ghibli
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Abrir en navegador: http://127.0.0.1:8000/docs

## 📌 Endpoints principales
- POST /usuarios
- GET /usuarios
- GET /usuarios/{id}
- PUT /usuarios/{id}
- DELETE /usuarios/{id}
- GET /usuarios/{id}/ghibli
