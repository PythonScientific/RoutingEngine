#!/usr/bin/env python
""" Algorithm Class
Provides bunch of algorithms that operates on data

Author: 	Patryk Zabkiewicz
Date:		2015.08.04

"""

from Graph import *

class Algorithm:
    def __init__(self):
        self.__data = []

    @staticmethod
    def find_shortes_path(graph,start_vertex,end_vertex):
        route = Route()
        return route

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
