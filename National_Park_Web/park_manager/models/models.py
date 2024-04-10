parks_data = [
    {
        'name': 'Acadia National Park',
        'location': 'Maine',
        'visitors': '3.8 million',
        'climate': 'Temperate',
        'temperature': {
            'spring': '45°F	Cloudy',
            'summer': '70°F	Sunny',
            'fall': '55°F Rainy',
            'winter': '35°F	Snowy',
        },
        'expense': {
            'transportation': 800,
            'other': 400
        },
        'terrain': 'Coastal',
    },
    # Add additional parks here
]

def get_all_parks():
    """Returns a list of all parks."""
    return parks_data

def get_park_by_name(park_name):
    """Returns a single park matching the given name or None if not found."""
    return next((park for park in parks_data if park['name'] == park_name), None)

		
