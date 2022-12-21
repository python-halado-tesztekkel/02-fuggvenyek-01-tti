from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import tti

class TestOsszeg(TestCase):
    def test_feladat01(self):
        aktualis = tti.tti_szoveg(0,1)
        elvart = "tti indexe maghatározhatatlan"
        self.assertEqual(elvart, aktualis, "Hibás testőmeg adatot nem kezeli jól.")

    def test_feladat02(self):
        aktualis = tti.tti_szoveg(1,0)
        elvart = "tti indexe maghatározhatatlan"
        self.assertEqual(elvart, aktualis, "Hibás magasság adatot nem kezeli jól.")