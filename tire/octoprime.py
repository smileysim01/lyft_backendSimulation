#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:09:26 2023

@author: simran
"""

from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array
        

    def needs_service(self):
        return sum(self.tire_wear_array) >= 3
