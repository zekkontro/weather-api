from flask import Flask, jsonify, request
from flask import make_response
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')  
def home():  
    return "Welcome";  


class Temperature:
    def __init__(self, weatherStatus, weatherTemperature, chanceOfRain):
        self.weatherStatus = weatherStatus
        self.weatherTemperature = weatherTemperature
        self.chanceOfRain = chanceOfRain


@app.route("/v1/latitude/<string:latitude>/longitude/<string:longitude>/tempUnit/<string:tempUnit>/lang/<string:lang>", methods=["GET"])
def getTemperature(longitude, latitude, tempUnit, lang):
    baseURL = "https://weather.com/"+lang +"/weather/today/l/"+latitude+","+longitude +"?par=google&temp=" + tempUnit if lang != None else "https://weather.com/weather/today/l/"+latitude+","+longitude +"?par=google&temp=" + tempUnit
    source = requests.get(baseURL)
    bs4 = BeautifulSoup(source.content, "html.parser")
    currentTemperature = Temperature( bs4.find("div", attrs={"class" : "CurrentConditions--phraseValue--2xXSr", "data-testid" : "wxPhrase"}).text, bs4.find("span", attrs={"data-testid" : "TemperatureValue", "class" : "CurrentConditions--tempValue--3KcTQ"}).text, bs4.find("div", attrs={"class" : "CurrentConditions--precipValue--RBVJT"}).find("span").text if str(bs4.find("div", attrs={"class" : "CurrentConditions--precipValue--RBVJT"})) != "None"  else "--") 
    morningTemperature = Temperature(str(bs4.find_all("svg", attrs={"class" : "Icon--icon--2AbGu Icon--fullTheme--3jU2v"})[0]) ,bs4.find_all("div", attrs={"data-testid" : "SegmentHighTemp", "class" : "Column--temp--2v_go"})[0].find("span").text , bs4.find_all("span", attrs={"class": "Column--precip--2H5Iw"})[0].text)
    afternoonTemperature = Temperature(str(bs4.find_all("svg", attrs={"class" : "Icon--icon--2AbGu Icon--fullTheme--3jU2v"})[1]) ,bs4.find_all("div", attrs={"data-testid" : "SegmentHighTemp", "class" : "Column--temp--2v_go"})[1].find("span").text , bs4.find_all("span", attrs={"class": "Column--precip--2H5Iw"})[1].text)
    eveningTemperature =  Temperature(str(bs4.find_all("svg", attrs={"class" : "Icon--icon--2AbGu Icon--fullTheme--3jU2v"})[2]) ,bs4.find_all("div", attrs={"data-testid" : "SegmentHighTemp", "class" : "Column--temp--2v_go"})[2].find("span").text , bs4.find_all("span", attrs={"class": "Column--precip--2H5Iw"})[2].text)
    overnightTemperature = Temperature(str(bs4.find_all("svg", attrs={"class" : "Icon--icon--2AbGu Icon--fullTheme--3jU2v"})[3]) ,bs4.find_all("div", attrs={"data-testid" : "SegmentHighTemp", "class" : "Column--temp--2v_go"})[3].find("span").text , bs4.find_all("span", attrs={"class": "Column--precip--2H5Iw"})[3].text)
    title = bs4.find("h1", attrs={"class" : "CurrentConditions--location--1Ayv3"}).text
    wind = bs4.find("span", attrs={"class" : "Wind--windWrapper--1Va1P undefined"}).text
    humidity = bs4.find("span", attrs={"data-testid": "PercentageValue"}).text
    dewPoint = bs4.find("div", attrs={"class" : "WeatherDetailsListItem--wxData--23DP5"}).find("span", attrs={"data-testid" : "TemperatureValue"}).text
    pressure = bs4.find("span", attrs={"class":"Pressure--pressureWrapper--3olKd undefined"}).text
    moonPhase = bs4.find_all("div", attrs={"class": "WeatherDetailsListItem--wxData--23DP5", "data-testid" : "wxData"})[-1].text
    sunriseTime = bs4.find_all("p", attrs={"class" : "SunriseSunset--dateValue--2nwgx"})[0].text
    sunsetTime = bs4.find_all("p", attrs={"class" : "SunriseSunset--dateValue--2nwgx"})[1].text
    highLowRate = bs4.find_all("div", attrs={"class" : "WeatherDetailsListItem--wxData--23DP5"})[0].text
    uvIndex = bs4.find("span", attrs={"data-testid" : "UVIndexValue"}).text
    totalResults = {
        "currentTemperature" : {
            "weatherTemperature" : currentTemperature.weatherTemperature,
            "chanceOfRain" : currentTemperature.chanceOfRain,
            "weatherStatus" : currentTemperature.weatherStatus
        },

        "morningTemperature" : {
            "weatherTemperature" : morningTemperature.weatherTemperature,
            "chanceOfRain" : morningTemperature.chanceOfRain,
        },
        "afternoonTemperature" : {
            "weatherTemperature" : afternoonTemperature.weatherTemperature,
            "chanceOfRain" : afternoonTemperature.chanceOfRain,
        },
        "eveningTemperature" : {
            "weatherTemperature" : eveningTemperature.weatherTemperature,
            "chanceOfRain" : eveningTemperature.chanceOfRain,
        },
        "overnightTemperature" : {
            "weatherTemperature" : overnightTemperature.weatherTemperature,
            "chanceOfRain" : overnightTemperature.chanceOfRain,
        },
        "title" : title,
        "wind" : wind,
        "humidity" : humidity,
        "dewPoint" : dewPoint,
        "pressure" : pressure,
        "highLowRate" : highLowRate,
        "moonPhase" : str(moonPhase),
        "sunriseTime" : sunriseTime,
        "uvIndex" : uvIndex,
        "sunsetTime" : sunsetTime,
        
    }

    return jsonify(totalResults)


