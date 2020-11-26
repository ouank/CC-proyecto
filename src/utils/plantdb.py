import os 
import sqlite3

class PlantDB(object):
	'''
	[HU] As a plant lover, I would like to find plants with my own criteria
	This is just a draft. Maybe another tool will be used for database
	'''
	def __init__(self, db_dir = os.path.join(os.path.dirname(__file__), 'PlantDB.db')):
		self.__db_dir = db_dir
		self.connection = sqlite3.connect(self.__db_dir)
		self.__cursor = self.connection.cursor()

	def create_table(self):
		self.__cursor.execute("CREATE TABLE IF NOT EXISTS plants(plant_name TEXT, \
														water_quantity TEXT, \
														water_quality TEXT, \
														care_quantity TEXT, \
														wind BOOLEAN, \
														brightness TEXT, \
														humidity TEXT)")

	def add_plant(self, name: str, water_quantity: str, water_quality: str, care_quantity: str, wind: bool, brightness: str, humidity: str):
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
			self.__cursor.execute("INSERT INTO plants(plant_name, water_quantity, water_quality, care_quantity, wind, brightness, humidity) VALUES (?, ?, ?, ?, ?, ?, ?)", 
			(name, water_quantity, water_quality, care_quantity, wind, brightness, humidity))
			self.commit()
			print(f'Plant {name} was successfully added to the database with the following attributes: \
					water_quantity: {water_quantity}, water_quality: {water_quality}, care_quantity: {care_quantity}, wind: {wind}, brightness: {brightness}, humidity: {humidity}.')
		except:
			print(f'Plant {name} could not be added. An Error occurred.')
			

	def close(self):
		self.__cursor.close()
		self.connection.close()

	def commit(self):
		self.connection.commit()

	def get_criteria(self, name: str) -> list:
		'''Get plant conditions by searching for the plants name'''
		self.__cursor.execute("SELECT water_quantity, water_quality, care_quantity, wind, brightness, humidity FROM plants WHERE plant_name = ?", [name])
		return self.__cursor.fetchall()

	def get_plants(self, water_quantity: str, water_quality: str, care_quantity: str, wind: bool, brightness: str, humidity: str) -> list:
		'''Get possible plants searching by condition'''
		self.__cursor.execute("SELECT plant_name FROM plants WHERE water_quantity = ? \
															 AND water_quality = ? \
															 AND care_quantity = ? \
															 AND wind = ? \
															 AND brightness = ? \
															 AND humidity = ?", [water_quantity, water_quality, care_quantity, wind, brightness, humidity])
		return self.__cursor.fetchall()