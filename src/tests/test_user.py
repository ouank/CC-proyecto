import pytest
from utils.user import User
from utils.op_utils import *
import os

@pytest.fixture
def example_user():
    new_user = User(ID = 1234, name='Mark', location={'country': 'ES', 'region':'Granada'}, email='Mark.Muster@hotmail.com')
    return new_user

@pytest.fixture
def example_user2():
    new_user = User(ID = 6789, name='Max', location={'country': 'DE', 'region':'Hamburg'}, email='Max.Herman@msn.com')
    return new_user

@pytest.fixture
def json_dir():
	return os.path.join(os.path.dirname(__file__), 'testdict_newplantdb.json')

def test_getters_setters(example_user):
	assert example_user.get_name() == 'Mark'
	example_user.set_name('Ralf')
	assert example_user.get_name() == 'Ralf'

def test_request(example_user, json_dir):
	'''
	make a request
	'''
	example_user.request(plant_name = 'my_new_plant', path = json_dir)
	ex_dict = load_json(json_dir)
	assert ex_dict['1234']['User_name'] == 'Mark'
	assert ex_dict['1234']['User_location'] == {'country': 'ES', 'region':'Granada'}
	assert ex_dict['1234']['User_email'] == 'Mark.Muster@hotmail.com'
	assert ex_dict['1234']['new_plant'] == 'my_new_plant'

def test_request2(example_user2, json_dir):
	'''
	make a second request
	'''
	example_user2.request(plant_name = 'home_plant', path = json_dir)
	ex_dict = load_json(json_dir)
	assert ex_dict['1234']['User_name'] == 'Mark'
	assert ex_dict['1234']['User_location'] == {'country': 'ES', 'region':'Granada'}
	assert ex_dict['1234']['User_email'] == 'Mark.Muster@hotmail.com'
	assert ex_dict['1234']['new_plant'] == 'my_new_plant'

	assert ex_dict['6789']['User_name'] == 'Max'
	assert ex_dict['6789']['User_location'] == {'country': 'DE', 'region':'Hamburg'}
	assert ex_dict['6789']['User_email'] == 'Max.Herman@msn.com'
	assert ex_dict['6789']['new_plant'] == 'home_plant'