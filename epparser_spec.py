import unittest
from should_dsl import should
import ephemeris

class EphemerisParserSpec(unittest.TestCase):

    def setUp(self):
        self.ephemerisTestISSPass1_1SecCompact = ephemeris.ephemerisTestISSPass1_1SecCompact
        self.ephemerisTestISSPass1_1Sec = ephemeris.ephemerisTestISSPass1_1Sec
