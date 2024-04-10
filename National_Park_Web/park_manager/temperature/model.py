# Model for handling temperature information in the 'temperature' sub-module.

class ParkTemperature:
    def __init__(self, name, spring, summer, fall, winter):
        self.name = name
        self.spring = spring
        self.summer = summer
        self.fall = fall
        self.winter = winter

# Sample data structure for park temperatures. This could be expanded or modified to include more detailed information.
park_temperatures = [
    ParkTemperature('Acadia National Park', '45°F Cloudy', '70°F Sunny', '55°F Rainy', '35°F Snowy'),
    ParkTemperature('Crater Lake National Park', '55°F Sunny',	'68°F Cloudy', '60°F Rainy', '40°F Snowy'),
    ParkTemperature('Glacier National Park','40°F Cloudy', '65°F Sunny', '50°F Rainy', '30°F Snowy'),
    ParkTemperature('Shenandoah National Park','55°F Sunny', '70°F Cloudy',	'60°F Rainy', '40°F	Snowy'),
    ParkTemperature('Great Smoky Mountains National Park','50°F	Cloudy', '75°F Sunny', '55°F Rainy', '35°F Snowy'),
    ParkTemperature('New River Gorge National Park Preserve','60°F Sunny',	'75°F Cloudy', '65°F Rainy', '45°F Snowy'),
    ParkTemperature('Grand Teton National Park','45°F Cloudy', '70°F Sunny', '55°F Rainy', '35°F Snowy'),
    ParkTemperature('Mount Rainier National Park','50°F	Rainy',	'65°F Cloudy', '55°F Sunny', '40°F Snowy'),
    ParkTemperature('Glacier Bay National Park and Preserve','40°F Sunny',	'55°F Cloudy', '45°F Rainy', '30°F Snowy'),
    ParkTemperature('Black Canyon of the Gunnison National Park','55°F Sunny', '75°F Cloudy', '60°F	Rainy',	'40°F Snowy'),
    ParkTemperature('Capitol Reef National Park','65°F Sunny',	'85°F Cloudy', '70°F Rainy', '50°F Snowy'),
    ParkTemperature('Rocky Mountain National Park','45°F Cloudy', '70°F	Sunny',	'55°F Rainy', '35°F	Snowy'),
    ParkTemperature('Saguaro National Park','70°F Sunny', '95°F Cloudy', '80°F Rainy', '60°F Sunny'),
    ParkTemperature('Olympic National Park','55°F Rainy', '70° FCloudy', '60°F Sunny', '40°F Snowy'),
    ParkTemperature('Theodore Roosevelt National Park','45°F Sunny', '65°F Cloudy',	'55°F Rainy', '35°F	Snowy'),
]













