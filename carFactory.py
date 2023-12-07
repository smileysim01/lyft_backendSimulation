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
from tire.carrigan import CarriganTire
from tire.octoprime import OctoprimeTire

from car import Car

class CarFactory(Car):
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear_array)
        car = Car(engine, battery, tire)
        return car
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear_array)
        car = Car(engine, battery, tire)
        return car
    
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear_array):
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear_array)
        car = Car(engine, battery, tire)
        return car
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array): 
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear_array)
        car = Car(engine, battery, tire)
        return car
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear_array)
        car = Car(engine, battery, tire)
        return car