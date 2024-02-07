import machine,os
from machine import SoftSPI, Pin, ADC, UART, SoftI2C,RTC 
import aqu_sens
import gs6d02a2
import sim800 
import test_dt
import utime 
#
from sysfont import sysfont
sfont = sysfont
import sdcard  
import os
spi=SoftSPI(baudrate=1000,polarity=1,
    phase=0,sck=Pin(25),
    mosi=Pin(13),miso=Pin(12))
spi.init(baudrate=1000)
spi.read(2) 
sd=sdcard.SDCard(spi,Pin(19))
utime.sleep(0.2)
os.mount(sd,'/sd')
print(os.listdir())
spi=SoftSPI(baudrate=40000000,polarity=1,phase=0,sck=Pin(18,Pin.OUT),
            mosi=Pin(23,Pin.OUT),miso=Pin(27))
dsp=gs6d02a2.S6D02A1_SPI(spi,dc=Pin(2),cs=Pin(15),rst=Pin(5))
utime.sleep(0.5)

###
int_dttm = '18,11,2022,17,42,0'
nst_dttm = '18,11,2022,17,52,0'
nem_dttm = '19,11,2022,17,42,0'
mbno1='"8208835619"'
df_email = 'nandithanaik8@gmail.com'
df_user_nm= 'Nanditha'
smtp_srv = '"mail.smtp2go.com"'
smtp_srv_port = '2525'
smtp_srv_user='"ganeshanaik99@gmail.com"'
smtp_srv_pw='"HR7bATg94nXQKnrA"'

def upDate_ZC(): 
    #global calib_z,calib_aclV,calib_calV,set_wl,AST_ON, GRD_ON, EDT_wl #BT_ON
    global int_dttm,nst_dttm,nem_dttm
    global store_T,mbno1
    global df_email, df_user_nm,smtp_srv,smtp_srv_port
    global smtp_srv_user, smtp_srv_pw
    f= open('file_zc.txt', 'r')
    rdLn = f.readline()
    rdLn = str(rdLn[0:len(rdLn)-1])
    int_dttm=rdLn
    #print('int_dttm:', int_dttm)
    rdLn = f.readline()
    rdLn = str(rdLn[0:len(rdLn)-1])
    nst_dttm=rdLn
    rdLn = f.readline()
    rdLn = str(rdLn[0:len(rdLn)-1])
    store_T = float(rdLn)
    
    rdLn = f.readline()
    rdLn = str(rdLn[0:len(rdLn)-1])
    mbno1 = str(rdLn)
    
    rdLn = f.readline()
    rdLn = str(rdLn[0:len(rdLn)-1])
    stt = rdLn.split(',')
    df_email = str(stt[0])
    df_user_nm= str(stt[1])
    
    rdLn = f.readline()
    rdLn = str(rdLn[0:len(rdLn)-1])
    stt = rdLn.split(',')
    smtp_srv = str(stt[0])
    smtp_srv_port = str(stt[1])
    
    rdLn = f.readline()
    rdLn = str(rdLn[0:len(rdLn)-1])
    stt = rdLn.split(',')
    smtp_srv_user=str(stt[0])
    smtp_srv_pw=str(stt[1])
    
    rdLn = f.readline()
    rdLn = str(rdLn[0:len(rdLn)-1])
    nem_dttm=rdLn
    #
    f.close()
upDate_ZC()
#
dsp.fill_rectangle(0,0,160,128, 0x7521)
utime.sleep(0.1)
clr_org = dsp.color565(250,20,30)
clr_blk = dsp.color565(10,10,10)
pos=(15,35) 
dsp.text(aPos=pos, aString=' IITM ', aColor=clr_org, aFont=sfont, aSize = 4, nowrap = False )
pos=(20,80) 
dsp.text(aPos=pos, aString='SOIL LOGGER', aColor=clr_blk, aFont=sfont, aSize = 2, nowrap = False )
#utime.sleep(0.1)
#
utime.sleep(0.5)
import wifi_server
conn, addr=wifi_server.run_wifi_server()
utime.sleep(1)

