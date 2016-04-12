#!/usr/bin/env python
""" DataAccess Class
Reads various format of data and provides nice and clean graph structure
to operate on

Author: 	Patryk Zabkiewicz
Date:		2015.08.04

License info:
This software comes with NO WARRANTY. You use it at your own risk.
Full license text is avaible at http://www.gnu.org/licenses/lgpl-3.0.html

"""

from graph import *

class DataAccess:
    def __init__(self):
        self.__data = []

    @staticmethod
    def read_txt(filename):
        graph = Graph()
        return graph
