#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:11:18 2023

@author: simran
"""

from battery.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        

    def needs_service(self):
        return self.last_service_date.year - self.current_date.year > 4