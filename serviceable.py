
"""
Created on Tue Dec  5 18:25:44 2023

@author: simran
"""

from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass