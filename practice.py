import pygeoip
import socket

gi=pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
def printRecord(tgt):
    rec=gi.record_by_name(tgt)
    #print rec
    city=rec['city']
    region=rec['region_code']
    country=rec['country_name']
    long=rec['longitude']
    lat=rec['latitude']

    print '[+] Target: '+tgt+' Geo-Located'
    print '[+] '+str(region)+', '+str(country)
    print '[+] Latitude: '+str(lat)+', Longitude: '+str(long)

tgt=socket.gethostbyname('www.naver.com')
printRecord(tgt)