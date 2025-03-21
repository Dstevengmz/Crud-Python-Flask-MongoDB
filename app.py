from flask import Flask, render_template, request, jsonify, redirect, url_for
import config.database as dbase
import os
from werkzeug.utils import secure_filename
from producto import Producto
from flask import session, flash

UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  
app.secret_key = 'DHIERJddds33434ASJDSJ'
db = dbase.dbconexion()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['clave']
        usuarios = db['usuarios']
        usuario = usuarios.find_one({'correo': correo, 'clave': contraseña})
        
        if usuario:
            session['usuario'] = correo
            return redirect(url_for('home'))
        else:
            flash('Credenciales incorrectas')
            return redirect(url_for('login'))
    return render_template('login.html')


#Cerrar Sesion
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))




@app.route("/")
def home():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    productos = db['productos']
    ProductoRecibidos = productos.find()
    return render_template('index.html', productos=ProductoRecibidos)

@app.route("/productos", methods=["POST"])
def agregarproducto():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    productos = db['productos']
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    precio = request.form['precio']
    categoria = request.form['categoria']
    
    if 'foto' not in request.files:
        return "No se ha cargado ninguna imagen", 400
    foto = request.files['foto']
    
    if foto and allowed_file(foto.filename):
        filename = secure_filename(foto.filename)  
        foto_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        foto.save(foto_path) 

        nuevo_producto = Producto(codigo, nombre, precio, categoria, foto_path)
        productos.insert_one(nuevo_producto.ConexionDB())
        return redirect(url_for('home'))
    else:
        return "No se han ingresado datos regrese e ingrese datos y no se ha cargado ninguna imagen", 400



@app.route("/eliminar/<string:producto_codigo>")
def eliminar(producto_codigo):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    producto = db['productos']
    producto.delete_one({'codigo': producto_codigo})
    return redirect(url_for('home'))

@app.route("/editar/<string:producto_codigo>", methods=["POST"])
def editar(producto_codigo):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    productos = db['productos']
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    precio = request.form['precio']
    categoria = request.form['categoria']
    
    if 'foto' in request.files:
        foto = request.files['foto']
        if foto and allowed_file(foto.filename):
            filename = secure_filename(foto.filename)
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            foto.save(foto_path) 
        else:
            foto_path = request.form['foto_actual']
    else:
        foto_path = request.form['foto_actual']
    
    productos.update_one(
        {'codigo': producto_codigo},
        {'$set': {'codigo': codigo, 'nombre': nombre, 'precio': precio, 'categoria': categoria, 'foto': foto_path}}
    )
    return redirect(url_for('home'))

@app.errorhandler(404)
def noFunciona(error=None):
    message = {
        'message': "No encontrado: " + request.url,
        'status': "404 no funciona"
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4100)

