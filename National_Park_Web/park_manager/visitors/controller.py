# Controller for the 'visitors' sub-module, interfacing between the model and the views.

from .model import park_visitors

def get_visitors_by_park_name(park_name):
    """Returns annual visitors for a specific park by name."""
    park = next((p for p in park_visitors if p.name == park_name), None)
    return park.annual_visitors if park else None
