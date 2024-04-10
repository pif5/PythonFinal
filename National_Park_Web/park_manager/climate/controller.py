# Controller for the 'climate' sub-module, interfacing between the model and the views.

from .model import park_climates

def get_climate_by_park_name(park_name):
    """Returns climate for a specific park by name."""
    park = next((p for p in park_climates if p.name == park_name), None)
    return park.climate if park else None
