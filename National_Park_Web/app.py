from flask import Flask, render_template
from pet_manager.profiles.view import profile_view
from pet_manager.healthcare.view import healthcare_view
from pet_manager.adoption.view import adoption_view

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/profile')
def profiles():
    return profile_view()

@app.route('/healthcare')
def healthcare():
    return healthcare_view()

@app.route('/adoption')
def adoption():
    return adoption_view()

# run the app if the code is directly
if __name__ == '__main__':
    app.run(debug=True)