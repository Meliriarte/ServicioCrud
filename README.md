# CrudServicio 🚀

Una API REST completa para la gestión de usuarios desarrollada con Flask. Este proyecto implementa todas las operaciones CRUD (Create, Read, Update, Delete) con una interfaz web moderna y atractiva.

## 🌟 Características

- ✅ **API REST completa** con operaciones CRUD
- 🎨 **Interfaz web moderna** y responsive
- 📱 **Diseño adaptativo** para móviles y escritorio
- 🔄 **Operaciones en tiempo real**
- 📊 **Dashboard con estadísticas**
- 🎯 **Fácil de usar y desplegar**

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask 3.0.3
- **Frontend**: HTML5, CSS3, JavaScript
- **Servidor**: Gunicorn 23.0.0
- **Despliegue**: Render
- **Iconos**: Font Awesome 6.0

## 📋 Requisitos

- Python 3.8+
- Flask 3.0.3
- Gunicorn 23.0.0
- Requests 2.32.0

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio
\`\`\`bash
git clone <url-del-repositorio>
cd CrudServicio
\`\`\`

### 2. Crear entorno virtual
\`\`\`bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\\Scripts\\activate
\`\`\`

### 3. Instalar dependencias
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Ejecutar la aplicación
\`\`\`bash
python app.py
\`\`\`

La aplicación estará disponible en \`http://localhost:5000\`

## 📚 Documentación de la API

### Base URL
\`\`\`
https://tu-app.onrender.com
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
    "email": "juan@email.com",
    "edad": 30,
    "ciudad": "Madrid"
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
    "email": "juan@email.com",
    "edad": 30,
    "ciudad": "Madrid"
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

## 🎯 Ejemplos de Uso

### Usando cURL

**Crear un usuario**:
\`\`\`bash
curl -X POST https://tu-app.onrender.com/usuarios \\
  -H "Content-Type: application/json" \\
  -d '{
    "nombre": "Ana García",
    "email": "ana@email.com",
    "edad": 25,
    "telefono": "+34 123 456 789"
  }'
\`\`\`

**Obtener un usuario**:
\`\`\`bash
curl https://tu-app.onrender.com/usuarios/1
\`\`\`

**Actualizar un usuario**:
\`\`\`bash
curl -X PUT https://tu-app.onrender.com/usuarios/1 \\
  -H "Content-Type: application/json" \\
  -d '{"edad": 26}'
\`\`\`

**Eliminar un usuario**:
\`\`\`bash
curl -X DELETE https://tu-app.onrender.com/usuarios/1
\`\`\`

### Usando Python

\`\`\`python
import requests

# URL base de tu API
BASE_URL = "https://tu-app.onrender.com"

# Crear usuario
nuevo_usuario = {
    "nombre": "Carlos López",
    "email": "carlos@email.com",
    "edad": 28,
    "ciudad": "Barcelona"
}

response = requests.post(f"{BASE_URL}/usuarios", json=nuevo_usuario)
print(response.json())

# Obtener usuario
user_id = 1
response = requests.get(f"{BASE_URL}/usuarios/{user_id}")
print(response.json())
\`\`\`

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

## 🎨 Características de la Interfaz

- **Diseño moderno** con gradientes y sombras
- **Cards responsivas** para cada usuario
- **Iconos intuitivos** para diferentes tipos de datos
- **Estadísticas en tiempo real** del número de usuarios
- **Información de la API** integrada en la vista
- **Adaptable a móviles** y tablets

## 🔧 Personalización

### Agregar nuevos campos
Para agregar nuevos campos a los usuarios, simplemente inclúyelos en el JSON al crear usuarios. La interfaz se adaptará automáticamente.

### Modificar estilos
Los estilos CSS están incluidos en el archivo \`usuarios.html\` y pueden modificarse fácilmente.

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (\`git checkout -b feature/AmazingFeature\`)
3. Commit tus cambios (\`git commit -m 'Add some AmazingFeature'\`)
4. Push a la rama (\`git push origin feature/AmazingFeature\`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo \`LICENSE\` para más detalles.

## 📞 Contacto

- **Desarrollador**: Tu Nombre
- **Email**: tu-email@ejemplo.com
- **Proyecto**: [https://github.com/tu-usuario/CrudServicio](https://github.com/tu-usuario/CrudServicio)

## 🙏 Agradecimientos

- Flask por el excelente framework web
- Font Awesome por los iconos
- Render por el hosting gratuito
- La comunidad de Python por el apoyo continuo

---

⭐ **¡No olvides dar una estrella al proyecto si te ha sido útil!** ⭐
\`\`\`

## 📊 Estado del Proyecto

![Estado](https://img.shields.io/badge/Estado-Activo-brightgreen)
![Versión](https://img.shields.io/badge/Versión-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)
![Flask](https://img.shields.io/badge/Flask-3.0.3-red)
