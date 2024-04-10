# Model for handling terrain information in the 'terrain' sub-module.

class ParkTerrain:
    def __init__(self, name, terrain):
        self.name = name
        self.terrain = terrain

# Sample data structure for park terrains. This could be expanded or modified to include more detailed information.
park_terrains = [
    ParkTerrain('Acadia National Park', 'Mountainous'),
    ParkTerrain('Crater Lake National Park','Coastal'),
    ParkTerrain('Glacier National Park','Mountainous'),
    ParkTerrain('Shenandoah National Park','Mountainous'),
    ParkTerrain('Great Smoky Mountains National Park','Mountainous'),
    ParkTerrain('New River Gorge National Park Preserve','Mountainous'),
    ParkTerrain('Grand Teton National Park','Mountainous'),
    ParkTerrain('Mount Rainier National Park','Mountainous'),
    ParkTerrain('Glacier Bay National Park and Preserve','Coastal'),
    ParkTerrain('Black Canyon of the Gunnison National Park','Mountainous'),
    ParkTerrain('Capitol Reef National Park','Desert'),
    ParkTerrain('Rocky Mountain National Park','Mountainous'),
    ParkTerrain('Saguaro National Park','Desert'),
    ParkTerrain('Olympic National Park','Coastal'),
    ParkTerrain('Theodore Roosevelt National Park','Plains'),
]











