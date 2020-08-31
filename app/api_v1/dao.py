"""
This module defines EventDao class used for creating response data
"""


class EventDao:
    """
    Class for storing the attributes date and value
    """
    __slots__ = ['date', 'value']  # for faster creation of objects

    def __init__(self, date: str, value: int):
        self.date = date
        self.value = value
