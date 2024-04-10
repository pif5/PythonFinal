# Controller for the 'location' sub-module, interfacing between the model and the views.

from .model import park_locations

def get_location_by_park_name(park_name):
    """Returns location for a specific park by name."""
    park = next((p for p in park_locations if p.name == park_name), None)
    return park.location if park else None
