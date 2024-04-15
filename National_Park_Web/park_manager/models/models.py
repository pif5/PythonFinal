parks_data = [
    {
        'name': 'Acadia National Park',
        'location': 'Maine',
        'image':'/images/acadia.jpeg',
        'visitors': '3.8 million',
        'climate': 'Temperate',
        'temperature': {
            'spring': '45°F Cloudy',
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
    {
        'name': 'Crater Lake National Park',
        'location': 'Oregon',
        'image':'/images/carter.jpeg',
        'visitors': '559,976',
        'climate': 'Temperate',
        'temperature': {
            'spring': '55°F	Sunny',
            'summer': '68°F	Cloudy',
            'fall': '60°F Rainy',
            'winter': '40°F	Snowy',
        },
        'expense': {
            'transportation': 600,
            'other': 300
        },
        'terrain': 'Mountainous',
    },
    {
        'name': 'Glacier National Park',
        'location': 'Montana',
        'image':'/images/glacier.jpeg',
        'visitors': 'Nearly 3 million',
        'climate': 'Continental',
        'temperature': {
            'spring': '40°F	Cloudy',
            'summer': '65°F	Sunny',
            'fall': '50°F Rainy',
            'winter': '30°F	Snowy',
        },
        'expense': {
            'transportation': 1000,
            'other': 600
        },
        'terrain': 'Mountainous',
    },
    {
        'name': 'Shenandoah National Park',
        'location': 'Virginia',
        'image':'/images/shenandoah.jpeg',
        'visitors': '1.4 million',
        'climate': 'Temperate',
        'temperature': {
            'spring': '55°F	Sunny',
            'summer': '70°F	Cloudy',
            'fall': '60°F Rainy',
            'winter': '40°F	Snowy',
        },
        'expense': {
            'transportation': 700,
            'other': 350
        },
        'terrain': 'Mountainous',
    },
    {
        'name': 'Great Smoky Mountains National Park',
        'location': 'Tennessee and North Carolina',
        'image':'/images/great_somky.jpeg',
        'visitors': '13.3 million',
        'climate': 'Temperate',
        'temperature': {
            'spring': '50°F	Cloudy',
            'summer': '75°F	Sunny',
            'fall': '55°F Rainy',
            'winter': '35°F	Snowy',
        },
        'expense': {
            'transportation': 1000,
            'other': 500
        },
        'terrain': 'Mountainous',
    },
    {
        'name': 'New River Gorge National Park Preserve',
        'location': 'West Virginia',
        'image':'/images/new_river.webp',
        'visitors': '1,709,623',
        'climate': 'Temperate',
        'temperature': {
            'spring': '60°F	Sunny',
            'summer': '75°F	Cloudy',
            'fall': '65°F	Rainy',
            'winter': '45°F	Snowy',
        },
        'expense': {
            'transportation': 800,
            'other': 400
        },
        'terrain': 'Mountainous',
    },
    {
        'name': 'Grand Teton National Park',
        'location': 'Wyoming',
        'image':'/images/grand.jpeg',
        'visitors': '3,417,106',
        'climate': 'Continental',
        'temperature': {
            'spring': '45°F	Cloudy',
            'summer': '70°F	Sunny',
            'fall': '55°F Rainy',
            'winter': '35°F	Snowy',
        },
        'expense': {
            'transportation': 1200,
            'other': 700
        },
        'terrain': 'Mountainous',
    },
    {
        'name': 'Mount Rainier National Park',
        'location': 'Washington',
        'image':'/images/mount.png',
        'visitors': '1.67 million',
        'climate': 'Temperate',
        'temperature': {
            'spring': '50°F	Rainy',
            'summer': '65°F	Cloudy',
            'fall': '55°F Sunny',
            'winter': '40°F	Snowy',
        },
        'expense': {
            'transportation': 900,
            'other': 450
        },
        'terrain': 'Mountainous',
    },
    {
        'name': 'Glacier Bay National Park and Preserve',
        'location': 'Alaska',
        'image':'/images/glacier_bay.jpeg',
        'visitors': '703,659',
        'climate': 'Temperate',
        'temperature': {
            'spring': '40°F	Sunny',
            'summer': '55°F	Cloudy',
            'fall': '45°F Rainy',
            'winter': '30°F	Snowy',
        },
        'expense': {
            'transportation': 1500,
            'other': 800
        },
        'terrain': 'Coastal',
    },
    {
        'name': 'Black Canyon of the Gunnison National Park',
        'location': 'Colorado',
        'image':'/images/black_canyon.png',
        'visitors': '357,069',
        'climate': 'Temperate',
        'temperature': {
            'spring': '55°F	Sunny',
            'summer': '75°F	Cloudy',
            'fall': '60°F Rainy',
            'winter': '40°F	Snowy',
        },
        'expense': {
            'transportation': 1000,
            'other': 550
        },
        'terrain': 'Mountainous',
    },
    {
        'name': 'Capitol Reef National Park',
        'location': 'Utah',
        'image':'/images/capitol.jpeg',
        'visitors': 'Nearly 1.2 million',
        'climate': 'Continental',
        'temperature': {
            'spring': '65°F	Sunny',
            'summer': '85°F	Cloudy',
            'fall': '70°F	Rainy',
            'winter': '50°F	Snowy',
        },
        'expense': {
            'transportation': 1200,
            'other': 600
        },
        'terrain': 'Desert',
    },
    {
        'name': 'Saguaro National Park',
        'location': 'Arizona',
        'image':'/images/saguaro.jpeg',
        'visitors': '908,000',
        'climate': 'Arid',
        'temperature': {
            'spring': '70°F	Sunny',
            'summer': '95°F	Cloudy',
            'fall': '80°F Rainy',
            'winter': '60°F	Sunny',
        },
        'expense': {
            'transportation': 1300,
            'other': 700
        },
        'terrain': 'Desert',
    },
    {
        'name': 'Olympic National Park',
        'location': 'Washington',
        'image':'/images/olympic.webp',
        'visitors': '2.9 million',
        'climate': 'Temperate',
        'temperature': {
            'spring': '55°F	Rainy',
            'summer': '70°F	Cloudy',
            'fall': '60°F Sunny',
            'winter': '40°F	Snowy',
        },
        'expense': {
            'transportation': 900,
            'other': 450
        },
        'terrain': 'Coastal',
    },
    {
        'name': 'Theodore Roosevelt National Park',
        'location': 'North Dakota',
        'image':'/images/theodore.webp',
        'visitors': 'Nearly 600,000',
        'climate': 'Continental',
        'temperature': {
            'spring': '45°F	Sunny',
            'summer': '765°F Cloudy',
            'fall': '655°F Rainy',
            'winter': '35°F	Snowy',
        },
        'expense': {
            'transportation': 1100,
            'other': 600
        },
        'terrain': 'Plains',
    },
]

def get_all_parks():
    """Returns a list of all parks."""
    return parks_data

def get_park_by_name(park_name):
    """Returns a single park matching the given name or None if not found."""
    return next((park for park in parks_data if park['name'] == park_name), None)

		
