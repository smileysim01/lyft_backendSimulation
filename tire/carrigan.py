#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:09:23 2023

@author: simran
"""

from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array
        

    def needs_service(self):
        for val in self.tire_wear_array:
            if val >= 0.9:
                return True
        return False
