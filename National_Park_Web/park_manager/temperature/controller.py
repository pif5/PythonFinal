# Controller for the 'temperature' sub-module, interfacing between the model and the views.

from .model import park_temperatures

def get_temperature_by_park_name(park_name):
    """Returns temperature information for a specific park by name."""
    park = next((p for p in park_temperatures if p.name == park_name), None)
    if park:
        return {'spring': park.spring, 'summer': park.summer, 'fall': park.fall, 'winter': park.winter}
    return None
