import unittest
import HU_classes

class TestRequest(unittest.TestCase):

	def test_type(self):
		new_p = HU_classes.Request(new_plant='spider_plant')
		self.assertIsInstance(new_p.repeat_plant_name(),str)

if __name__ == "__main__":
	unittest.main()