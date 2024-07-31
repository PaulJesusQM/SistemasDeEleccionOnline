from app import app
from controllers.usuario_controller import usuario_bp
from controllers.votacion_controller import list_votaciones, detail_votacion

app.register_blueprint(usuario_bp, url_prefix='/api')
app.add_url_rule('/votaciones', 'list_votaciones', list_votaciones)
app.add_url_rule('/votaciones/<int:votacion_id>', 'detail_votacion', detail_votacion)
