from machine import Pin, SoftI2C, UART
from time import sleep
# ESP32 Modbus

modbus_uart = UART(1, baudrate=9600, tx=32, rx=4)
#modbus_uart = UART(2,9600)
modbus_uart.init(9600,bits=8,parity=None,stop=1)
#byte_request = b'\x01\x03\x00\x02\x00\x02\x65\xCB' #01030002000265CB
#
#add_02= b'\x01\x06\x01\x00\x01\x02\x08\x67'   #address reg 0100
#byte_request = b'\x02\x03\x00\x02\x00\x02\x65\xF8'
#
add_03= b'\x01\x06\x01\x00\x01\x03\xC9\xA7'
byte_request = b'\x03\x03\x00\x02\x00\x02\x64\x29'
#
#add_04= b'\x01\x06\x01\x00\x01\x04\x88\x65'
#byte_request = b'\x04\x03\x00\x02\x00\x02\x65\x9E'

sleep(2) # to add new sesor 
modbus_uart.write(add_03)
sleep(0.01)

def sensor_value(start, last):
  t = 0
  t = start * 256
  t = t + last
  return t
#
def rd_byte_req(byte_request):
    modbus_uart.write(byte_request)
    sleep(0.01)
    moisture = 0.0
    temperature = 0.0
    tt=0
    while tt<20:
        if modbus_uart.any():
            byte_response = modbus_uart.read()
            moisture = sensor_value(byte_response[3], byte_response[4]) * 0.1 ;
            temperature = sensor_value(byte_response[5], byte_response[6]) * 0.1;
            #print('Moisture: {} %'.format(moisture))
            #print('Temperature: {} °C'.format(temperature))
            break
        tt= tt+1
        sleep(0.1)
    fault=False
    if tt==20: fault= True
    return moisture,temperature,fault
'''    
while True:
    #byte_request = b'\x01\x03\x00\x02\x00\x02\x65\xCB' #01030002000265CB
    byte_request = b'\x02\x03\x00\x02\x00\x02\x65\xF8'
    sl_ms1,sl_tp1,fault1=rd_byte_req(byte_request)
    print('Mois1: {} %'.format(sl_ms1),'Temp1: {} °C'.format(sl_tp1),'Falut1:',fault1)
    sleep(0.5)
    byte_request = b'\x02\x03\x00\x02\x00\x02\x65\xF8'
    sl_ms2,sl_tp2,fault2=rd_byte_req(byte_request)
    print('Mois2: {} %'.format(sl_ms2),'Temp2: {} °C'.format(sl_tp2),'Falut2:',fault2)
    sleep(0.5)
    #byte_request = b'\x03\x03\x00\x02\x00\x02\x64\x29'
    byte_request = b'\x02\x03\x00\x02\x00\x02\x65\xF8'
    sl_ms3,sl_tp3,fault3=rd_byte_req(byte_request)
    print('Mois3: {} %'.format(sl_ms3),'Temp3: {} °C'.format(sl_tp3),'Falut3:',fault3)
    sleep(0.5)
    #byte_request = b'\x04\x03\x00\x02\x00\x02\x65\x9E'
    byte_request = b'\x02\x03\x00\x02\x00\x02\x65\xF8'
    sl_ms4,sl_tp4,fault4=rd_byte_req(byte_request)
    print('Mois4: {} %'.format(sl_ms4),'Temp4: {} °C'.format(sl_tp4),'Falut4:',fault4)
    print()
    sleep(4)
'''