import unittest
from app import app, db
from domain.entities.votacion import Votacion

class VotacionModelTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_votacion_creation(self):
        votacion = Votacion(
            titulo='Elección 2024',
            descripcion='Elección presidencial 2024',
            fecha_inicio='2024-01-01',
            fecha_fin='2024-01-15'
        )
        db.session.add(votacion)
        db.session.commit()
        self.assertEqual(votacion.titulo, 'Elección 2024')

if __name__ == '__main__':
    unittest.main()
