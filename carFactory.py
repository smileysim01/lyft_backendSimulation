#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:42:44 2023

@author: simran
"""

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.splinder import SplinderBattery
from battery.nubbin import NubbinBattery

from car import Car

class CarFactory(Car):
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(last_service_date, warning_light_on)
        battery = SplinderBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage): 
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car