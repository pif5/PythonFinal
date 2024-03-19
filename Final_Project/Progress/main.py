import pandas as pd


class NationalPark: 
    def init(self, id, name, longitude, latitude): 
        self.id = id 
        self.name = name 
        self.longitude = longitude 
        self.latitude = latitude 
        self.visitors = 0
        self.weather = [] 
        self.expenses = []

    def add_visitor(self, visitor):
        self.visitors.append(visitor)

    def add_weather(self, weather):
        self.weather.append(weather)

    def add_expense(self, expense):
        self.expenses.append(expense)
    
class Visitors: 
    def init(self, year, month, number_of_visitors): 
        self.year = year 
        self.month = month 
        
        self.number_of_visitors = number_of_visitors

class Weather: 
    def init(self, year, month, day, weather): 
        self.year = year 
        self.month = month 
        self.day = day 
        self.weather = weather

class Expense: 
    def init(self, destination_name, travel_vehicle, cost): 
        self.destination_name = destination_name 
        self.travel_vehicle = travel_vehicle 
        self.cost = cost

class ParkInfo: 
    def init(self, terrain, climate, crowds): 
        self.terrain = terrain 
        self.climate = climate 
        self.crowds = crowds

def read_excel_file(file_path): 
    national_parks = [] 
    df = pd.read_excel(file_path) 
    for index, row in df.iterrows(): 
        park_name = row['ParkName'] 
        latitude = row['Location'] 
        longitude = row['NumberOfVisitors'] 
    return national_parks