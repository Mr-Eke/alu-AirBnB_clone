#!/usr/bin/python3
"""
This module holds a model that defines the all common attr/metthods
for other class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    A base class that defines all common attributes/methods for other classes
    """

    def __init__(self):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ returns a human readable str form of the class instance & attr"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'



