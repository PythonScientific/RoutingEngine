#!/usr/bin/env python
""" Route Engine
This project is intended to provide a very fast and small routing
engine written in Python.

Author: Patryk Zabkiewicz
Date:	2015.07.30

"""

from graph import *

if __name__ == "__main__":
		graph1 = { "a" : ["c", "a"],
		  "b" : ["c", "e", "d"],
		  "c" : ["a", "b", "d", "e"],
		  "d" : ["c"],
		  "e" : ["c", "b"],
		  "f" : []
		}

		g = Graph(graph1)
		print(g.generate_edges())

