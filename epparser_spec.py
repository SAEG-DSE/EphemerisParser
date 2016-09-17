import unittest
from should_dsl import should
import ephemeris
from epparser import EphemerisParser

class EphemerisParserSpec(unittest.TestCase):

    def setUp(self):
    	self.single_ephemeris = ephemeris.ephemeris.singleEphemeris
        self.ephemerisTestISSPass1_1SecCompact = ephemeris.ephemerisTestISSPass1_1SecCompact
        self.ephemerisTestISSPass1_1Sec = ephemeris.ephemerisTestISSPass1_1Sec
        self.Parser = EphemerisParser()

    def test_parsing_of_single_ephemeris(self):
    	self.Parser.parse(single_ephemeris) |should| have(4).variables
    	self.Parser.parse(single_ephemeris) |should| contain([{'flag': 0, 'azimuth': 0.3539, 'elevation': 0.1238, 'time': datetime.datetime(2015, 12, 15, 0, 47, 50)}])

