import urllib.request
import json


def whats_the_weather(location):

    if location is None or location == "":
        print("location cannot be null")
        return

    urlrequest = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID=bd626856cc18501d26f9a0333c130521"
    page = urllib.request.urlopen(urlrequest).read().decode('utf8', 'ignore')

    json_output = json.loads(page)

    print(json_output['weather'])

if __name__ == '__main__':
    whats_the_weather('Nairobi')