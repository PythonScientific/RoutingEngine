#!/usr/bin/env python
""" DataAccess Class
Reads various format of data and provides nice and clean graph structure
to operate on

Author: 	Patryk Zabkiewicz
Date:		2015.08.04

"""

from graph import *

class DataAccess:
    def __init__(self):
        self.__data = []

    @staticmethod
    def read_txt(filename):
        graph = Graph()
        return graph
