from machine import Pin, ADC, SoftI2C
import machine, onewire, ds18x20
import utime
import soil_ht3
import BME680_ht
#
utime.sleep(1)
bat = ADC(Pin(33)) #Battery Voltage
bat.atten(ADC.ATTN_11DB)

# fault registers
fault_bat = False
fault_SM1  = False
fault_SM2  = False
fault_SM3 = False
fault_SM4 = False
fault_ST1  = False # for soil temp.
fault_ST2  = False # for soil temp.
fault_ST3  = False # for soil temp.
fault_ST4  = False # for soil temp.
fault_HT = False  #
fault_AP  = False # air preassure

low_bat_rg = 8.0
#while True:
def rd_sens():
    #global mnt_rg
    #soil moisture
    global fault_bat,fault_SM1,fault_SM2,fault_SM3,fault_SM4,fault_ST1,fault_ST2,fault_ST3,fault_ST4,fault_HT,fault_AP
    global low_bat_rg
    
    global bat, pot1,pot2,pot3,pot4
    global sensor,bme,roms,ds_sensor
    bat_value = bat.read()
    bat_v = '%5.2f'%(12.3/3060*bat_value) #+'v'
    if float(bat_v)> low_bat_rg:
        fault_bat= False
    else:
        fault_bat= True
        
    #For reading Soil moisture and Soil temparature
        
    byte_request = b'\x01\x03\x00\x02\x00\x02\x65\xCB' #01030002000265CB
   # byte_request = b'\x02\x03\x00\x02\x00\x02\x65\xF8' # previous code address
    vp1,stp_f1,fault_SM1=soil_ht3.rd_byte_req(byte_request)
    #print('Mois1: {} %'.format(vp1),'Temp1: {} °C'.format(stp_f1),'Falut1:',fault_SM1)
    utime.sleep(0.5)
    byte_request = b'\x02\x03\x00\x02\x00\x02\x65\xF8'
    vp2,stp_f2,fault_SM2=soil_ht3.rd_byte_req(byte_request)
    #print('Mois2: {} %'.format(vp2),'Temp2: {} °C'.format(stp_f2),'Falut2:',fault_SM2)
    utime.sleep(0.5)
    byte_request = b'\x03\x03\x00\x02\x00\x02\x64\x29'
    #byte_request = b'\x02\x03\x00\x02\x00\x02\x65\xF8' # old adress of third sesnor
    vp3,stp_f3,fault_SM3=soil_ht3.rd_byte_req(byte_request)
    #print('Mois3: {} %'.format(vp3),'Temp3: {} °C'.format(stp_f3),'Falut3:',fault_SM3)
    utime.sleep(0.5)
    byte_request = b'\x04\x03\x00\x02\x00\x02\x65\x9E'
    #byte_request = b'\x02\x03\x00\x02\x00\x02\x65\xF8'
    vp4,stp_f4,fault_SM4=soil_ht3.rd_byte_req(byte_request)
    #print('Mois4: {} %'.format(vp4),'Temp4: {} °C'.format(stp_f4),'Falut4:',fault_SM4)
    #print()
    utime.sleep(0.5)
    fault_ST1= fault_SM1
    fault_ST2= fault_SM2
    fault_ST3= fault_SM3
    fault_ST4= fault_SM4
    #air temp, humidity and air pressue 
    temp=0.0
    hum = 0.0
    falt_HT = False
    fault_AP = False
    hum,temp,pres,fault_HT = BME680_ht.read_ATH() #hum,temp,fault= read_ATH()
    fault_AP = fault_HT
    ####   
    if fault_bat: # False
        batv_str = 'BATTERY:' + 'FAULT!'
 
    if fault_SM1 :
        sm_str1 = 'SM1:' + 'FAULT!'
    else:
        sm_str1 = 'SM1:' + '%5.1f' %vp1 + '%'
    if fault_SM2 :
        sm_str2 = 'SM2:' + 'FAULT!'
    else:
        sm_str2 = 'SM2:' + '%5.1f' %vp2 + '%'
    if fault_SM3 :
        sm_str3 = 'SM3:' + 'FAULT!'
    else:
        sm_str3 = 'SM3:' + '%5.1f' %vp3 + '%'
    if fault_SM4 :
        sm_str4 = 'SM4:' + 'FAULT!'
    else:
        sm_str4 = 'SM4:' + '%5.1f' %vp4 + '%'
    
    if fault_ST1 :
        st_str1 = 'ST1:' +  'FAULT!'
    else:
        st_str1 = 'ST1:' + '%5.1f' %stp_f1 + 'C'
    if fault_ST2 :
        st_str2 = 'ST2:' +  'FAULT!'
    else:
        st_str2 = 'ST2:' + '%5.1f' %stp_f2 + 'C'
    if fault_ST3 :
        st_str3 = 'ST3:' +  'FAULT!'
    else:
        st_str3 = 'ST3:' + '%5.1f' %stp_f3 + 'C'
    if fault_ST4 :
        st_str4 = 'ST4:' +  'FAULT!'
    else:
        st_str4 = 'ST4:' + '%5.1f' %stp_f4 + 'C'
    if fault_HT :
        ah_str = 'ARH:' +  'FAULT!'
    else:
        ah_str = 'ARH:' + '%5.1f' %hum +'%'
    if fault_HT :
        at_str = 'ART:' +  'FAULT!'
    else:
        at_str = 'ART:' + '%5.1f' %temp +'C'
    if fault_AP :
        ap_str = 'ARP:' +  'FAULT!'
    else:
        ap_str = 'ARP:' + pres #'AP:' + '%7.2f' %pres +'hPa'       
    ###
    data = '' 
    store_rg =1
    if store_rg == 1: 
        if fault_SM1 :
            data = 'xx.x'
        else:
            stt= sm_str1.split(':')     #pres_vl= str(pres[0:len(pres)-3]) 
            st =stt[1]
            st= st[0:len(st)-1]
            #data = data+','+ st
            data =  st
            
        if fault_SM2 :
            data = data+','+ 'xx.x'
        else:
            stt= sm_str2.split(':')
           
            data = data+','+ stt[1][0:len(stt[1])-1]
            
        if fault_SM3 :
            data = data+','+ 'xx.x'
        else:
            stt= sm_str3.split(':')
            data = data+','+ stt[1][0:len(stt[1])-1]
            
        if fault_SM4 :
            data = data+','+ 'xx.x'
        else:
            stt= sm_str4.split(':')
            data = data+','+ stt[1][0:len(stt[1])-1] 
        
        if fault_ST1 :
            data = data+','+ 'xx.x'
        else:
            stt= st_str1.split(':')
            data = data+','+ stt[1][0:len(stt[1])-1]
        if fault_ST2 :
            data = data+','+ 'xx.x'
        else:
            stt= st_str2.split(':')
            data = data+','+ stt[1][0:len(stt[1])-1]
        if fault_ST3 :
            data = data+','+ 'xx.x'
        else:
            stt= st_str3.split(':')
            data = data+','+ stt[1][0:len(stt[1])-1]
        if fault_ST4 :
            data = data+','+ 'xx.x'
        else:
            stt= st_str4.split(':')
            data = data+','+ stt[1][0:len(stt[1])-1]              
            
        if fault_HT :
            data = data+','+ 'xxx.xx'
        else:
            stt= ah_str.split(':')
            data = data+','+ stt[1][0:len(stt[1])-1]   
        if fault_HT :
            data = data+','+ 'xxx.xx'
        else:
            stt= at_str.split(':')
            data = data+','+ stt[1][0:len(stt[1])-1]
        if fault_AP :
            data = data+','+ 'xxx.xx'
        else:
            stt= ap_str.split(':')

            data = data+','+ stt[1][0:len(stt[1])-3]
            
        if fault_bat:
            data = data+','+ 'xxx.xx'
        else:
            data = data+','+ bat_v     
    return bat_v,sm_str1,sm_str2,sm_str3,sm_str4,st_str1,st_str2,st_str3,st_str4,ah_str,at_str,ap_str,data

