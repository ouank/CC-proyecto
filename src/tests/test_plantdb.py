import pytest

from utils.plantdb import PlantDB

import os
import sqlite3 


@pytest.fixture
def setup_database():
	""" Fixture to set up the in-memory database with test table"""
	db = PlantDB(db_dir = ':memory:')
	db.create_table()
	yield db

@pytest.fixture
def setup_test_data(setup_database):
	plant1_name = "crassula_ovata"
	plant1_water_quantity = "low"
	plant1_water_quality = "tap"
	plant1_care_quantity = "rarely"
	plant1_wind = True
	plant1_brightness = "fully"
	plant1_humidity = "low"
	setup_database.add_plant(name = plant1_name, water_quantity = plant1_water_quantity, water_quality = plant1_water_quality, 
					care_quantity = plant1_care_quantity, wind = plant1_wind, brightness = plant1_brightness, humidity = plant1_humidity)
	plant2_name = "ivy"
	plant2_water_quantity = "high"
	plant2_water_quality = "tap"
	plant2_care_quantity = "normal"
	plant2_wind = True
	plant2_brightness = "fully"
	plant2_humidity = "low"
	setup_database.add_plant(name = plant2_name, water_quantity = plant2_water_quantity, water_quality = plant2_water_quality, 
					care_quantity = plant2_care_quantity, wind = plant2_wind, brightness = plant2_brightness, humidity = plant2_humidity)
	yield setup_database

def test_sample_data(setup_test_data):
	# Test to make sure that there is 1 item in the database
	assert len(list(setup_test_data._PlantDB__cursor.execute("SELECT * FROM plants"))) == 2

def test_add_plant(setup_database, capsys):
	name = "spider_plant"
	water_quantity = "normal"
	water_quality = "tap"
	care_quantity = "rarely"
	wind = True
	brightness = "fully"
	humidity = "middle"
	setup_database.add_plant(name = name, water_quantity = water_quantity, water_quality = water_quality, care_quantity = care_quantity, wind = wind, brightness = brightness, humidity = humidity)
	captured = capsys.readouterr()
	assert captured.out == f'Plant {name} was successfully added to the database with the following attributes: \
					water_quantity: {water_quantity}, water_quality: {water_quality}, care_quantity: {care_quantity}, wind: {wind}, brightness: {brightness}, humidity: {humidity}.\n'

def test_get_criteria(setup_test_data):
	plant_name = "crassula_ovata"
	criterias = setup_test_data.get_criteria(name = plant_name)
	assert criterias == [('low', 'tap', 'rarely', True, 'fully', 'low')]

def test_get_plants(setup_test_data):
	water_quantity = "low"
	water_quality = "tap"
	care_quantity = "rarely"
	wind = True
	brightness = "fully"
	humidity = "low"
	plants = setup_test_data.get_plants(water_quantity = water_quantity, water_quality = water_quality, care_quantity = care_quantity, wind = wind, brightness = brightness, humidity = humidity)
	assert plants == [('crassula_ovata',)]