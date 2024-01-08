#!/usr/bin/python3
"""function that adds a new attribute to an object"""


def add_attribute(obj, att, value):
    """Raise a TypeError exception, with the message can't add new
    attribute if the object can’t have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
