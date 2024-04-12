from flask import Flask, render_template, url_for
from park_manager.models.models import get_all_parks, get_park_by_name

app = Flask(__name__)

@app.route('/')
def home():
    parks = get_all_parks()
    return render_template('index.html', parks=parks[:15])

@app.route('/park/<string:park_name>')
def park_details(park_name):
    park = get_park_by_name(park_name)
    if park:
        return render_template('park_details.html', park=park, park_name=park_name)
    else:
        return 'Park not found', 404

@app.route('/park/<string:park_name>/location')
def park_location(park_name):
    park = get_park_by_name(park_name)
    if park:
        return render_template('park_location.html', park=park)
    else:
        return 'Park not found', 404

# Additional routes for other categories
@app.route('/park/<string:park_name>/visitors')
def park_visitors(park_name):
    park = get_park_by_name(park_name)
    if park:
        return render_template('park_visitors.html', park=park)
    else:
        return 'Park not found', 404

@app.route('/park/<string:park_name>/climate')
def park_climate(park_name):
    park = get_park_by_name(park_name)
    if park:
        return render_template('park_climate.html', park=park)
    else:
        return 'Park not found', 404

@app.route('/park/<string:park_name>/temperature')
def park_temperature(park_name):
    park = get_park_by_name(park_name)
    if park:
        return render_template('park_temperature.html', park=park)
    else:
        return 'Park not found', 404

@app.route('/park/<string:park_name>/expense')
def park_expense(park_name):
    park = get_park_by_name(park_name)
    if park:
        return render_template('park_expense.html', park=park)
    else:
        return 'Park not found', 404

@app.route('/park/<string:park_name>/terrain')
def park_terrain(park_name):
    park = get_park_by_name(park_name)
    if park:
        return render_template('park_terrain.html', park=park)
    else:
        return 'Park not found', 404

if __name__ == '__main__':
    app.run(debug=True)