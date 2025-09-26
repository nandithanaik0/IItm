import network
import socket
import utime
###
station = network.WLAN(network.STA_IF)
station.active(True)
###
utime.sleep(2)
def connect():
    global station
    server = ''
    print('in connect')
    ssid = 'SOIL_IITM_AP'   #'iBall-Baton' #"yourNetworkName"
    password = '123456789' #'nanditha90' #"yourNetworkPassword"
    '''
    station = network.WLAN(network.STA_IF)
    station.active(True)
    '''
    alrdy_conn=False
    utime.sleep(0.5)
    if station.isconnected() == True:
        print("Already connected")
        stt= station.ifconfig()
        #print('server:', stt[2])
        server = str(stt[2])
        alrdy_conn=True
        return server,alrdy_conn
 
    #station.active(True)
    utime.sleep(1)
    break_rg= True
    while break_rg:   
        stt = station.scan() #.decode("utf-8")
        #print('station.scan():', stt)
        print('len(stt):', len(stt))
        ck_ssid=''
        utime.sleep(2)
        for i in range (len(stt)):
            #print('stt[i]:',stt[i])
            st=str(stt[i]).split(',')
            #print('len(st), st:', len(st), st)
            ck_ssid= st[0][3:len(st[0])-1]
            print('ssid, st[0]:',ssid,',',ck_ssid) #.decode('utf-8'))
            #for j in range(len(st)):
                #print('st[',j,']:',st[j])
            #print('ck_ssid:',ssid)
            if ck_ssid==ssid:
                print('FOUND.. ssid:', ck_ssid)
                break_rg=False
                
            
    print('goes for station.connect(ssid, "")')
    station.connect(ssid, "") #password)
    print('while station.isconnected() == False:')
    while station.isconnected() == False:
        print('while station.isconnected() == False:')
        utime.sleep(1)
        pass
    
 
    stt = station.ifconfig()
    print("Connection successful:",stt) 
    alrdy_conn=False
    #print('Server:',stt[2])
    server = str(stt[2])
    return server,alrdy_conn
    '''
    utime.sleep(2)
    sock = socket.socket()
    sock.connect(('192.168.4.1', 80))
    sock.write('GET / HTTP/1.0\nHost: example.com\n\n')
    rd_ln = sock.readline()
    print('rd_ln:', rd_ln)
    sock.close()
    '''
def ck_station():
    global station
    status_station=False
    if station.isconnected() == True:
        status_station=True
    return status_station


#server,alrdy_conn= connect()
#print('server,alrdy_conn:', server,alrdy_conn)
