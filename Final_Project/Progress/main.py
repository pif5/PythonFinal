import pandas as pd

class NationalPark: 
    def __init__(self, name, location, visitors=0):
        self.name = name
        self.location = location
        self.visitors = visitors
        self.weather = []
        self.expenses = []

    def add_visitor(self, visitor):
        self.visitors.append(visitor)

    def add_weather(self, weather):
        self.weather.append(weather)

    def add_expense(self, expense):
        self.expenses.append(expense)
    
class Visitors: 
    def __init__(self, year, month, number_of_visitors): 
        self.year = year 
        self.month = month 
        self.number_of_visitors = number_of_visitors

class Weather: 
    def __init__(self, year, month, day, weather): 
        self.year = year 
        self.month = month 
        self.day = day 
        self.weather = weather

class Expense: 
    def __init__(self, destination_name, travel_vehicle, cost): 
        self.destination_name = destination_name 
        self.travel_vehicle = travel_vehicle 
        self.cost = cost

class ParkInfo: 
    def __init__(self, terrain, climate, crowds): 
        self.terrain = terrain 
        self.climate = climate 
        self.crowds = crowds

def read_excel_file(file_path):
    national_parks = []
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        park_name = row['ParkName']
        location = row['Location']
        visitors = row['NumberOfVisitors']
        national_park = NationalPark(park_name, location, visitors)
        national_parks.append(national_park)
    return national_parks

def print_park_info(national_parks):
    for park in national_parks:
        print(f"Name: {park.name}, Location: {park.location}, Visitors: {park.visitors}")


#run when directly executed
if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement. 
    file_path = '/Users/tr1ee/PythonFinal/Final_Project/Progress/National_Parks_Visitors.xlsx'
    national_parks = read_excel_file(file_path)
    print_park_info(national_parks)
