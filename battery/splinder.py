#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:03:58 2023

@author: simran
"""
from battery.battery import Battery

class SplinderBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        

    def needs_service(self):
        return self.current_date.year - self.last_service_date.year > 3

    