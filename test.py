#!/usr/bin/env python3

import cv2 as cv
from digit_reader import DigitReader
from unittest import TestCase
from datetime import time


class TestReader(TestCase):
    def test_reader(self):
        reader = DigitReader()
        img = cv.imread("demo.png", 0)

        drone = reader.get_drone(img)
        order_time = reader.get_time(img)

        self.assertEqual(drone, 105)
        self.assertEqual(order_time, time.fromisoformat("02:04:08"))