def rd_faults(bat_v):
    global fault_bat,fault_SM1,fault_SM2,fault_SM3,fault_SM4,fault_ST1,fault_ST2,fault_ST3,fault_ST4
    global fault_HT,fault_AP
    sfmsg_sms= ''
    if fault_bat: sfmsg_sms=sfmsg_sms+'Low Battery:'+bat_v+'v!\r\n'
    if fault_SM1 : sfmsg_sms=sfmsg_sms+'Soil moisture Sensor1 FAULT!\r\n'
    if fault_SM2 : sfmsg_sms=sfmsg_sms+'Soil moisture Sensor2 FAULT!\r\n'
    if fault_SM3 : sfmsg_sms=sfmsg_sms+'Soil moisture Sensor3 FAULT!\r\n'
    if fault_SM4 : sfmsg_sms=sfmsg_sms+'Soil moisture Sensor4 FAULT!\r\n'
    
    if fault_ST1 : sfmsg_sms=sfmsg_sms+'Soil Temparature Sensor1 FAULT!\r\n'
    if fault_ST2 : sfmsg_sms=sfmsg_sms+'Soil Temparature Sensor2 FAULT!\r\n'
    if fault_ST3 : sfmsg_sms=sfmsg_sms+'Soil Temparature Sensor3 FAULT!\r\n'
    if fault_ST4 : sfmsg_sms=sfmsg_sms+'Soil Temparature Sensor4 FAULT!\r\n'  
    
    if fault_HT : sfmsg_sms=sfmsg_sms+'Air Humidity/Temp. Sensor FAULT!\r\n'
    if fault_AP : sfmsg_sms=sfmsg_sms+'Air Pressure Sensor FAULT!\r\n'
    return sfmsg_sms
            
    ###
##>>> test
'''
while True:
    pot1_value = pot1.read()
    print("pot1_value:",pot1_value)
    pot2_value = pot2.read()
    print("pot2_value:",pot2_value)
    pot3_value = pot3.read()
    print("pot3_value:",pot3_value)
    pot4_value = pot4.read()
    print("pot4_value:",pot4_value)
    utime.sleep(2)
'''
##<<