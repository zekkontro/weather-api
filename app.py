from flask import Flask, jsonify, request
from flask import make_response
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')  
def home():  
    return """<h1 id="weather-api">Weather API</h1>
<p>Python api pulling weather data based on latitude and longitude data
SITE URL: </p>
<h3 id="author">Author</h3>
<h4 id="mustafa-berat-kurt-zekkontro">Mustafa Berat Kurt - zekkontro</h4>
<h5 id="-github-page-https-github-com-zekkontro-"><a href="https://github.com/zekkontro">Github Page</a></h5>
<h4 id="-instagram-page-https-www-instagram-com-brtwlf-"><a href="https://www.instagram.com/brtwlf/">Instagram Page</a></h4>
<h3 id="usage">Usage</h3>
<h5 id="requests">Requests</h5>
<pre><code>latitude =&gt; required
longitude =&gt; required
tempUnit =&gt; required (c =&gt; Celcius, f =&gt; Fahrenite)
lang =&gt; not required (Ex: tr-TR, de-DE ...)

Ex: /v1/latitude/<span class="hljs-string">"LATITUDE"</span>/longitude/<span class="hljs-string">"LONGITUDE"</span>/tempUnit/<span class="hljs-string">"TEMP-UNIT"</span>/lang/<span class="hljs-string">"LANG-COUNTRY"</span>
</code></pre><h5 id="response-example">Response Example</h5>
<pre><code>{
  <span class="hljs-attr">"afternoonTemperature"</span>: {
    <span class="hljs-attr">"chanceOfRain"</span>: <span class="hljs-string">"Regenwahrscheinlichkeit0%"</span>, 
    <span class="hljs-attr">"weatherTemperature"</span>: <span class="hljs-string">"11\u00b0"</span>
  }, 
  <span class="hljs-attr">"currentTemperature"</span>: {
    <span class="hljs-attr">"chanceOfRain"</span>: <span class="hljs-string">"--"</span>, 
    <span class="hljs-attr">"weatherStatus"</span>: <span class="hljs-string">"Heiter"</span>, 
    <span class="hljs-attr">"weatherTemperature"</span>: <span class="hljs-string">"3\u00b0"</span>
  }, 
  <span class="hljs-attr">"dewPoint"</span>: <span class="hljs-string">"12\u00b0"</span>, 
  <span class="hljs-attr">"eveningTemperature"</span>: {
    <span class="hljs-attr">"chanceOfRain"</span>: <span class="hljs-string">"Regenwahrscheinlichkeit4%"</span>, 
    <span class="hljs-attr">"weatherTemperature"</span>: <span class="hljs-string">"2\u00b0"</span>
  }, 
  <span class="hljs-attr">"highLowRate"</span>: <span class="hljs-string">"12\u00b0/-4\u00b0"</span>, 
  <span class="hljs-attr">"humidity"</span>: <span class="hljs-string">"63%"</span>, 
  <span class="hljs-attr">"moonPhase"</span>: <span class="hljs-string">"abnehmender Halbmond"</span>, 
  <span class="hljs-attr">"morningTemperature"</span>: {
    <span class="hljs-attr">"chanceOfRain"</span>: <span class="hljs-string">"--"</span>, 
    <span class="hljs-attr">"weatherTemperature"</span>: <span class="hljs-string">"0\u00b0"</span>
  }, 
  <span class="hljs-attr">"overnightTemperature"</span>: {
    <span class="hljs-attr">"chanceOfRain"</span>: <span class="hljs-string">"Regenwahrscheinlichkeit7%"</span>, 
    <span class="hljs-attr">"weatherTemperature"</span>: <span class="hljs-string">"-3\u00b0"</span>
  }, 
  <span class="hljs-attr">"pressure"</span>: <span class="hljs-string">"Arrow Down1024.0 mb"</span>, 
  <span class="hljs-attr">"sunriseTime"</span>: <span class="hljs-string">"7:26"</span>, 
  <span class="hljs-attr">"sunsetTime"</span>: <span class="hljs-string">"18:53"</span>, 
  <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Eski\u015fehir, Eski\u015fehir, T\u00fcrkei Wetter"</span>, 
  <span class="hljs-attr">"uvIndex"</span>: <span class="hljs-string">"3 von 10"</span>, 
  <span class="hljs-attr">"wind"</span>: <span class="hljs-string">"Wind Direction10 km/h"</span>
}
</code></pre><h3 id="license">LICENSE</h3>
<pre><code>MIT License

Copyright (c) 2021 Berat Kurt   
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to <span class="hljs-keyword">use</span>, copy, <span class="hljs-keyword">modify</span>, <span class="hljs-keyword">merge</span>, publish, <span class="hljs-keyword">distribute</span>, sublicense, <span class="hljs-keyword">and</span>/<span class="hljs-keyword">or</span> sell
copies <span class="hljs-keyword">of</span> the Software, <span class="hljs-keyword">and</span> <span class="hljs-keyword">to</span> permit persons <span class="hljs-keyword">to</span> whom the Software <span class="hljs-keyword">is</span>
furnished <span class="hljs-keyword">to</span> <span class="hljs-keyword">do</span> so, subject <span class="hljs-keyword">to</span> the <span class="hljs-keyword">following</span> conditions:
The above copyright <span class="hljs-keyword">notice</span> <span class="hljs-keyword">and</span> this permission <span class="hljs-keyword">notice</span> shall be included <span class="hljs-keyword">in</span> all
copies <span class="hljs-keyword">or</span> substantial portions <span class="hljs-keyword">of</span> the Software.
THE SOFTWARE <span class="hljs-keyword">IS</span> PROVIDED <span class="hljs-string">"AS IS"</span>, <span class="hljs-keyword">WITHOUT</span> WARRANTY <span class="hljs-keyword">OF</span> <span class="hljs-keyword">ANY</span> KIND, EXPRESS <span class="hljs-keyword">OR</span>
IMPLIED, <span class="hljs-keyword">INCLUDING</span> BUT <span class="hljs-keyword">NOT</span> LIMITED <span class="hljs-keyword">TO</span> THE WARRANTIES <span class="hljs-keyword">OF</span> MERCHANTABILITY,
FITNESS <span class="hljs-keyword">FOR</span> A PARTICULAR PURPOSE <span class="hljs-keyword">AND</span> NONINFRINGEMENT. <span class="hljs-keyword">IN</span> <span class="hljs-keyword">NO</span> <span class="hljs-keyword">EVENT</span> SHALL THE
<span class="hljs-keyword">AUTHORS</span> <span class="hljs-keyword">OR</span> COPYRIGHT HOLDERS BE LIABLE <span class="hljs-keyword">FOR</span> <span class="hljs-keyword">ANY</span> CLAIM, DAMAGES <span class="hljs-keyword">OR</span> OTHER
LIABILITY, WHETHER <span class="hljs-keyword">IN</span> AN <span class="hljs-keyword">ACTION</span> <span class="hljs-keyword">OF</span> CONTRACT, TORT <span class="hljs-keyword">OR</span> OTHERWISE, ARISING <span class="hljs-keyword">FROM</span>,
<span class="hljs-keyword">OUT</span> <span class="hljs-keyword">OF</span> <span class="hljs-keyword">OR</span> <span class="hljs-keyword">IN</span> <span class="hljs-keyword">CONNECTION</span> <span class="hljs-keyword">WITH</span> THE SOFTWARE <span class="hljs-keyword">OR</span> THE <span class="hljs-keyword">USE</span> <span class="hljs-keyword">OR</span> OTHER DEALINGS <span class="hljs-keyword">IN</span> THE
SOFTWARE.
</code></pre> """;  


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
