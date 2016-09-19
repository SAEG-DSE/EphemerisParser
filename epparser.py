from datetime import datetime
from time import strptime

class EphemerisParser():

    def __init__(self):

        self.ephemeris_parsed = []
        self.single_ephemeris = {}
        self.single_ephemeris['time'] = 0
        self.single_ephemeris['azimuth'] = {}
        self.single_ephemeris['elevation'] = {}
        self.single_ephemeris['flag'] = {}


    def parse(self, ephemerisData):
    
        for counter, ephemeris in enumerate(ephemerisData):
            if (counter>=0):

                self.single_ephemeris = {}
                self.single_ephemeris['time'] = 0
                self.single_ephemeris['azimuth'] = {}
                self.single_ephemeris['elevation'] = {}
                self.single_ephemeris['flag'] = {}
                
                time = datetime.strptime(ephemeris[0],'%Y-%m-%d %H:%M:%S')
                azimuth = ephemeris[1]
                elevation = ephemeris[2]
                flag = ephemeris[3]
                
                self.single_ephemeris['time'] = time
                self.single_ephemeris['azimuth'] = azimuth
                self.single_ephemeris['elevation'] = elevation
                self.single_ephemeris['flag'] = flag

                self.ephemeris_parsed.append(self.single_ephemeris)

        return self.ephemeris_parsed