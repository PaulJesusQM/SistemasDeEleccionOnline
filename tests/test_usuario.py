import unittest
from app import app, db
from domain.entities.usuario import Usuario

class UsuarioModelTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_usuario_creation(self):
        usuario = Usuario(username='testuser', email='testuser@example.com', password='password')
        db.session.add(usuario)
        db.session.commit()
        self.assertEqual(usuario.username, 'testuser')

if __name__ == '__main__':
    unittest.main()
