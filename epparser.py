class EphemerisParser():

    def __init__(self):

        self.ephemeris_parsed = []
        self.single_ephemeris = {}
        self.single_ephemeris['time'] = 0
        self.single_ephemeris['azimuth'] = {}
        self.single_ephemeris['elevation'] = {}