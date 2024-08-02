from app import db

class Voto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    votacion_id = db.Column(db.Integer, db.ForeignKey('votacion.id'), nullable=False)
    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    
    usuario = db.relationship('Usuario', backref=db.backref('votos', lazy=True))
    votacion = db.relationship('Votacion', backref=db.backref('votos', lazy=True))
    candidato = db.relationship('Candidato', backref=db.backref('votos', lazy=True))

    def __repr__(self):
        return f'<Voto {self.id}>'
