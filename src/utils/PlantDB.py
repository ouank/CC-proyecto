from .user import User
import os 
from .op_utils import *
import sqlite3

class PlantDB(object):
	'''
	[HU] As a plant lover, I would like to find plants with my own criteria
	This is just a draft. Maybe another tool will be used for database
	'''
	__db_dir = os.path.join(os.path.dirname(__file__), 'PlantDB.db')
	def __init__(self):
		self.connection = sqlite3.connect(__db_dir)
		self.cursor = self.connection.cursor()

	def create_table(self):
		self.cursor("CREATE TABLE IF NOT EXISTS plants(plant_name TEXT, \
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
		self.cursor.execute("INSERT INTO plants(plant_name, water_quantity, water_quality, care_quantity, wind, brightness, humidity) VALUES (?, ?, ?, ?, ?, ?, ?)", 
			(name, water_quantity, water_quality, care_quantity, wind, brightness, humidity))
		self.commit()

	def close(self):
		self.cursor.close()
		self.connection.close()

	def commit(self):
		self.connection.commit()

	def get_criteria(self, name: str):
		'''Get plant conditions by searching for the plants name'''
		self.cursor.execute("SELECT water_quantity, water_quality, care_quantity, wind, brightness, humidity FROM plants WHERE plant_name = plant_name")
		self.print_rows(self.cursor.fetchall())

	def get_plants(self, water_quantity: str, water_quality: str, care_quantity: str, wind: bool, brightness: str):
		'''Get possible plants searching by condition'''
		self.cursor.execute("SELECT plant_name FROM plants WHERE water_quantity = water_quantity \
															 AND water_quality = water_quality \
															 AND care_quantity = care_quantity \
															 AND wind = wind \
															 AND brightness = brightness")
		self.print_rows(self.cursor.fetchall())

	def print_rows(self, data):
		for row in data:
			print(row)