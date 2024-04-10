# Controller for the 'terrain' sub-module, interfacing between the model and the views.

from .model import park_terrains

def get_terrain_by_park_name(park_name):
    """Returns terrain for a specific park by name."""
    park = next((p for p in park_terrains if p.name == park_name), None)
    return park.terrain if park else None
