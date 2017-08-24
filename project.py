import urllib
import json

url = "http://ip-api.com/json"
content = urllib.urlopen(url).read()
data = json.loads(content)
city = data["city"]
country = data["country"]
lat = data["lat"]
lon = data["lon"]
print "\nYour location is: %s, %s" %(city, country)

weather_url = "http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=9a3f5c783ac3e84bc0436fbcb453ffe8" %(lat, lon)
weather_content = urllib.urlopen(weather_url).read()
weather_data = json.loads(weather_content)
try:
    weather_condition = weather_data["weather"][0]["main"]
    print "\nWeather Condition: %s" %(weather_condition)
except:
    pass
try:
    weather_temp = 1.8 * (int(weather_data["main"]["temp"]) - 273) + 32
    print "\nCurrent Temperature: %s F" %(weather_temp)
except:
    pass
try:
    weather_humidity = weather_data["main"]["humidity"]
    print "Humidity: %s %%" %(weather_humidity)
except:
    pass
try:
    weather_temp_max = 1.8 * (int(weather_data["main"]["temp_max"]) - 273) + 32
    weather_temp_min = 1.8 * (int(weather_data["main"]["temp_min"]) -273) + 32
    print "\nToday's High: %s F" %(weather_temp_max)
    print "Today's Low: %s F" %(weather_temp_min)
except:
    pass
try:
    weather_wind_speed = round(int(weather_data["wind"]["speed"]) * 0.000621371 * 60 * 60, 2)
    weather_wind_deg = weather_data["wind"]["deg"]
    print "\nWind Speed: %s MPH" %(weather_wind_speed)
    print "Wind Degree: %s degrees" %(weather_wind_deg)
except:
    pass
try:
    weather_sunrise = weather_data["sys"]["sunrise"]
    sunrise_converter_url = "http://www.convert-unix-time.com/api?timestamp=%s&timezone=current" %(weather_sunrise)
    weather_sunrise_converted = json.loads(urllib.urlopen(sunrise_converter_url).read())["localDate"]
    weather_sunset = weather_data["sys"]["sunset"]
    sunset_converter_url = "http://www.convert-unix-time.com/api?timestamp=%s&timezone=current" %(weather_sunset)
    weather_sunset_converted = json.loads(urllib.urlopen(sunset_converter_url).read())["localDate"]
    print "\nToday's Sunrise: %s" %(weather_sunrise_converted)
    print "Today's Sunset: %s" %(weather_sunset_converted)
except:
    pass
