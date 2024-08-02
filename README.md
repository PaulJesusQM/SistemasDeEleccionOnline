# Sistemas de Elección Online
## Propósito del Proyecto

El propósito del proyecto `SistemasDeEleccionOnline` es proporcionar una plataforma en línea para gestionar elecciones, permitiendo a los usuarios registrarse, votar en diferentes elecciones, y ver los resultados. La plataforma está diseñada para ser fácil de usar y escalable.


## Diagrama de casos de uso
![1](https://github.com/user-attachments/assets/fd058ae8-8edc-437a-9a46-369c5dd8a6ee)
##  Diagrama de Clases
![2](https://github.com/user-attachments/assets/74df8867-9d5a-41c8-851d-78396b3c1748)

![3](https://github.com/user-attachments/assets/bd4c4b11-0822-4801-a18f-77294bc24ab6)



# Estructura del Proyecto
## Descripción
Esta es una aplicación web desarrollada con Flask, utilizando un enfoque de Domain-Driven Design (DDD) y Model-View-Controller (MVC). La aplicación está configurada para trabajar con una base de datos SQLite utilizando SQLAlchemy y Flask-Migrate para manejar las migraciones.

```
SistemasDeEleccionOnline/
|-- app/
|   |-- __init__.py
|   |-- routes.py
|   |-- api/
|       |-- __init__.py
|       |-- usuario_api.py
|       |-- votacion_api.py
|       |-- administrador_api.py
|       |-- candidato_api.py
|       |-- voto_api.py
|-- controllers/
|   |-- __init__.py
|   |-- usuario_controller.py
|   |-- votacion_controller.py
|   |-- administrador_controller.py
|   |-- candidato_controller.py
|   |-- voto_controller.py
|-- domain/
|   |-- __init__.py
|   |-- entities/
|       |-- __init__.py
|       |-- administrador.py
|       |-- usuario.py
|       |-- votacion.py
|       |-- candidato.py
|       |-- voto.py
|   |-- repositories/
|       |-- __init__.py
|       |-- usuario_repository.py
|       |-- votacion_repository.py
|       |-- administrador_repository.py
|       |-- candidato_repository.py
|       |-- voto_repository.py
|   |-- services/
|       |-- __init__.py
|       |-- usuario_service.py
|       |-- votacion_service.py
|       |-- administrador_service.py
|       |-- candidato_service.py
|       |-- voto_service.py
|-- templates/
|   |-- base.html
|   |-- index.html
|   |-- detail.html
|   |-- home.html
|   |-- login.html
|   |-- register.html
|   |-- welcome.html
|   |-- usuario/
|   |   |-- list.html
|   |   |-- detail.html
|   |-- votacion/
|   |   |-- list.html
|   |   |-- detail.html
|   |-- administrador/
|   |   |-- list.html
|   |   |-- detail.html
|   |-- candidato/
|   |   |-- list.html
|   |   |-- detail.html
|   |-- voto/
|   |   |-- list.html
|   |   |-- detail.html
|-- static/
|   |-- css/
|       |-- styles.css
|   |-- js/
|       |-- main.js
|       |-- detail.js
|       |-- scripts.js
|   |-- images/
|       |-- diagrama_componentes.png
|-- migrations/
|   |-- versions/
|-- tests/
|   |-- __init__.py
|   |-- test_usuario.py
|   |-- test_usuario_api.py
|   |-- test_votacion.py
|   |-- test_votacion_api.py
|   |-- test_administrador.py
|   |-- test_administrador_api.py
|   |-- test_candidato.py
|   |-- test_candidato_api.py
|   |-- test_voto.py
|   |-- test_voto_api.py
|-- manage.py
|-- requirements.txt
|-- .env
|-- config.py
|-- database.db
|-- README.md
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

# Convenciones de Codificación y CLEAN CODE

## Nombres
Es importante utilizar nombres descriptivos para las variables y parámetros. Esto facilita la comprensión del código y su mantenimiento.

```python
def calculate_total_votes(votes):
    total = sum(votes)
    return total
```
## Comentarios
Los comentarios claros y concisos ayudan a entender la intención detrás del código.
```python
class ElectionService:
    """Servicio para manejar las operaciones relacionadas con las elecciones"""

    def get_election(self, election_id):
        # Obtiene una elección por su ID
        pass
```
## Funciones Pequeñas y Enfocadas
Escribir funciones pequeñas que hagan una sola cosa y la hagan bien.

```python
def is_valid_vote(vote):
    return vote in ['yes', 'no']

```
## Uso de Constantes
Definir constantes para valores que se repiten y pueden cambiar, en lugar de usar valores mágicos.
```python
MAX_VOTES = 100

def validate_votes(votes):
    if votes > MAX_VOTES:
        raise ValueError("Excedido el número máximo de votos")

```


## Manejo Adecuado de Excepciones
Implementar un manejo adecuado de excepciones para mejorar la robustez del código.
```python
try:
    usuario = usuario_service.create_usuario(data)
except DatabaseError as e:
    return jsonify({"error": str(e)}), 400
```

# Principios SOLID
## Single Responsibility Principle (SRP)
Cada clase tiene una única responsabilidad. Los controladores, servicios y repositorios tienen responsabilidades distintas.
```python
# UsuarioRepository: Maneja las operaciones de persistencia de usuarios
class UsuarioRepository:
    def save(self, usuario: Usuario):
        # Guarda el usuario en la base de datos
        pass

# UsuarioService: Maneja la lógica de negocio relacionada con usuarios
class UsuarioService:
    def create_usuario(self, data: dict) -> Usuario:
        # Lógica de negocio para crear un usuario
        pass

```
## Open/Closed Principle (OCP)
El código está abierto para extensión pero cerrado para modificación.

```python
# UsuarioRepository: Se puede extender con nuevos métodos sin modificar los existentes
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
# UsuarioService: Depende de una abstracción (UsuarioRepository)
class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

```
## Interface Segregation Principle (ISP)
Los clientes no deberían verse forzados a depender de interfaces que no utilizan.
```python
# Interface para el repositorio de usuarios
class IUsuarioRepository:
    def save(self, usuario: Usuario):
        pass

    def find_by_id(self, usuario_id: int) -> Usuario:
        pass

# Repositorio específico que implementa la interface
class UsuarioRepository(IUsuarioRepository):
    def save(self, usuario: Usuario):
        pass

    def find_by_id(self, usuario_id: int) -> Usuario:
        pass

```

## Liskov Substitution Principle (LSP)
Las subclases deben poder reemplazar a sus superclases sin alterar el comportamiento esperado del programa.
```python
# Clase base Usuario
class Usuario:
    def get_role(self) -> str:
        return "Usuario"

# Subclase Admin que reemplaza a Usuario
class Admin(Usuario):
    def get_role(self) -> str:
        return "Admin"

```

# Estilos de Programación
## Cookbook
El estilo cookbook se utiliza para operaciones comunes y reutilizables como el manejo de base de datos.

```python
# Método cookbook para encontrar un usuario por su ID
class UsuarioRepository:
    def find_by_id(self, usuario_id: int) -> Usuario:
        return Usuario.query.get(usuario_id)

```
# Restful
Se utiliza para estructurar los controladores y servicios en la aplicación.
```python
# Controlador Restful para crear un usuario
@usuario_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    usuario = usuario_service.create_usuario(data)
    return jsonify(usuario.serialize()), 201

```

# Error/Exception Handling
Manejo de errores y excepciones para mejorar la robustez del código.
```python
# Ejemplo de manejo de excepciones en la creación de un usuario
try:
    usuario = usuario_service.create_usuario(data)
except DatabaseError as e:
    return jsonify({"error": str(e)}), 400

```

## Convención de Nombres
Se siguen convenciones de nombres claras y consistentes para mejorar la legibilidad del código.
```python
# Uso de nombres claros y consistentes
def calculate_total_votes(votes):
    total = sum(votes)
    return total
```

## Documentación y Comentarios
Se añaden comentarios y documentación donde es necesario para clarificar el propósito y funcionamiento del código.
```python
# Comentarios explicativos para clarificar la lógica
class ElectionService:
    """Servicio para manejar las operaciones relacionadas con las elecciones"""

    def get_election(self, election_id):
        # Obtiene una elección por su ID
        pass
```

## Constantes y Configuraciones
Uso de constantes y configuraciones en lugar de números mágicos o strings hardcodeados.
```python
# Uso de constantes para mejorar la mantenibilidad del código
MAX_VOTES = 100

def validate_votes(votes):
    if votes > MAX_VOTES:
        raise ValueError("Excedido el número máximo de votos")
```

## Pantalla de Bienvenida (welcome.html)
Descripción: Pantalla de bienvenida de la aplicación. Desde aquí, los usuarios pueden navegar a la página de registro o inicio de sesión. La interfaz muestra dos botones principales: "Registrarse" e "Iniciar Sesión".
![1 1](https://github.com/user-attachments/assets/537b2be0-96d6-4899-86b6-f8280ac057d8)
## Pantalla de Registro (register.html)
Descripción: Pantalla de registro donde los nuevos usuarios pueden crear una cuenta proporcionando su nombre, email y contraseña. Incluye un formulario sencillo con campos de entrada y un botón para enviar la información.
![1 2](https://github.com/user-attachments/assets/a4c8da9c-fb76-46c0-82c5-659a111c235d)

## Pantalla de Inicio de Sesión (login.html)
Descripción: Pantalla de inicio de sesión donde los usuarios existentes pueden ingresar sus credenciales para acceder a la aplicación. Contiene un formulario con campos para email y contraseña, así como un botón para iniciar sesión.
![1 3](https://github.com/user-attachments/assets/4ef426b7-e079-4a55-b5be-b7fbca80ae45)

## Pantalla Principal (home.html)
Descripción: Pantalla principal después de iniciar sesión o registrarse. Aquí, los usuarios pueden ver las elecciones disponibles y pasadas. Las elecciones disponibles se muestran con enlaces que llevan a la página de detalles de cada elección.
![1 4](https://github.com/user-attachments/assets/ec815a0c-6e69-467f-8c1e-8326499b3788)

## Detalle de Elección (detail.html)
Descripción: Pantalla de detalles de una elección específica. Muestra los candidatos disponibles para la elección seleccionada y permite a los usuarios votar por su candidato preferido. Contiene un formulario y un botón para enviar el voto.

![1 5](https://github.com/user-attachments/assets/99743587-6bfe-4540-8767-8ec8b5714deb)
