from Constants import *
import copy

class Entity:

	def __init__(self, entity_name, entity_score, entity_profile):
		self.name = entity_name
		self.score = entity_score
		self.profile = copy.deepcopy(entity_profile)
		self.alive = True
		self.parse_entity_profile # For now, profiles will be stored in Constants

	def parse_entity_profile(profile):
		self.level = profile['level']

		self.max_hp = profile['max_hp']
		if 'hp' in profile:
			self.hp = profile['hp']
		else:
			self.hp = self.max_hp

		self.max_mp = profile['max_mp']
		if 'mp' in profile:
			self.mp = profile['mp']
		else:
			self.mp = self.max_mp

		for equipment in profile['equipment']:
			self.add_equipment(equipment)

	def damage(self, amount):
		self.hp -= amount
		if self.hp <= 0:
			self.die()

	def die(self):
		self.alive=False

