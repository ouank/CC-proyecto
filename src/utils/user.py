class User(object):
	'''
	This is the User class 
	'''
	def __init__(self, ID: int, name: str, location: dict, email: str) -> None:
		self.id = ID
		self.name = name
		self.location = location
		self.email = email

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_location(self):
		return self.location

	def get_email(self):
		return self.email

	def set_email(self,email):
		self.email = email

	def request(self, plant_name: str, website: str = None):
		'''
		[HU] As a User I want to make a suggestions about plants that should be added to the data base
		Args:
			plant_name: Name of the plant the user suggests to be added to the data bank
			website: Optional, give a reference website for this plant 
		'''
		

		pass