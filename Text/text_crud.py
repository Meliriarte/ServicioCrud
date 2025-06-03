import requests

url_base = 'http://127.0.0.1:5000/usuarios'

def crear_usuario(nombre, edad):
    data = {
        'nombre': nombre,
        'edad': edad
    }
    response = requests.post(url_base, json=data)
    print("Crear Usuario:", response.json())

def obtener_usuarios():
    response = requests.get(url_base)
    print(f"Obtener usuarios", response.json())

def obtener_usuario(id):
    response = requests.get(f"{url_base}/{id}")
    print(f"Obtener usuario {id}:", response.json())

def actualizar_usuario(id, nombre, edad):
    data = {
        'nombre': nombre,
        'edad': edad
    }
    response = requests.put(f"{url_base}/{id}", json=data)
    print(f"Actualizar usuario {id}:", response.json())

def eliminar_usuario(id):
    response = requests.delete(f"{url_base}/{id}")
    print(f"Eliminar usuario {id}:", response.json())

if __name__ == '__main__':
    crear_usuario('Juan', 25)
    obtener_usuarios()
    obtener_usuario(1)
    actualizar_usuario(1, 'Juan actaulizado', 26)
    obtener_usuario(1)
    eliminar_usuario(1)
    obtener_usuarios()