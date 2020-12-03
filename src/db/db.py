import os
from sqlalchemy import (MetaData, Table, Column, String, Boolean, create_engine)

class DataAccessLayer:
	connection = None
	engine = None
	conn_string = None
	metadata = MetaData()
	plants = Table('plants',
					metadata,
					Column('plant_name', String(), primary_key = True),
					Column('water_quantity', String()),
					Column('water_quality', String()),
					Column('care_quantity', String()),
					Column('wind', Boolean()),
					Column('brightness', String()),
					Column('humidity', String()))

	def db_init(self, db_dir = os.path.join(os.path.dirname(__file__), 'PlantDB.db')):
		self.__db_dir = db_dir
		self.engine = create_engine('sqlite:///'+self.__db_dir, echo = True)
		self.metadata.create_all(self.engine)
		self.connection = self.engine.connect()

dal = DataAccessLayer()