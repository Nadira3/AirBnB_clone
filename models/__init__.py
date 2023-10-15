#!/usr/bin/python3
""" This module contains storage file initialization """

from models import base_model, amenity, city, place, state, user, review
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
