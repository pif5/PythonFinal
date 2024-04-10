# Model for handling expense information in the 'expense' sub-module.

class ParkExpense:
    def __init__(self, name, transportation, other_expenses):
        self.name = name
        self.transportation = transportation
        self.other_expenses = other_expenses

# Sample data structure for park expenses. This could be expanded or modified to include more detailed information.
park_expenses = [
    ParkExpense('Acadia National Park', 800, 400),
    ParkExpense('Crater Lake National Park', 600, 300),
    ParkExpense('Glacier National Park', 1000, 600),
    ParkExpense('Shenandoah National Park', 700, 350),
    ParkExpense('Great Smoky Mountains National Park', 1000, 500),
    ParkExpense('New River Gorge National Park Preserve', 800, 400),
    ParkExpense('Grand Teton National Park', 1200, 700),
    ParkExpense('Mount Rainier National Park', 900, 450),
    ParkExpense('Glacier Bay National Park and Preserve', 1500, 800),
    ParkExpense('Black Canyon of the Gunnison National Park', 1000, 550),
    ParkExpense('Capitol Reef National Park', 1200, 600),
    ParkExpense('Rocky Mountain National Park', 1000, 500),
    ParkExpense('Saguaro National Park', 1300, 700),
    ParkExpense('Olympic National Park', 900, 450),
    ParkExpense('Theodore Roosevelt National Park', 1100, 600),
]


