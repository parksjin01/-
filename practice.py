#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import pygeoip
import dpkt
import socket

gi=pygeoip.GeoIP('/opt/GeoIp/Geo.dat')

def whoIs(tip):
    ip=gi.record_by_name(tip)
    try:
        return "("+ip['city']+', '+ip['country_name']+")"
    except:
        try:
            return "("+ip['country_name']+")"
        except:
            return "(None), "+tip


f=open('/Users/Knight/Desktop/tmp.s0i0.pcap')
pcap=dpkt.pcap.Reader(f)

for ts, buf in pcap:
    eth=dpkt.ethernet.Ethernet(buf)
    ip=eth.data
    dst=socket.inet_ntoa(ip.dst)
    src=socket.inet_ntoa(ip.src)
    print whoIs(src)+' --> '+whoIs(dst)