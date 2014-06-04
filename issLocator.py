import urllib, json, threading
from pygeocoder import Geocoder

url= "https://api.wheretheiss.at/v1/satellites/25544";

def Fetch():
	response = urllib.urlopen(url)
        data = json.loads(response.read())
        lat = data['latitude']
        lon = data['longitude']       
	try:
		addr =  Geocoder.reverse_geocode(lat, lon)
		return lat, lon, addr
	except:
		return 0,0

if __name__ == "__main__":
	Lat, Lon, Addr = Fetch()
	print "Lat: {}\nLon: {}\nAddress: {}".format(Lat, Lon, Addr)
