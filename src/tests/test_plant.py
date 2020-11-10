import pytest
from utils.plant import PlantDB
from utils.op_utils import *
import os

@pytest.fixture
def db_path():
	return os.path.join(os.path.expanduser('~'), 'ugr', 'cc', 'repos', 'selva_urbana', 'src', 'tests', 'testdict_plantdb.json')

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