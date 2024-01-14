from flask import Flask, request, render_template
import requests

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=["GET", "POST"])
def index():
    weather_data = ''
    error = 0
    city_name = ''
    
    if request.method == "POST":
        city_name = request.form.get("cityName")
        
        if city_name:
            weather_api_key = '12fc5b69d50b9ae9d1ef7069abb598d9'
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={weather_api_key}"
            
            try:
                weather_data = requests.get(url).json()

                if 'main' not in weather_data:
                    error = 1
            except requests.RequestException:
                error = 1

    return render_template('index.html', data=weather_data, city_name=city_name, error=error)

if __name__ == "__main__":
    app.run(debug=True)
