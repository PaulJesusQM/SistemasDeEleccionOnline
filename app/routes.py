from flask import Flask, render_template, request, redirect, url_for, session
from .models import Usuario, Eleccion, Candidato
from . import db
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        nuevo_usuario = Usuario(nombre=nombre, email=email, password=password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = Usuario.query.filter_by(email=email, password=password).first()
        if usuario:
            session['usuario_id'] = usuario.id
            return redirect(url_for('home'))
        else:
            return "Email o contraseña incorrectos", 400
    return render_template('login.html')

@app.route('/home')
def home():
    elecciones = Eleccion.query.filter(Eleccion.fecha_fin >= datetime.now()).all()
    elecciones_pasadas = Eleccion.query.filter(Eleccion.fecha_fin < datetime.now()).all()
    return render_template('home.html', elecciones=elecciones, elecciones_pasadas=elecciones_pasadas)

@app.route('/detalle/<int:id>')
def detalle_eleccion(id):
    eleccion = Eleccion.query.get(id)
    return render_template('detail.html', eleccion=eleccion)

@app.route('/votar/<int:id>', methods=['POST'])
def votar(id):
    candidato_id = request.form['candidato']
    eleccion = Eleccion.query.get(id)
    candidato = Candidato.query.get(candidato_id)
    # Lógica para registrar el voto
    return redirect(url_for('home'))
