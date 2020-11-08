import unittest
from utils.plant import Plant
from utils.user import User

class TestRequest(unittest.TestCase):

	def test_type(self):
		new_user = User(name='Mark', location={'country': 'ES', 'region':'Granada'}, email='Mark.Muster@hotmail.com')
		self.assertIn('@', new_user.email)

if __name__ == "__main__":
	unittest.main()