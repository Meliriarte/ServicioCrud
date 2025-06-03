# CrudServicio 🚀

Una API REST completa para la gestión de usuarios desarrollada con Flask. Este proyecto implementa todas las operaciones CRUD (Create, Read, Update, Delete).

---

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask 3.0.3
- **Frontend**: HTML5, CSS3, JavaScript
- **Servidor**: Gunicorn 23.0.0
- **Despliegue**: Render

---

## 📋 Requisitos

- Python 3.8+
- Flask 3.0.3
- Gunicorn 23.0.0
- Requests 2.32.0

---

## 📚 Documentación de la API

### Base URL
\`\`\`
https://serviciocrud.onrender.com
\`\`\`

### Endpoints Disponibles

#### 1. Crear Usuario
- **Método**: \`POST\`
- **Endpoint**: \`/usuarios\`
- **Content-Type**: \`application/json\`

**Ejemplo de solicitud**:
\`\`\`json
{
  "nombre": "Juan Pérez",
  "email": "juan@email.com",
  "edad": 30,
  "ciudad": "Madrid"
}
\`\`\`

**Respuesta exitosa**:
\`\`\`json
{
  "Mensaje": "Usuario creado exitosamente",
  "Usuario": {
    "id": 1,
    "nombre": "Juan Pérez",
    "edad": 30,
  }
}
\`\`\`

#### 2. Obtener Todos los Usuarios (Vista Web)
- **Método**: \`GET\`
- **Endpoint**: \`/usuarios\`
- **Respuesta**: Página HTML con interfaz visual

#### 3. Obtener Usuario por ID
- **Método**: \`GET\`
- **Endpoint**: \`/usuarios/<id>\`

**Respuesta exitosa**:
\`\`\`json
{
  "Usuario": {
    "id": 1,
    "nombre": "Juan Pérez",
    "edad": 30,
  }
}
\`\`\`

#### 4. Actualizar Usuario
- **Método**: \`PUT\`
- **Endpoint**: \`/usuarios/<id>\`
- **Content-Type**: \`application/json\`

**Ejemplo de solicitud**:
\`\`\`json
{
  "nombre": "Juan Carlos Pérez",
  "edad": 31
}
\`\`\`

#### 5. Eliminar Usuario
- **Método**: \`DELETE\`
- **Endpoint**: \`/usuarios/<id>\`

**Respuesta exitosa**:
\`\`\`json
{
  "Mensaje": "Usuario eliminado exitosamente"
}
\`\`\`

---

## 🎯 Ejemplos de Uso

### Usando cURL

**Crear un usuario**:
\`\`\`bash
curl -X POST https://serviciocrud.onrender.com/usuarios \\
  -H "Content-Type: application/json" \\
  -d '{
    "nombre": "Ana García",
    "edad": 25,
  }'
\`\`\`

**Obtener un usuario**:
\`\`\`bash
curl https://serviciocrud.onrender.com/usuarios/1
\`\`\`

**Actualizar un usuario**:
\`\`\`bash
curl -X PUT https://serviciocrud.onrender.com/usuarios/1 \\
  -H "Content-Type: application/json" \\
  -d '{"edad": 26}'
\`\`\`

**Eliminar un usuario**:
\`\`\`bash
curl -X DELETE https://serviciocrud.onrender.com/usuarios/1
\`\`\`

### Usando Python

\`\`\`python
import requests

# URL base de tu API
BASE_URL = "https://serviciocrud.onrender.com"

# Crear usuario
nuevo_usuario = {
    "nombre": "Carlos López",
    "edad": 28,
}

response = requests.post(f"{BASE_URL}/usuarios", json=nuevo_usuario)
print(response.json())

# Obtener usuario
user_id = 1
response = requests.get(f"{BASE_URL}/usuarios/{user_id}")
print(response.json())
\`\`\`

---

## 🌐 Despliegue en Render

### Configuración automática
El proyecto incluye los archivos necesarios para el despliegue automático en Render:

- \`requirements.txt\`: Dependencias de Python
- \`app.py\`: Aplicación principal

### Pasos para desplegar:

1. **Conectar repositorio** a Render
2. **Configurar el servicio**:
   - Build Command: \`pip install -r requirements.txt\`
   - Start Command: \`gunicorn app:app\`
3. **Desplegar** automáticamente

---

## 📁 Estructura del Proyecto

\`\`\`
CrudServicio/
│
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias Python
├── README.md             # Documentación
└── templates/
    └── usuarios.html     # Interfaz web para usuarios
\`\`\`