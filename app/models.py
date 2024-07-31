from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email
        }
