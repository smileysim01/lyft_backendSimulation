#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:36:27 2023

@author: simran
"""
from abc import ABC

class Engine(ABC):
    def needs_service(self):
        pass 