# Weather API

Python api pulling weather data based on latitude and longitude data


### Author
#### Mustafa Berat Kurt - zekkontro
##### [Github Page](https://github.com/zekkontro)
#### [Instagram Page](https://www.instagram.com/brtwlf/)

### Usage
##### Latitude-Longitude Requests
	
    latitude => required
    longitude => required
    tempUnit => required (c => Celcius, f => Fahrenite)
    lang => not required (Ex: tr-TR, de-DE ...)
    
	Ex: /v1/latitude/"LATITUDE"/longitude/"LONGITUDE"/tempUnit/"TEMP-UNIT"/lang/"LANG-COUNTRY"

##### Get towns request

    https://weathersapi.herokuapp.com/v1/towns

##### Get Weathers by Town Name

    countryId => required (Ex: TR, US, FR...)
    townName => required (Ex: Erdemli, Eregli...)
    tempUnit => required (c => Celcius, f => Fahrenite)
    lang => not required (Ex: tr-TR, de-DE ...)
    
    	Ex: /v1/country/<countryId>/town/<townName>/tempUnit/<tempUnit>
	    /v1/country/<countryId>/town/<townName>/lang/<lang>/tempUnit/<tempUnit>

##### Response Example

    {
      "afternoonTemperature": {
        "chanceOfRain": "Regenwahrscheinlichkeit0%", 
        "weatherTemperature": "11\u00b0"
      }, 
      "currentTemperature": {
        "chanceOfRain": "--", 
        "weatherStatus": "Heiter", 
        "weatherTemperature": "3\u00b0"
      }, 
      "dewPoint": "12\u00b0", 
      "eveningTemperature": {
        "chanceOfRain": "Regenwahrscheinlichkeit4%", 
        "weatherTemperature": "2\u00b0"
      }, 
      "highLowRate": "12\u00b0/-4\u00b0", 
      "humidity": "63%", 
      "moonPhase": "abnehmender Halbmond", 
      "morningTemperature": {
        "chanceOfRain": "--", 
        "weatherTemperature": "0\u00b0"
      }, 
      "overnightTemperature": {
        "chanceOfRain": "Regenwahrscheinlichkeit7%", 
        "weatherTemperature": "-3\u00b0"
      }, 
      "pressure": "Arrow Down1024.0 mb", 
      "sunriseTime": "7:26", 
      "sunsetTime": "18:53", 
      "title": "Eski\u015fehir, Eski\u015fehir, T\u00fcrkei Wetter", 
      "uvIndex": "3 von 10", 
      "wind": "Wind Direction10 km/h"
    }


### LICENSE

    MIT License
 
    Copyright (c) 2021 Berat Kurt   
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
