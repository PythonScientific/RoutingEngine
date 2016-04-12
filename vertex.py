#!/usr/bin/env python
""" Vertex Class
Represent a vertex with properties.

Author: 	Patryk Zabkiewicz
Date:		2015.08.03

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

class Vertex:
    def __init__(self,vertex={}):
        if vertex:
            self.__verticies = vertex.__verticies
            self.id = vertex.id
            self.name = vertex.name
            self.capacity = vertex.capacity
            self.flow = vertex.flow
            self.speed = vertex.speed
            self.inflow = vertex.inflow
            self.outflow = vertex.outflow
            self.max_outflow = vertex.max_outflow
            self.cost = vertex.cost
        else:
            self.id = 0
            self.name = ""
            self.capacity = 0
            self.flow = 0
            self.speed = 0
            self.inflow = 0
            self.outflow = 0
            self.max_outflow = 0
            self.cost = 0

    def add_edge(self,vertex):
        self.__verticies.append(vertex)
