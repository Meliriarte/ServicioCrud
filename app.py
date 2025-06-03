from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route('/')
def index():
    return 'Bienvenidos a mi primera aplicación Flask!'

@app.route('/usuarios', methods=['POST'])
def Crear_usuario():
    nuevo_usuario = request.get_json()
    nuevo_usuario['id'] = len(usuarios) + 1
    usuarios.append(nuevo_usuario)
    return jsonify({"Mensaje": "Usuario creado exitosamente", "Usuario": nuevo_usuario}), 201

@app.route('/usuarios', methods=['GET'])
def Obtener_usuarios():
    return jsonify({"Usuarios": usuarios})

@app.route('/usuarios/<int:id>', methods=['GET'])
def Obtener_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        return jsonify({"Usuario": usuario})
    else:
        return jsonify({"Mensaje": "Usuario no encontrado"}), 404
    
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        datos = request.get_json()
        usuario.update(datos)
        return jsonify({"Mensaje": "Usuario actualizado exitosamente", "Usuario": usuario})
    else:
        return jsonify({"Mensaje": "Usuario no encontrado"}), 404

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        usuarios.remove(usuario)
        return jsonify({"Mensaje": "Usuario eliminado exitosamente"})
    else:
        return jsonify({"Mensaje": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)