@app.route("/v1/latitude/<string:latitude>/longitude/<string:longitude>/tempUnit/<string:tempUnit>", methods=["GET"])
def getTemperatureWithoutLang(longitude, latitude, tempUnit):
    baseURL = "https://weather.com/weather/today/l/"+latitude+","+longitude +"?par=google&temp=" + tempUnit 
    source = requests.get(baseURL)
    bs4 = BeautifulSoup(source.content, "html.parser")
    currentTemperature = Temperature( bs4.find("div", attrs={"class" : "CurrentConditions--phraseValue--2xXSr", "data-testid" : "wxPhrase"}).text, bs4.find("span", attrs={"data-testid" : "TemperatureValue", "class" : "CurrentConditions--tempValue--3KcTQ"}).text, bs4.find("div", attrs={"class" : "CurrentConditions--precipValue--RBVJT"}).find("span").text if str(bs4.find("div", attrs={"class" : "CurrentConditions--precipValue--RBVJT"})) != "None"  else "--") 
    morningTemperature = Temperature(str(bs4.find_all("svg", attrs={"class" : "Icon--icon--2AbGu Icon--fullTheme--3jU2v"})[0]) ,bs4.find_all("div", attrs={"data-testid" : "SegmentHighTemp", "class" : "Column--temp--2v_go"})[0].find("span").text , bs4.find_all("span", attrs={"class": "Column--precip--2H5Iw"})[0].text)
    afternoonTemperature = Temperature(str(bs4.find_all("svg", attrs={"class" : "Icon--icon--2AbGu Icon--fullTheme--3jU2v"})[1]) ,bs4.find_all("div", attrs={"data-testid" : "SegmentHighTemp", "class" : "Column--temp--2v_go"})[1].find("span").text , bs4.find_all("span", attrs={"class": "Column--precip--2H5Iw"})[1].text)
    eveningTemperature =  Temperature(str(bs4.find_all("svg", attrs={"class" : "Icon--icon--2AbGu Icon--fullTheme--3jU2v"})[2]) ,bs4.find_all("div", attrs={"data-testid" : "SegmentHighTemp", "class" : "Column--temp--2v_go"})[2].find("span").text , bs4.find_all("span", attrs={"class": "Column--precip--2H5Iw"})[2].text)
    overnightTemperature = Temperature(str(bs4.find_all("svg", attrs={"class" : "Icon--icon--2AbGu Icon--fullTheme--3jU2v"})[3]) ,bs4.find_all("div", attrs={"data-testid" : "SegmentHighTemp", "class" : "Column--temp--2v_go"})[3].find("span").text , bs4.find_all("span", attrs={"class": "Column--precip--2H5Iw"})[3].text)
    title = bs4.find("h1", attrs={"class" : "CurrentConditions--location--1Ayv3"}).text
    wind = bs4.find("span", attrs={"class" : "Wind--windWrapper--1Va1P undefined"}).text
    humidity = bs4.find("span", attrs={"data-testid": "PercentageValue"}).text
    dewPoint = bs4.find("div", attrs={"class" : "WeatherDetailsListItem--wxData--23DP5"}).find("span", attrs={"data-testid" : "TemperatureValue"}).text
    pressure = bs4.find("span", attrs={"class":"Pressure--pressureWrapper--3olKd undefined"}).text
    moonPhase = bs4.find_all("div", attrs={"class": "WeatherDetailsListItem--wxData--23DP5", "data-testid" : "wxData"})[-1].text
    sunriseTime = bs4.find_all("p", attrs={"class" : "SunriseSunset--dateValue--2nwgx"})[0].text
    sunsetTime = bs4.find_all("p", attrs={"class" : "SunriseSunset--dateValue--2nwgx"})[1].text
    highLowRate = bs4.find_all("div", attrs={"class" : "WeatherDetailsListItem--wxData--23DP5"})[0].text
    uvIndex = bs4.find("span", attrs={"data-testid" : "UVIndexValue"}).text
    totalResults = {
        "currentTemperature" : {
            "weatherTemperature" : currentTemperature.weatherTemperature,
            "chanceOfRain" : currentTemperature.chanceOfRain,
            "weatherStatus" : currentTemperature.weatherStatus
        },

        "morningTemperature" : {
            "weatherTemperature" : morningTemperature.weatherTemperature,
            "chanceOfRain" : morningTemperature.chanceOfRain,
        },
        "afternoonTemperature" : {
            "weatherTemperature" : afternoonTemperature.weatherTemperature,
            "chanceOfRain" : afternoonTemperature.chanceOfRain,
        },
        "eveningTemperature" : {
            "weatherTemperature" : eveningTemperature.weatherTemperature,
            "chanceOfRain" : eveningTemperature.chanceOfRain,
        },
        "overnightTemperature" : {
            "weatherTemperature" : overnightTemperature.weatherTemperature,
            "chanceOfRain" : overnightTemperature.chanceOfRain,
        },
        "title" : title,
        "wind" : wind,
        "humidity" : humidity,
        "dewPoint" : dewPoint,
        "pressure" : pressure,
        "highLowRate" : highLowRate,
        "moonPhase" : str(moonPhase),
        "sunriseTime" : sunriseTime,
        "uvIndex" : uvIndex,
        "sunsetTime" : sunsetTime,
        
    }

    return jsonify(totalResults)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'HTTP 404 Error': 'The content you looks for does not exist. Please check your request.'}), 404)

if __name__ =="__main__":      app.run(debug = True)