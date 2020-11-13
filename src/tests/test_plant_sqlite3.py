import pytest
from utils.plant import PlantDB
from utils.op_utils import *
import os
import sqlite3 


@pytest.fixture
def db_dir():
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),'utils','PlantDB.db')

def test_existence(db_dir):
	assert os.path.isfile(db_dir)

def test_load(db_dir):
	try:
		conn = sqlite3.connect('file:{}?mode=rw'.format(db_dir), uri=True)
		c = conn.cursor()
	except sqlite3.OperationalError:
		raise AssertionError('Database does not exist')

def test_save(db_dir):
	assert 





@pytest.fixture
def db_path():
	return os.path.join(os.path.dirname(__file__),'testdict_plantdb.json')	
	
@pytest.fixture
def example_db(db_path):
	return PlantDB(db_path = db_path)

def test_load(example_db, db_path):
	assert example_db.load(path = db_path) == True

def test_save(example_db):
	assert example_db.savedb() == True

def test_set(example_db, db_path):
	assert example_db.set(name = 'Crassula Ovata', water_quantity = 'low', water_quality = 'tap', care_quantity = 'rarely', wind = True, brightness = 'fully', humidity = 'low') == True
	example_db.load(path = db_path)
	new_db = example_db.get_db()
	assert new_db['Crassula Ovata']['water_quantity'] == 'low'
	assert new_db['Crassula Ovata']['water_quality'] == 'tap'

