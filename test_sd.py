import sdcard  
import os,utime
from machine import SoftSPI, Pin
spi=SoftSPI(baudrate=1000,polarity=1,
    phase=0,sck=Pin(25),
    mosi=Pin(13),miso=Pin(12))
spi.init(baudrate=1000)
spi.read(2) 
sd=sdcard.SDCard(spi,Pin(19))
utime.sleep(0.2)
os.mount(sd,'/sd')
print(os.listdir())
os.chdir('/sd')
