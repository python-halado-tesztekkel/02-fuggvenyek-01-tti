from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import tti

class TestOsszeg(TestCase):
    def test_feladat01(self):
        aktualis = tti.tti_szoveg(1.8,60)
        elvart = "sovány"
        self.assertEqual(elvart, aktualis, "tti értékelés pontatlan sovány súly esetén")