def store_file_zc(): 
    global int_dttm,nst_dttm,nem_dttm
    global store_T, mbno1
    global df_email, df_user_nm,smtp_srv,smtp_srv_port
    global smtp_srv_user, smtp_srv_pw
    f=open('file_zc.txt','w')
    f.write(int_dttm+'\n')
    f.write(nst_dttm+'\n')
     
    f.write(str(store_T)+'\n')
    f.write(str(mbno1)+'\n')
    
    f.write(str(df_email)+','+str(df_user_nm)+'\n')
    f.write(str(smtp_srv)+','+str(smtp_srv_port)+'\n')
    f.write(str(smtp_srv_user)+','+str(smtp_srv_pw)+'\n')
    f.write(nem_dttm+'\n')
    utime.sleep(0.5)    
    f.close()
clrb = dsp.color565(150,150,150)
clr = dsp.color565(20,250,250)
dsp.fill_rectangle(0,0,160,128,clrb) #0x7521)
utime.sleep(1)

def txt_f(xf,yf,xf1,yf1,clrb,cllr):
    dsp.fill_rectangle(xf,yf,xf1,yf1,clrb)
#fill_rectangle(self, x, y, width, height, color)   
def txt2(xyP, str_t, clrt, fnt, fsiz):
    global clrb
    xf= xyP[0]
    yf= xyP[1]
    w= int(len(str_t)*(6*fsiz)) #11)
    h = int(7 * fsiz) #14
    #print(xf, yf, w, h)
    dsp.fill_rectangle(xf,yf,w,h,clrb) #0x7521) 
    
    utime.sleep_ms(5)
    dsp.text(aPos=xyP, aString=str_t, aColor=clrt, aFont=fnt, aSize = fsiz, nowrap = False)
    utime.sleep_ms(5)
    
pos=(10,50)
dsp.text(aPos=pos, aString='..WAIT..', aColor=clr, aFont=sfont, aSize = 3, nowrap = False )
utime.sleep(1) 
### start of bluetoothcodes  ###
import BT_server
ble= BT_server.run_bt()
print('ble at main:', ble)
utime.sleep(4)
message = '' #message.BT_server
### End  of bluetoothcodes  ###
rtc=RTC() 
sim800.inz_sim()
date =''
time = ''
#utime.sleep(2)
date, time=sim800.rd_sim_dttm() #rd_gprs_dat_time()
print('GPRS_date:', date)
print('GPRS_time:', time)
            
if len(date)>6 and len(time) > 4:
    std = date.split('/')
    stt = time.split(':')
    int_dttm = str(std[2])+','+str(std[1])+','+str(std[0])+','
    int_dttm = int_dttm + str(stt[0])+','+str(stt[1])+','+str(stt[2])
    print('int_dttm:', int_dttm)
    stt= int_dttm.split(',')
    stt[2]= str(int(stt[2])+2000)
    rtc.init((int(stt[2]),int(stt[1]) ,int(stt[0]), 4,int(stt[3]),int(stt[4]),int(stt[5]) , 0))
###
else:
#rtc=RTC() 
    stt= int_dttm.split(',')
    rtc.init((int(stt[2]),int(stt[1]) ,int(stt[0]), 4,int(stt[3]),int(stt[4]), 0 , 0))

def rd_dttm(): 
    DT = rtc.datetime()
    date = str(DT[2])+'/'+str(DT[1])+'/'+str(DT[0])
    time = str(DT[4])+':'+str(DT[5]) #+':'+str(DT[6])
    mnt= str(DT[5])
    return date,time,mnt
utime.sleep(0.2)
date,time,mnt = rd_dttm()
dsp.fill_rectangle(0,0,160,128,clrb) #0x7521)
utime.sleep(0.5)
scr_rg = 0
bat_dt_rg=0
sen_fault_rg=0
# for rain gauge count
button_pressed_count = 0 # global variable
pin_button = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)
#pin_button = Pin(34, mode=Pin.IN, pull=Pin.PULL_UP)
def button_isr(pin):
    global button_pressed_count
    button_pressed_count += 1
    #time.sleep(0.2)
    while True:
        if pin_button.value()==1:
            break
    print('button_pressed_count:',button_pressed_count)
        

#if __name__ == "__main__":
button_pressed_count_old = 0
pin_button.irq(trigger=Pin.IRQ_FALLING,handler=button_isr)
f_count=0

