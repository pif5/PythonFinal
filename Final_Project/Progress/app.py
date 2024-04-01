# from flask import Flask
# import pandas as pd
# from main import read_excel_file, print_park_info



# app = Flask(__name__)

# @app.route('/')
# def home():
#     file_path = '/Users/tr1ee/PythonFinal/Final_Project/Progress/National_Parks_Visitors.xlsx'
#     national_parks = read_excel_file(file_path)
#     return [park.name for park in national_parks]

from flask import Flask, render_template_string
import pandas as pd
from main import read_excel_file, NationalPark

app = Flask(__name__)

@app.route('/')
def home():
    file_path = '/Users/tr1ee/PythonFinal/Final_Project/Progress/National_Parks_Visitors.xlsx'
    national_parks = read_excel_file(file_path)

    parks_info_html = "<h1>National Parks</h1>"
    for park in national_parks:
        parks_info_html += f"<p><strong>Name:</strong> {park.name}, <strong>Location:</strong> {park.location}, <strong>Visitors:</strong> {park.visitors}</p>"

    return render_template_string(parks_info_html)

if __name__ == '__main__':
    app.run(debug=True)
