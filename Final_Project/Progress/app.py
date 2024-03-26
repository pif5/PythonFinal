from flask import Flask, render_template
import pandas as pd
from main import read_excel_file, print_park_info



app = Flask(__name__)

@app.route('/')
def home():
    file_path = '/Users/tr1ee/PythonFinal/Final_Project/Progress/National_Parks_Visitors.xlsx'
    national_parks = read_excel_file(file_path)
    return [park.name for park in national_parks]

