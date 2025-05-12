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
        created_at = datetime.now()
        updated_at = datetime.now()



