# Controller for the 'expense' sub-module, interfacing between the model and the views.

from .model import park_expenses

def get_expense_by_park_name(park_name):
    """Returns expense information for a specific park by name."""
    park = next((p for p in park_expenses if p.name == park_name), None)
    if park:
        return {'transportation': park.transportation, 'other': park.other_expenses}
    return None
