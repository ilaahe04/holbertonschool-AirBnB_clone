#!/usr/bin/python3

import os
import unittest

from models import storage
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_city_id(self):
        myModel = Place()
        myModel.city_id = "164"
        self.assertEqual(myModel.city_id, "164")

    def test_user_id(self):
        myModel = Place()
        myModel.user_id = "165"
        self.assertEqual(myModel.user_id, "165")

    def test_name(self):
        myModel = Place()
        myModel.name = "Baku"
        self.assertEqual(myModel.name, "Baku")

    def test_description(self):
        myModel = Place()
        myModel.description = "Windy Place"
        self.assertEqual(myModel.description, "Windy Place")

    def test_number_rooms(self):
        myModel = Place()
        myModel.number_rooms = 5
        self.assertEqual(myModel.number_rooms, 5)

    def test_number_bathrooms(self):
        myModel = Place()
        myModel.number_bathrooms = 1
        self.assertEqual(myModel.number_bathrooms, 1)

    def test_max_guest(self):
        myModel = Place()
        myModel.max_guest = 5
        self.assertEqual(myModel.max_guest, 5)

    def test_price_by_night(self):
        myModel = Place()
        myModel.price_by_night = 20
        self.assertEqual(myModel.price_by_night, 20)

    def test_latitude(self):
        myModel = Place()
        myModel.latitude = 22
        self.assertEqual(myModel.latitude, 22)

    def test_longitude(self):
        myModel = Place()
        myModel.longitude = 22
        self.assertEqual(myModel.longitude, 22)

    def test_amenity_ids(self):
        myModel = Place()
        myModel.amenity_ids = ["1", "2"]
        self.assertEqual(myModel.amenity_ids, ["1", "2"])
