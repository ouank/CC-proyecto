## Some Pseudocode as first draft
import json
database_dir = '/MyDatabaseDirectory'

def save_json(obj, file, indent=4, sort_keys=True):
    with open(file, 'w') as f:
        json.dump(obj, f, sort_keys=sort_keys, indent=indent)

class Request:
	'''
	User Request to add certain plants to database
	'''
	def __init__(self, new_plant, description=None, Username='NoName', Emailadress=None):
		self.name = Username
		self.mail = Emailadress
		self.plant_name = new_plant
		self.comment = description
		
		assert isinstance(self.plant_name, str), 'the plant name should be string'

	def save(): 
		json_dict = dict()
		json_dict['Username'] = self.name
		json_dict['User_email'] = self.mail
		json_dict['plant_to_add'] = self.plant_name
		json_dict['User_comment'] = self.comment
		save_json(json_dict,database_dir)

	def repeat_plant_name(self):
		return self.plant_name


class Record_Traffic:
	'''
	Search Plants based on Room Condition and Location of User
	'''
	def __init__(self, location, conditions):
		self.location = location
		self.conditions = conditions

		assert isinstance(self.location, dict), 'wrong content for location were given'
	def save():
		'''TODO:
		add to statistics of application'''		


class Record_Search:
	'''
	Search for conditions of certain specific plants
	'''
	def __init__(self, location, plant_name):
		self.location = location
		self.plant_name = plant_name

		assert isinstance(self.location, dict), 'wrong content for location were given'
	def save():
		'''TODO
		add to statistics of application'''

class Search: 
	def __init__(self,location, con1, con2, con3):
		self.location = location
		self.con1 = con1
		self.con2 = con2
		self.con3 = con3

	def apply(): 
		'''apply search algorithm''' 