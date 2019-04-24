import json, time, requests
from stem import Signal
from urllib.request import urlopen
from stem.control import Controller

proxies = {
    'http': 'socks5://localhost:9050', 'https': 'socks5://localhost:9050'
}


def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)


for x in range(0, 15):
    renew_tor_ip()
    ipAddress = requests.get("http://api.ipify.org", proxies=proxies).text
    response = urlopen(f"http://ipinfo.io/{ipAddress}/json")
    data = json.load(response)
    city = data['city']
    country = data['country']
    region = data['region']
    provider = data['org']
    print(f"IP Address: {ipAddress} \t City: {city} \t Region: {region} \t Country: {country} \t Provider: {provider}")
    time.sleep(10)

