class Map:
    # class that stores all map fields
    def __init__(self, map):
        self.map = map
        self.all_fields = []
    def generate_map(self):
        """
        Generates map based on map.txt.
        Map is a list of objects (individual fields) with location, altitude etc.
        """
        i = 0
        for line in self.map:
            j = 0
            line = line.split('\n')[0]
            for cell in line:
                field = Map_field(location=[i, j], altitude=cell)
                self.all_fields.append(field)
                j += 1
            i += 1

class Map_field: 
    # class that stores location and altitude of one field and what whiecles are there
    def __init__(self, location, altitude):
        self.location = location
        self.altitude = altitude
        self.vehicles = []
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)