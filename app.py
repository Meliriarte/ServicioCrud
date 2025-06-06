from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Usuarios de ejemplo para demostración
usuarios = [
    {
        'id': 1,
        'nombre': 'Ana García',
        'edad': 28
    },
    {
        'id': 2,
        'nombre': 'Carlos López',
        'edad': 35
    },
    {
        'id': 3,
        'nombre': 'María Rodríguez',
        'edad': 24
    },
    {
        'id': 4,
        'nombre': 'Pedro Martínez',
        'edad': 42
    },
    {
        'id': 5,
        'nombre': 'Laura Sánchez',
        'edad': 31
    }
]

@app.route('/')
def index():
    html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CrudServicio - Gestión de Usuarios</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .header {{
            text-align: center;
            margin-bottom: 40px;
            color: white;
        }}

        .header h1 {{
            font-size: 3rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}

        .header p {{
            font-size: 1.2rem;
            opacity: 0.9;
        }}

        .welcome-card {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
        }}

        .welcome-title {{
            font-size: 2rem;
            color: #333;
            margin-bottom: 15px;
        }}

        .welcome-subtitle {{
            font-size: 1.1rem;
            color: #666;
        }}

        .stats-card {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
        }}

        .stats-number {{
            font-size: 3rem;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }}

        .stats-label {{
            font-size: 1.2rem;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .table-container {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            overflow-x: auto;
        }}

        .table-title {{
            font-size: 1.5rem;
            color: #333;
            margin-bottom: 20px;
            text-align: center;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}

        th, td {{
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}

        th {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        tr:hover {{
            background-color: #f5f5f5;
        }}

        .user-id {{
            font-weight: bold;
            color: #667eea;
        }}

        .user-name {{
            color: #333;
            font-weight: 500;
        }}

        .user-age {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 0.9rem;
            font-weight: 600;
            display: inline-block;
        }}

        .api-info {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 25px;
            margin-top: 30px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }}

        .api-title {{
            color: #333;
            font-size: 1.3rem;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }}

        .api-title i {{
            margin-right: 10px;
            color: #667eea;
        }}

        .api-endpoints {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }}

        .endpoint {{
            background: #f8f9fa;
            padding: 12px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}

        .endpoint-method {{
            font-weight: bold;
            color: #667eea;
            font-size: 0.9rem;
        }}

        .endpoint-path {{
            color: #333;
            font-family: monospace;
            margin-top: 5px;
        }}

        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 2rem;
            }}
            
            .api-endpoints {{
                grid-template-columns: 1fr;
            }}
            
            table {{
                font-size: 0.9rem;
            }}
            
            th, td {{
                padding: 10px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-home"></i> ¡Bienvenidos a mi primera aplicación Flask!</h1>
            <p>Sistema de Gestión de Usuarios</p>
        </div>

        <div class="welcome-card">
            <div class="welcome-title">🎉 Sistema CRUD de Usuarios</div>
            <div class="welcome-subtitle">Gestiona usuarios de forma fácil y eficiente</div>
        </div>

        <div class="stats-card">
            <div class="stats-number">{len(usuarios)}</div>
            <div class="stats-label">Usuarios Registrados</div>
        </div>

        <div class="table-container">
            <div class="table-title">📋 Lista de Usuarios</div>
            <table>
                <thead>
                    <tr>
                        <th><i class="fas fa-hashtag"></i> ID</th>
                        <th><i class="fas fa-user"></i> Nombre</th>
                        <th><i class="fas fa-calendar"></i> Edad</th>
                    </tr>
                </thead>
                <tbody>
"""
    
    # Agregar filas de usuarios
    for usuario in usuarios:
        html_content += f"""
                    <tr>
                        <td class="user-id">{usuario['id']}</td>
                        <td class="user-name">{usuario['nombre']}</td>
                        <td><span class="user-age">{usuario['edad']} años</span></td>
                    </tr>
"""
    
    html_content += """
                </tbody>
            </table>
        </div>

        <div class="api-info">
            <h3 class="api-title">
                <i class="fas fa-code"></i>
                Endpoints de la API
            </h3>
            <div class="api-endpoints">
                <div class="endpoint">
                    <div class="endpoint-method">POST</div>
                    <div class="endpoint-path">/usuarios</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-method">GET</div>
                    <div class="endpoint-path">/usuarios</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-method">GET</div>
                    <div class="endpoint-path">/usuarios/&lt;id&gt;</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-method">PUT</div>
                    <div class="endpoint-path">/usuarios/&lt;id&gt;</div>
                </div>
                <div class="endpoint">
                    <div class="endpoint-method">DELETE</div>
                    <div class="endpoint-path">/usuarios/&lt;id&gt;</div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""
    
    return html_content

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
