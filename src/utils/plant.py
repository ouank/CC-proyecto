from .user import User
import os 
from .op_utils import *


class PlantDB(object):
	'''
	[HU] As a plant lover, I would like to find plants with my own criteria
	This is just a draft. Maybe another tool will be used for database
	'''

	def __init__(self, db_path: str):
		self.path = db_path
		self.load(self.path)


	def load(self, path: str):
		'''
		Database loader
		'''
		if os.path.exists(path):
			self.db = load_json(path)
		else:
			self.db = {}
		return True


	def savedb(self):
		'''
		Database saver / Dumper
		'''
		try:
			save_json(self.db, self.path)
			return True
		except:
			return False


	def set(self, name: str, water_quantity: str, water_quality: str, care_quantity: str, wind: bool, brightness: str, humidity: str):
		'''
		Add new plant to Database
		Args:
			name: name of the plant of type str
			water_quantity: amount of water the plant to be searched will need. Out of [low, normal, high]
			water_quality: what kind of water quality you can present to the plant. Out of [tap, rain]
			care_quantity: how often you want to / can care for your plant [rarely, normal, often]
			wind: If the chosen location in the room will be windy.
			brightness: How bright will the location be? [shadow, partly, fully]
			humidity: What is the average humidity of the Region [low, middle, high]
		'''
		try:
			self.db[name] = {}
			self.db[name]['water_quantity'] = water_quantity
			self.db[name]['water_quality'] = water_quality 
			self.db[name]['care_quantity'] = care_quantity
			self.db[name]['wind'] = wind
			self.db[name]['brightness'] = brightness
			self.db[name]['humidity'] = humidity
			self.savedb()
			return True
		except Exception as e:
			print('Error saving new plant to Database: ' + str(e))
			return False

	def get_db(self):
		return self.db

	def get_value_by_key(self, name: str):
		'''
		Get Values by searching for the key.
		Get plant conditions by searching for the plants name
		'''
		pass


	def get_key_by_values(self, water_quantity: str, water_quality: str, care_quantity: str, wind: bool, brightness: str):
		'''
		Get keys by searching for their values
		Get possible plants searching by condition
		'''
		pass
