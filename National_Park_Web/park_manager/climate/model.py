# Model for handling climate information in the 'climate' sub-module.

class ParkClimate:
    def __init__(self, name, climate):
        self.name = name
        self.climate = climate

# Sample data structure for park climates. This could be expanded or modified to include more detailed information.
park_climates = [
    ParkClimate('Acadia National Park', 'Temperate'),
    ParkClimate('Crater Lake National Park','Temperate'),
    ParkClimate('Glacier National Park','Continental'),
    ParkClimate('Shenandoah National Park','Temperate'),
    ParkClimate('Great Smoky Mountains National Park','Temperate'),
    ParkClimate('New River Gorge National Park Preserve','Temperate'),
    ParkClimate('Grand Teton National Park','Temperate'),
    ParkClimate('Mount Rainier National Park','Temperate'),
    ParkClimate('Glacier Bay National Park and Preserve','Temperate'),
    ParkClimate('Black Canyon of the Gunnison National Park','Temperate'),
    ParkClimate('Capitol Reef National Park','Continental'),
    ParkClimate('Rocky Mountain National Park','Continental'),
    ParkClimate('Saguaro National Park','Arid'),
    ParkClimate('Olympic National Park','Temperate'),
    ParkClimate('Theodore Roosevelt National Park','Continental'),
]















