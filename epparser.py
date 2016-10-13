
class EphemerisParser():

    def parse(self, ephemerisData):
        return map(lambda x: dict(zip(['time', 'azimuth',
         'elevation', 'flag'], x)), ephemerisData)