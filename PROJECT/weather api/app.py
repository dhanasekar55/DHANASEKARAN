from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = '0985ef16cb4673555a2d6a394c88b1b5'  # Replace with your OpenWeatherMap API key
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(base_url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = None

    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
