#!/usr/bin/env python
""" Graph Class
Base class for routing engine.

Author: 	Patryk Zabkiewicz
Date:		2015.08.01

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

from vertex import *
from edge import *

class Graph:
	def __init__(self,graph_input={}):
		self.__graph = graph_input

	def add_vertex(self,vertex):
		if vertex not in self.__graph:
			self.__graph[vertex] = []

	def add_edge(self,edge):
		edge = set(edge)
		(vertex1, vertex2) = tuple(edge)
		if vertex1 in self.__graph:
			self.__graph[vertex1].append(vertex2)
		else:
			self.__graph[vertex1] = [vertex2]

	def generate_edges(self):
		edges = []
		for node in self.__graph:
			for neighbour in self.__graph[node]:
				edges.append((node, neighbour))
		return edges

	def find_isolated_nodes(self):
		isolated = []
		for node in self.__graph:
			if not self.__graph[node]:
				isolated += node
		return isolated

	def find_path(self, start_vertex, end_vertex, path=[]):
		""" find a simple path from A to B in graph """
		graph = self.__graph
		path = path + [start_vertex]
		if start_vertex == end_vertex:
			return path
		if start_vertex not in graph:
			return None
		for vertex in graph[start_vertex]:
			if vertex not in path:
				extended_path = self.find_path(vertex, end_vertex, path)
				if extended_path:
					return extended_path
		return None

	def vertex_degree(self,vertex):
		degree = 0
		return degree

	def max_degree(self):
		degree = 0
		return degree

	def min_degree(self):
		degree = 100000
		return degree

	def degree_seqence(self):
		seq = []
		return seq

	def density(self):
		density = 0
		return density

	def check_connectivity(self):
		return True

	def distance(self, start_vertex, end_vertex):
		distance = 0
		return distance

	def diameter(self):
		diameter = 0
		return diameter