##
while True:
    bat_v,sm_str1,sm_str2,sm_str3,sm_str4,st_str1,st_str2,st_str3,st_str4,ah_str,at_str,ap_str,dataS=aqu_sens.rd_sens()
    sfmsg_sms=aqu_sens.rd_faults(bat_v)
    #For Display
    date,time,mnt = rd_dttm()
    #
    int_dttm=''
    #
    std= date.split('/')
    stt= time.split(':')
    str_dt = ('%4.2f'%(int(std[0])/100))[2:]
    int_dttm = int_dttm+str_dt
    str_mt = ('%4.2f'%(int(std[1])/100))[2:]
    int_dttm = int_dttm+','+str_mt+','+str(std[2])
    str_yr = str(int(std[2])-2000)
    str_hr = ('%4.2f'%(int(stt[0])/100))[2:]
    int_dttm = int_dttm+','+str_hr
    str_mnt = ('%4.2f'%(int(stt[1])/100))[2:]
    int_dttm = int_dttm+','+str_mnt+',0'
    
    date_str = str_dt+'/'+str_mt+'/'+ str_yr
    time_str = str_hr+':'+str_mnt
    dt_tm_str =  date_str+ ','+ time_str
    bat_f = float(bat_v)
    str_bat_vd = ('%4.2f'%(int(bat_f)/100))[2:]
    bat_vf = (bat_f-int(bat_f))*100
    str_bat_vf = ('%4.2f'%(bat_vf/100))[2:]
    batv_str= 'BATTERY:'+ str_bat_vd + '.'+ str_bat_vf +'v'
    rnf = button_pressed_count*0.14  #0.28 /2
    rnf_str= '%6.2f'%rnf 
    rn_str= 'RNF: '+ rnf_str +'mm'
    ######
    if scr_rg ==0 :
        pos=(2,2)
        txt2(xyP=pos, str_t= dt_tm_str, clrt=clr_blk, fnt=sfont, fsiz=2)
        pos=(10,20)
        txt2(xyP=pos, str_t= sm_str1, clrt=clr_org, fnt=sfont, fsiz=2)
        pos=(10,38)
        txt2(xyP=pos, str_t= sm_str2, clrt=clr_org, fnt=sfont, fsiz=2)
        pos=(10,56)
        txt2(xyP=pos, str_t= sm_str3, clrt=clr_org, fnt=sfont, fsiz=2)
        pos=(10,74)
        txt2(xyP=pos, str_t= sm_str4, clrt=clr_org, fnt=sfont, fsiz=2)
        pos=(10,92)
        txt2(xyP=pos, str_t= ah_str, clrt=clr_org, fnt=sfont, fsiz=2)
        pos=(5,110)
        txt2(xyP=pos, str_t= ap_str, clrt=clr_org, fnt=sfont, fsiz=2)
  
    if scr_rg == 1:
        pos=(2,2)
        txt2(xyP=pos, str_t= batv_str, clrt=clr_blk, fnt=sfont, fsiz=2)
        pos=(10,20)
        txt2(xyP=pos, str_t= st_str1, clrt=clr, fnt=sfont, fsiz=2)
        pos=(10,38)
        txt2(xyP=pos, str_t= st_str2, clrt=clr, fnt=sfont, fsiz=2)
        pos=(10,56)
        txt2(xyP=pos, str_t= st_str3, clrt=clr, fnt=sfont, fsiz=2)
        pos=(10,74)
        txt2(xyP=pos, str_t= st_str4, clrt=clr, fnt=sfont, fsiz=2)
        pos=(10,92)
        txt2(xyP=pos, str_t= at_str, clrt=clr, fnt=sfont, fsiz=2)  
        pos=(5,110)
        #txt2(xyP=pos, str_t= ap_str, clrt=clr, fnt=sfont, fsiz=2)
        txt2(xyP=pos, str_t= rn_str, clrt=clr, fnt=sfont, fsiz=2)
        utime.sleep(2)
    #print('scr_rg:',scr_rg)
    
    if scr_rg ==0: scr_rg=1
    else: scr_rg=0

    #for storing data
   
    store_rg = test_dt.store_time_check(int_dttm, nst_dttm)
            
    if store_rg == 1:
        #data = dt_tm_str+','+dataS+'\n'
        data = dt_tm_str+','+dataS+','+rnf_str+'\n'
        print('data to store:',data)
        '''
        f = open("DATA.txt", "a+")
        
        f.write(data)
        f.close()
        '''
        os.chdir('/sd')
        f = open("DATA.txt", "a+")
        utime.sleep(0.2)
        f.write(data)
        utime.sleep(0.2)
        f.close()
        button_pressed_count=0  # make zero .
        os.chdir('/') 
        utime.sleep(0.2)
        #update_nxt_store()
        ad_hr = int(store_T) #int(stt[0]) #5
        ad_mnt= int((store_T-ad_hr)*100) #30
        nst_dttm = test_dt.add_hr_mnt(int_dttm,ad_hr,ad_mnt)
        store_file_zc()
        print('nst_dttm @ store..:',nst_dttm)
        utime.sleep(1)
        #for storing the image in camara
        stt=int_dttm.split(',')
        dt_tm_tail = stt[0]+stt[1]+str(int(stt[2])-2000)+'-'+stt[3]+stt[4]
        print('in get_pic from camara through wifi')
     #>>>   
        conn.send('&click_store,'+dt_tm_tail+'\r\n')
     #<<<   
        utime.sleep(2)
        
    ### for Auto Email
        
    print('int_dttm:',int_dttm)
    print('nem_dttm:',nem_dttm)
    auto_email = test_dt.check_Auto_Email_time(int_dttm, nem_dttm)
    print('auto_email:', auto_email)
    if auto_email== 1:
        email_add = df_email #'nandithanaik8@gmail.com'
        user_name= df_user_nm #'Nanditha'
        print('email_add:', email_add)
        print('user_name:', user_name)
        #??utime.sleep(4) #??
        numb = 0
        mbno=mbno1
        sim800.send_email(email_add,user_name,numb,mbno)
        ad_24=24
        ad_00=00
        #
        stt= nem_dttm.split(',')
        std= int_dttm.split(',')
        nem_dttm=std[0]+','+std[1]+','+std[2]+','+stt[3]+','+stt[4]+',0'
        utime.sleep(0.1)
        nem_dttm= test_dt.add_hr_mnt(nem_dttm,ad_24,ad_00)
        print('nem_dttm:', nem_dttm)
        utime.sleep(0.2)
        store_file_zc()
        # to store next email
    if len(sfmsg_sms) > 5 and sen_fault_rg == 0:
        sim800.send_sms(mbno1,sfmsg_sms)
        sen_fault_rg=1
    if len(sfmsg_sms) < 5: sen_fault_rg=0
    
    ###  
    # to read SMS
    mbno, sms_msg= sim800.read_sms()
    print('mbno, sms_msg:',mbno,sms_msg)
    stt_sms_msg= sms_msg.split(':')
    print('stt_sms_msg:', stt_sms_msg)
    #if sms_msg=='READ':
    if stt_sms_msg[0]=='READ':
        print('in send sms mbno, sms_msg:',mbno,sms_msg)
        sms_msg_send = dt_tm_str+'\r\n'
        sms_msg_send = sms_msg_send+sm_str1+'\r\n'+sm_str2+'\r\n'+sm_str3+'\r\n'+sm_str4+'\r\n'
        sms_msg_send = sms_msg_send+st_str1+'\r\n'+st_str2+'\r\n'+st_str3+'\r\n'+st_str4+'\r\n'
        sms_msg_send = sms_msg_send+ah_str+'\r\n'
        sms_msg_send = sms_msg_send+at_str+'\r\n'+ap_str+'\r\n'+batv_str
        sim800.send_sms(mbno,sms_msg_send) 
    #if sms_msg=='STORE' query store_T
    if stt_sms_msg[0]=='STORE':
        print('in send sms mbno, sms_msg:',mbno,sms_msg)
        sms_msg_send = 'STORE:'+str(store_T)+'\r\n'
        sim800.send_sms(mbno,sms_msg_send)        
    #set store time
    if stt_sms_msg[0]=='SET_STORE':
        if len(stt_sms_msg) >1:
            store_T = float(stt_sms_msg[1])
            store_file_zc()
            
        print('store_T:', store_T)
        utime.sleep(1)

    if stt_sms_msg[0]=='SET_STORE_NEXT':
        if len(stt_sms_msg) >1:
            stt= stt_sms_msg[1].split(',')
            if len(stt)==5:
                nst_dt = int(stt[0])
                nst_mt = int(stt[1])
                nst_yr = int(stt[2])
                if nst_yr<99: nst_yr = nst_yr+2000
                if int(stt[3])<24 and int(stt[3])>0:
                    nst_hr = int(stt[3])
                if int(stt[4])<60:
                    nst_mnt = int(stt[4])
            store_file_zc()
            utime.sleep(1)
        
    if stt_sms_msg[0]=='MBNO1':
        print('in send sms mbno, sms_msg:',mbno,sms_msg)
        sms_msg_send = 'MBNO1:'+str(mbno1)+'\r\n'
        sim800.send_sms(mbno,sms_msg_send)
    #set mbno1
    if stt_sms_msg[0]=='SET_MBNO1':
        if len(stt_sms_msg) >1:
            mbno1 = '"'+str(stt_sms_msg[1])+'"'
            store_file_zc()
            
        print('MBNO1:', mbno1)
        utime.sleep(1)
    #for setting default email and username
    if stt_sms_msg[0]=='SET_EMAIL':
        if len(stt_sms_msg) >1:
            df_email = str(stt_sms_msg[1])
            stt_email_usr= df_email.split(',')
            if len(stt_email_usr) >1:
                df_email = str(stt_email_usr[0])
                df_user_nm= str(stt_email_usr[1])
        store_file_zc()
        utime.sleep(0.2)
    
    #if sms_msg=='EMAIL':
    if stt_sms_msg[0]=='EMAIL_DATA':
        email_add = df_email #'nandithanaik8@gmail.com'
        user_name= df_user_nm #'Nanditha'
        if len(stt_sms_msg) >1:
            email_add = str(stt_sms_msg[1])
            stt_email_add= email_add.split(',')
            if len(stt_email_add) >1:
                email_add = str(stt_email_add[0])
                user_name= str(stt_email_add[1])
        numb = 0
        sim800.send_email(email_add,user_name,numb,mbno)    
        
    #    
    if stt_sms_msg[0]=='EMAIL_PIC':    #'GET_PIC':
        print('in get_pic from camara through wifi')
        wifi_server.get_pic(conn)
        utime.sleep(0.5)
        email_add = df_email #'nandithanaik8@gmail.com'
        user_name= df_user_nm #'Nanditha'
        if len(stt_sms_msg) >1:
            email_add = str(stt_sms_msg[1])
            stt_email_add= email_add.split(',')
            if len(stt_email_add) >1:
                email_add = str(stt_email_add[0])
                user_name= str(stt_email_add[1])
        numb = 1
        sim800.send_email(email_add,user_name,numb,mbno)
    #for BT
    #print('BT_server.ble_connect=:',BT_server.ble_connect)
    def sendBT(bt_msg_snd):
        global ble
        ble.send(bt_msg_snd)
        utime.sleep_ms(200)
    if BT_server.ble_connect :
        ###
        sendBT(sm_str1)
        sendBT(sm_str2)
        sendBT(sm_str3)
        sendBT(sm_str4)
        sendBT(st_str1)
        sendBT(st_str2)
        sendBT(st_str3)
        sendBT(st_str4)
        sendBT(at_str)
        sendBT(ah_str)
        sendBT(ap_str)
        sendBT(batv_str)
        ###
        message = BT_server.read_message_bt()  
        stt_bt_msg= message.split(':')
        message= '' #????????
        #if sms_msg=='READ':
        #if stt_sms_msg[0]=='READ':
        ##
        if stt_bt_msg[0]=='MBNO1':
            bt_msg_send = 'MBNO1:'+str(mbno1) #+'\r\n'
            sendBT(bt_msg_send)
        if stt_bt_msg[0]=='SET_MBNO1':
            if len(stt_bt_msg) >1:
                mbno1 = '"'+str(stt_bt_msg[1])+'"'
                store_file_zc()
                utime.sleep(0.5)
            bt_msg_send = 'MBNO1:'+str(mbno1) #+'\r\n'
            sendBT(bt_msg_send)
        if stt_bt_msg[0] == "STORE":  
            bt_msg_send = 'STORE:'+str(store_T)
            sendBT(bt_msg_send)     
        #set store time
        if stt_bt_msg[0]=='SET_STORE':
            if len(stt_bt_msg) >1:
                store_T = float(stt_bt_msg[1])
                store_file_zc()
                utime.sleep(0.5)
            bt_msg_send = 'STORE:'+str(store_T)
            sendBT(bt_msg_send)
        #
    else:
        utime.sleep(2)
    