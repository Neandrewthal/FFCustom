import pygame as pg
import numpy as np
from Constants import *
from EncounterManager import EncounterManager
from pygame.locals import *


class FFCustom:
	def __init__(self):
		self.running = True

	def on_init(self):
		pg.init()

	def on_execute(self):
		self.on_init()

		while (self.running):
			for event in pygame.event.get():
				self.on_event(event)

			# Do stuff
			


