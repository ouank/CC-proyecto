class User(object):
	'''
	This is the User class 
	'''
	def __init__(self, name: str, location: dict, email: str) -> None:
		self.name = name
		self.location = location
		self.email = email

	def request(self, plant_name):
		'''
		[HU] As a User I want to make a suggestions about plants that should be added to the data base
		'''
		pass