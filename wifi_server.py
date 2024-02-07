# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket  
except:
  import socket

import os
import sys

import network

import esp
esp.osdebug(None)

import gc
gc.collect()
import utime

def web_page():
    html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body><h1>Hello, World!</h1></body></html>"""
    return html
def run_wifi_server():
    ssid = 'SOIL_IITM_AP' #'MicroPython-AP'
    password = '123456789'

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid) #, password=password)

    while ap.active() == False:
      pass

    print('AP created successful')
    print(ap.ifconfig())

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    print('in s.accept()..')
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    utime.sleep(1)
    return conn, addr
#while True:
def get_pic(conn):  
  conn.send('&click\r\n')
  utime.sleep(4)
  flns = conn.recv(1024)
  flns_str= str(flns.decode("utf-8"))
  print('flns_str:', flns_str)
  
  f=open('pic_img1.jpg','w')
  flns_int = int(flns)
  #for i in range (flns_int):
  flns_int_rem = flns_int
  flns_tl = 0
  pics_tl = 0
  while True:
      if flns_int_rem > 1024:
          pics = conn.recv(1024)
          f.write(pics)
          flns_tl= flns_tl+1024
          utime.sleep(0.2)
          flns_int_rem=flns_int_rem-1024
          print('len(pics):', len(pics))
          pics_tl = pics_tl+ len(pics)
          
          
      else:
          pics = conn.recv(flns_int_rem)
          f.write(pics)
          flns_tl=flns_tl+ flns_int_rem
          utime.sleep(0.2)
          print('len(pics)@else:', len(pics))
          pics_tl = pics_tl+ len(pics)
          break
  f.close()
  print('flns_tl:', flns_tl)
  print('pics_tl:', pics_tl)
          
  #conn.close()
'''
conn, addr=run_wifi_server()
utime.sleep(2)
get_pic(conn)
'''

