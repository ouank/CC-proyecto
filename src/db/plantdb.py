import os 
import sqlite3

from sqlalchemy.sql import select
from . import dal


class PlantDB:
	'''
	[HU] As a plant lover, I would like to find plants with my own criteria
	This is just a draft. Maybe another tool will be used for database
	'''
	def __init__(self, db_dir = os.path.join(os.path.dirname(__file__), 'PlantallaDB.db')):
		self.__db_dir = db_dir
		self.dal = dal
		self.dal.db_init(db_dir = self.__db_dir)

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
			#dal.init()
#			ct = create_table()
			ins = self.dal.plants.insert()
			dal.connection.execute(ins, plant_name = name,
										water_quantity = water_quantity,
										water_quality = water_quality,
										care_quantity = care_quantity,
										wind = wind,
										brightness = brightness,
										humidity = humidity)


			print(f'Plant {name} was successfully added to the database with the following attributes: \
					water_quantity: {water_quantity}, water_quality: {water_quality}, care_quantity: {care_quantity}, wind: {wind}, brightness: {brightness}, humidity: {humidity}.')
		except:
			print(f'Plant {name} could not be added. An Error occurred.')

	def get_criteria(self, name: str) -> list:
		'''Get plant conditions by searching for the plants name'''
		s = self.dal.plants.select().where(self.dal.plants.columns.plant_name == name)

		return self.dal.connection.execute(s).fetchall()

	def get_plants(self, water_quantity: str, water_quality: str, care_quantity: str, wind: bool, brightness: str, humidity: str) -> list:
		'''Get possible plants searching by condition'''
		c = self.dal.plants.columns
		s = select([self.dal.plants.columns.plant_name]).where(c.water_quantity == water_quantity 
															and c.water_quality == water_quality 
															and c.care_quantity == care_quantity 
															and c.wind == wind
															and c.brightness == brightness
															and c.humidity == humidity)

		return self.dal.connection.execute(s).fetchall()