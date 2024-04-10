# Controller for the 'name' sub-module, interfacing between the model and the views.

from .model import park_names

def get_all_park_names():
    """Returns a list of all park names."""
    return [park.name for park in park_names]
