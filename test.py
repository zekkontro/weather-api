
import requests
from bs4 import BeautifulSoup

baseURL = "https://weather.com/weather/today/l/39.76,30.52?par=google&temp=c"
source = requests.get(baseURL)
bs4 = BeautifulSoup(source.content, "html.parser")
print(str(bs4.find("div", attrs={"class" : "CurrentConditions--precipValue--RBVJT"})))