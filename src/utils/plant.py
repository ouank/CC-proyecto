class Plant(object):
	'''
	[HU] As a plant lover, I would like to find plants with my own criteria 
	'''
	def __init__(self, name: str, water_quantity: str, water_quality: str, care_quantity: str, wind: bool, brightness: str, location: dict) -> None:
		self.name = name
		self.w_qn = water_quantity
		self.w_ql = water_quality
		self.c_qn = care_quantity
		self.wind = wind
		self.bright = brightness
		self.location = location

	def search(self) -> list:
		pass