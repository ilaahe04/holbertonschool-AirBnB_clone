#!/usr/bin/python3

import os
import unittest

from models import storage
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.objects = {}

    def test_place_id(self):
        myModel = Review()
        myModel.place_id = "164"
        self.assertEqual(myModel.place_id, "164")

    def test_user_id(self):
        myModel = Review()
        myModel.user_id = "165"
        self.assertEqual(myModel.user_id, "165")

    def test_text(self):
        myModel = Review()
        myModel.text = "Baku"
        self.assertEqual(myModel.text, "Baku")
