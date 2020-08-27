# This classes file isn't actually used, just a reminder to myself how 
# I should have written the code first time around. Object oriented.

class BaseCluster:
    def __init__(self, galaxy):
        self.iterations = galaxy[8]
        self.nuker_params = galaxy[4]
        self.spatial_data = self._get_spatial(galaxy)
        self.name = Galaxy[11]
    
    def _get_spatial(self, galaxy):
        return {'centre': galaxy[0], 'size': galaxy[1], 'angle': galaxy[2], 'eccentricity': galaxy[3]}

    def _get_image(self, galaxy):
        return {'offset': galaxy[5], 'grayscale': galaxy[6], 'rotation': galaxy[7]}



class Galaxy(BaseCluster):
    def __init__(self):
        super().__init__(self)

