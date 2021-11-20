from flask import Flask, render_template, request
import requests 
from config import API_KEY

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/", methods=["GET","POST"])
def get_index():
    
    if request.method == "POST":
        city_name = request.form.get("city")     
         
        if not city_name:
            city_name = "Delhi"
        
        api_key = API_KEY
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(url)
        result = response.json()
        
        if result["cod"] == "404":
            return "<h1>City Not Found!</h1>"
        
        data = {
            "temp" : round(result["main"]["temp"] - 273.15),
            "humidity" : result["main"]["humidity"],
            "wind_speed" : result["wind"]["speed"],
            "country_name" : result["sys"]["country"]
        
        }

        return render_template("result.html", data=data, city_name=city_name)
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
