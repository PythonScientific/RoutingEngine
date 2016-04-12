#!/usr/bin/env python
""" Algorithm Class
Provides bunch of algorithms that operates on data

Author: 	Patryk Zabkiewicz
Date:		2015.08.04

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

from Graph import *

class Algorithm:
    def __init__(self):
        self.__data = []

    @staticmethod
    def a_star(graph, start_vertex, end_vertex):
	route = List()
	while( verticiesList ):
        verticies
        
    while( verticiesList )
        v = verticiesList.pop()
		route.push(v)
	return route

    @staticmethod
    def dijkstra(graph, start_vertex, end_vertex):
	return route

    @staticmethod
    def find_shortes_path(graph, start_vertex, end_vertex):
	""" Searches for the shortest path between two points  """
        route = Route()
	while( graph.getListOfVerticies() )
		route.add()
        return route

    @staticmethod
    def precalculate_shortest_path(graph):
	""" Precalculate the route from every point to every point """
	verticiesList = graph.getListOfVerticies()

	while( verticiesList )
		v = verticiesList.pop()
		
	return

    @staticmethod
    def find_maximum_flow(graph,source_vertex,sink_vertex):
        route = Route()
        return route

    @staticmethod
    def find_most_economical_route(graph,start_vertex,end_vertex):
        route = Route()
        return route

    @staticmethod
    def erdoes_gallai(dsequence):
        if sum(dsequence) % 2:
            # sum of sequence is odd
            return False
        if Graph.is_degree_sequence(dsequence):
            for k in range(1,len(dsequence) + 1):
                left = sum(dsequence[:k])
                right =  k * (k-1) + sum([min(x,k) for x in dsequence[k:]])
                if left > right:
                    return False
        else:
            # sequence is increasing
            return False
        return True
