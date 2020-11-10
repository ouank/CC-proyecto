from .op_utils import *

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

	def request(self, plant_name: str, path = None):
		'''
		[HU] As a User I want to make a suggestions about plants that should be added to the data base
		For now it adds the plant to a simple list on the OS. The Saving point of the list will be changed in a later step
		Args: 
			plant_name: Name of the plant the user suggests to be added to the data base 
		'''
		if path == None:
			path = 'new_plants.json'
		json_dict = load_json(path)
		user_id = str(self.id)
		json_dict[user_id] = {}
		#json_dict['User_ID'] = self.id
		json_dict[user_id]['User_name'] = self.name
		json_dict[user_id]['User_location'] = self.location
		json_dict[user_id]['User_email'] = self.email
		json_dict[user_id]['new_plant'] = plant_name
		print(json_dict)
		save_json(json_dict, path)

		return




		#pass