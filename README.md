# Sistemas de Elección Online

## Descripción
Esta es una aplicación web desarrollada con Flask, utilizando un enfoque de Domain-Driven Design (DDD) y Model-View-Controller (MVC). La aplicación está configurada para trabajar con una base de datos SQLite utilizando SQLAlchemy y Flask-Migrate para manejar las migraciones.

## Estructura del Proyecto

# Estructura del Proyecto

## SistemasDeEleccionOnline/
```
- **app/**
  - `__init__.py`
  - `routes.py`
  - `models.py`
  - **api/**
    - `__init__.py`
    - `usuario_api.py`
    - `votacion_api.py`
    - `administrador_api.py`
    - `candidato_api.py`
    - `voto_api.py`
  - **templates/**
    - `base.html`
    - `index.html`
    - **usuario/**
      - `list.html`
      - `detail.html`
    - **votacion/**
      - `list.html`
      - `detail.html`
    - **administrador/**
      - `list.html`
      - `detail.html`
    - **candidato/**
      - `list.html`
      - `detail.html`
    - **voto/**
      - `list.html`
      - `detail.html`
  - **static/**
    - **css/**
      - `styles.css`
    - **js/**
      - `scripts.js`
    - **images/**
      - `logo.png`

- **controllers/**
  - `__init__.py`
  - `usuario_controller.py`
  - `votacion_controller.py`
  - `administrador_controller.py`
  - `candidato_controller.py`
  - `voto_controller.py`

- **domain/**
  - `__init__.py`
  - **entities/**
    - `__init__.py`
    - `administrador.py`
    - `usuario.py`
    - `votacion.py`
    - `candidato.py`
    - `voto.py`
  - **repositories/**
    - `__init__.py`
    - `usuario_repository.py`
    - `votacion_repository.py`
    - `administrador_repository.py`
    - `candidato_repository.py`
    - `voto_repository.py`
  - **services/**
    - `__init__.py`
    - `usuario_service.py`
    - `votacion_service.py`
    - `administrador_service.py`
    - `candidato_service.py`
    - `voto_service.py`

- **migrations/**
  - **versions/**

- **tests/**
  - `__init__.py`
  - `test_usuario.py`
  - `test_usuario_api.py`
  - `test_votacion.py`
  - `test_votacion_api.py`
  - `test_administrador.py`
  - `test_administrador_api.py`
  - `test_candidato.py`
  - `test_candidato_api.py`
  - `test_voto.py`
  - `test_voto_api.py`

- `manage.py`
- `requirements.txt`
- `.env`
- `config.py`
- `database.db`
```
# Instalación

1. **Clonar el repositorio**:
   - Abre tu terminal o línea de comandos.
   - Navega hasta la carpeta donde deseas clonar el repositorio.
   - Copia la URL del repositorio que deseas clonar desde GitHub.
   - Ejecuta el siguiente comando para clonar el repositorio:
     ```bash
     git clone <url-del-repositorio>
     ```

2. **Crear y activar un entorno virtual**:
   - Crea un entorno virtual con Python 3:
     ```bash
     python3 -m venv venv
     ```
   - Activa el entorno virtual:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar las dependencias**:
   - Asegúrate de estar en la raíz del proyecto (donde se encuentra el archivo `requirements.txt`).
   - Ejecuta el siguiente comando para instalar las dependencias:
     ```bash
     pip install -r requirements.txt
     ```

4. **Configurar las variables de entorno**:
   - Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
     ```
     DATABASE_URL=sqlite:///database.db
     ```

5. **Inicializar la base de datos**:
   - Ejecuta los siguientes comandos para crear y migrar la base de datos:
     ```bash
     flask db init
     flask db migrate -m "Initial migration."
     flask db upgrade
     ```
# Uso

1. **Ejecuta la aplicación**:
   - Para iniciar la aplicación, ejecuta el siguiente comando:
     ```bash
     flask run
     ```
   - La aplicación se ejecutará en el puerto 5000.

2. **Exporta la aplicación Flask (si es necesario)**:
   - Si necesitas exportar la aplicación para desplegarla en otro entorno, configura la variable de entorno `FLASK_APP`:
     ```bash
     export FLASK_APP=manage.py
     ```
   - Luego, puedes construir un archivo wheel (.whl) para desplegarlo en otro entorno.

3. **Estructura del Código**:
   - Tu proyecto sigue una estructura organizada para mantener la claridad y la modularidad. Aquí están los principales directorios y archivos:
     - **app/controllers/**: Contiene los controladores que manejan la lógica de las rutas.
     - **app/domain/**: Define el dominio de la aplicación, incluyendo entidades, repositorios y servicios.
     - **app/templates/**: Contiene las plantillas HTML para renderizar vistas.
     - **app/static/**: Almacena archivos estáticos como CSS, JavaScript e imágenes.
     - **tests/**: Incluye pruebas unitarias y de integración.
     - **migrations/**: Contiene los archivos de migración de la base de datos.

# Convenciones de Codificación y Buenas Prácticas

## Nombres
Es importante utilizar nombres descriptivos para las variables y parámetros. Esto facilita la comprensión del código y su mantenimiento.

## Funciones (Python)
```python
def create_usuario(data: dict) -> Usuario:
    """
    Crea un nuevo usuario a partir de los datos proporcionados.

    Args:
        data (dict): Diccionario con los datos del usuario.

    Returns:
        Usuario: Objeto Usuario creado.
    """
    usuario = Usuario(**data)
    self.repository.save(usuario)
    return usuario 
```
## Comentarios
Los comentarios claros y concisos ayudan a entender la intención detrás del código.

## Estructura del Código Fuente
La correcta indentación y la separación de las funciones con líneas en blanco mejoran la legibilidad del código.

## Objetos/Estructura de Datos
Usa estructuras de datos apropiadas y mantenlas organizadas para facilitar el mantenimiento y la extensión.

# Principios SOLID
## Single Responsibility Principle (SRP)
Cada clase tiene una única responsabilidad. Los controladores, servicios y repositorios tienen responsabilidades distintas.
```python
class UsuarioRepository:
    def save(self, usuario: Usuario):
        # Guarda el usuario en la base de datos
        pass

class UsuarioService:
    def create_usuario(self, data: dict) -> Usuario:
        # Lógica de negocio para crear un usuario
        pass
```
## Open/Closed Principle (OCP)
El código está abierto para extensión pero cerrado para modificación.

```python
class UsuarioRepository:
    def save(self, usuario: Usuario):
        pass

    def find_by_email(self, email: str) -> Usuario:
        # Método adicional sin modificar los existentes
        pass
```

## Dependency Inversion Principle (DIP)
Los módulos de alto nivel no deben depender de los módulos de bajo nivel. Ambos deben depender de abstracciones.

```python
class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository
```
# Estilos de Programación
## Cookbook
El estilo cookbook se utiliza para operaciones comunes y reutilizables como el manejo de base de datos.

```python
class UsuarioRepository:
    def find_by_id(self, usuario_id: int) -> Usuario:
        return Usuario.query.get(usuario_id)
```
# Restful
Se utiliza para estructurar los controladores y servicios en la aplicación.
```python
@usuario_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    usuario = usuario_service.create_usuario(data)
    return jsonify(usuario.serialize()), 201
```

# Error/Exception Handling
Manejo de errores y excepciones para mejorar la robustez del código.
```python
try:
    usuario = usuario_service.create_usuario(data)
except DatabaseError as e:
    return jsonify({"error": str(e)}), 400
```