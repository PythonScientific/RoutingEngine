#!/usr/bin/env python
""" Route Class
Basic class to represent a route from A to B
The Route has two meanings:
	- list of verticies
	- list of turns

Author: Patryk Zabkiewicz
Date:	2015.08.02

"""

class Route:
	def __init__(self,route={}):
		self.__route = route
