import unittest
from app import create_app, db
from app.domain.entities.usuario import Usuario

class UsuarioApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_usuarios(self):
        response = self.client.get('/usuarios')
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.content_type)

if __name__ == '__main__':
    unittest.main()
