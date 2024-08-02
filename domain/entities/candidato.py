from app import db

class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    votacion_id = db.Column(db.Integer, db.ForeignKey('votacion.id'), nullable=False)
    votacion = db.relationship('Votacion', backref=db.backref('candidatos', lazy=True))

    def __repr__(self):
        return f'<Candidato {self.nombre}>'
