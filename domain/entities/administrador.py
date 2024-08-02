from app import db

class Administrador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('administrador', lazy=True))

    def __repr__(self):
        return f'<Administrador {self.id}>'
