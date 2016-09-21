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
    	self.Parser.parse(single_ephemeris) |should| include_keys('flag', 'azimuth', 'elevation', 'time')
    	self.Parser.parse(single_ephemeris) |should| contain([{'flag': 0, 'azimuth': 0.3539, 'elevation': 0.1238, 'time': datetime.datetime(2015, 12, 15, 0, 47, 50)}])

    def test_parsing_of_compact_ephemeris(self):
		self.Parser.parse(ephemerisTestISSPass1_1SecCompact) |should| include_keys('flag', 'azimuth', 'elevation', 'time')
		self.Parser.parse(ephemerisTestISSPass1_1SecCompact) |should| contain([{'flag': 0, 'azimuth': 39.1376, 'elevation': 10.0126, 'time': datetime.datetime(2014, 4, 25, 0, 51, 13)}, {'flag': 0, 'azimuth': 39.4224, 'elevation': 10.0443, 'time': datetime.datetime(2014, 4, 25, 0, 51, 15)}, {'flag': 0, 'azimuth': 39.7081, 'elevation': 10.0755, 'time': datetime.datetime(2014, 4, 25, 0, 51, 16)}, {'flag': 0, 'azimuth': 39.9945, 'elevation': 10.1063, 'time': datetime.datetime(2014, 4, 25, 0, 51, 17)}, {'flag': 0, 'azimuth': 40.2818, 'elevation': 10.1366, 'time': datetime.datetime(2014, 4, 25, 0, 51, 18)}, {'flag': 0, 'azimuth': 40.5698, 'elevation': 10.1665, 'time': datetime.datetime(2014, 4, 25, 0, 51, 18)}, {'flag': 0, 'azimuth': 40.8586, 'elevation': 10.1958, 'time': datetime.datetime(2014, 4, 25, 0, 51, 19)}, {'flag': 0, 'azimuth': 41.1482, 'elevation': 10.2248, 'time': datetime.datetime(2014, 4, 25, 0, 51, 20)}, {'flag': 0, 'azimuth': 41.4385, 'elevation': 10.2532, 'time': datetime.datetime(2014, 4, 25, 0, 51, 21)}, {'flag': 0, 'azimuth': 41.7296, 'elevation': 10.2811, 'time': datetime.datetime(2014, 4, 25, 0, 51, 23)}, {'flag': 0, 'azimuth': 42.0214, 'elevation': 10.3086, 'time': datetime.datetime(2014, 4, 25, 0, 51, 24)}, {'flag': 0, 'azimuth': 42.3139, 'elevation': 10.3356, 'time': datetime.datetime(2014, 4, 25, 0, 51, 25)}, {'flag': 0, 'azimuth': 42.6071, 'elevation': 10.362, 'time': datetime.datetime(2014, 4, 25, 0, 51, 25)}, {'flag': 0, 'azimuth': 42.9011, 'elevation': 10.388, 'time': datetime.datetime(2014, 4, 25, 0, 51, 26)}, {'flag': 0, 'azimuth': 43.1957, 'elevation': 10.4134, 'time': datetime.datetime(2014, 4, 25, 0, 51, 27)}, {'flag': 0, 'azimuth': 43.4909, 'elevation': 10.4384, 'time': datetime.datetime(2014, 4, 25, 0, 51, 28)}, {'flag': 0, 'azimuth': 43.7869, 'elevation': 10.4628, 'time': datetime.datetime(2014, 4, 25, 0, 51, 30)}])