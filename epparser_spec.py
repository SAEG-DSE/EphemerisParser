import unittest
from should_dsl import should
import ephemeris
from epparser import EphemerisParser
import datetime

class EphemerisParserSpec(unittest.TestCase):

    def setUp(self):
    	self.single_ephemeris = ephemeris.singleEphemeris
        self.ephemerisTestISSPass1_1SecCompact = ephemeris.ephemerisTestISSPass1_1SecCompact
        self.ephemerisTestISSPass1_1Sec = ephemeris.ephemerisTestISSPass1_1Sec
        self.Parser = EphemerisParser()

    def test_parsing_of_single_ephemeris(self):
    	self.Parser.parse(self.single_ephemeris)[0] |should| include_keys('flag', 'azimuth', 'elevation', 'time')
    	self.Parser.parse(self.single_ephemeris) |should| have(2).ephemeris

    def test_parsing_of_compact_ephemeris(self):
		self.Parser.parse(self.ephemerisTestISSPass1_1SecCompact)[0] |should| include_keys('flag', 'azimuth', 'elevation', 'time')
		self.Parser.parse(self.ephemerisTestISSPass1_1SecCompact) |should| have(34).ephemeris

    def test_parsing_of_complete_ephemeris(self):

		self.Parser.parse(self.ephemerisTestISSPass1_1Sec)[0] |should| include_keys('flag', 'azimuth', 'elevation', 'time')
		self.Parser.parse(self.ephemerisTestISSPass1_1Sec) |should| have(312).ephemeris