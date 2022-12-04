#Imports
import socket
import re
import random
import sys
import time
import itertools

class Notebook:
    def __init__(self):
        self.master_list = []
        self.foundSuspects = []
        self.foundWeapons = []
        self.foundRooms = []
    
    def add_to_notebook(self):
        user_input = input("What would you like to record?")
        self.master_list.append(user_input)
        print ("You recorded " + user_input) 
    
    def add_suggestion(self, suspect, weapon, room):
        """can use this flavor of recording input to specify room/suspect/weapon"""
        self.foundSuspects.append(suspect)
        self.foundWeapons.append(weapon)
        self.foundRooms.append(room)
        
    def read_notebook(self):
        print (self.master_list)
    
    
"""unit tests..."""
n1 = Notebook()
n1.add_to_notebook()
n1.add_to_notebook()
n1.read_notebook()
