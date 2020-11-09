from .user import User

class Plant(object):
	'''
	[HU] As a plant lover, I would like to find plants with my own criteria
	'''
	def __init__(self, name: str, water_quantity: str, water_quality: str, care_quantity: str, wind: bool, brightness: str) -> None:
		'''
		Args:
			name: name of the plant of type str
			water_quantity: amount of water the plant to be searched will need. Out of [low, normal, high]
			water_quality: what kind of water quality you can present to the plant. Out of [tap, rain]
			care_quantity: how often you want to / can care for your plant [rarely, normal, often]
			wind: If the chosen location in the room will be windy.
			brightness: How bright will the location be? [shadow, partly, fully]
		'''
		self.name = name
		self.w_qn = water_quantity
		self.w_ql = water_quality
		self.c_qn = care_quantity
		self.wind = wind
		self.bright = brightness

	def search(self) -> list:
		user_loc = User.get_location()


		pass