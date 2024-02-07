#AT commands for gsm/gprs sim 800l
from machine import UART 
import utime,os
urt = UART(2,9600)
urt.init(9600,bits=8,parity=None,stop=1)

cmd_at='AT\r\n'
cmd_at_cfun_1='AT+CFUN=1\r\n'
cmd_at_cops_1='AT+COPS=0\r\n'
cmd_at_clip_1='AT+CLIP=1\r\n'
cmd_at_cmgf_1='AT+CMGF=1\r\n'
cmd_ate0='ATE0\r\n' 
cmd_at_cmgl_unread='AT+CMGL='+'"REC UNREAD"'+'\r\n'
cmd_at_cmgs='AT+CMGS='
cmd_at_cmgd_1_3='AT+CMGD=1,3\r\n'
cmd_at_cmgd_1_4='AT+CMGD=1,4\r\n'
cmd_at_creg_1='AT+CREG=1\r\n' 
cmd_at_cclk='AT+CCLK?\r\n'
cmd_at_clts_1='AT+CLTS=1\r\n'

def clr_urt_ipB(): 
    while True:
        if urt.any():
           rdl_urt= urt.readline()
           #rdl_urt_str=str(rdl_urt.decode('utf-8'))
           #print('urt_rd:', rdl_urt_str)
        else: break
        
def rd_urt():
    tt=0
    while tt<10:
        if urt.any():
           rdl_urt= urt.readline()
           
           #rdl_urt_str=str(rdl_urt.decode('utf-8'))
           
           print('urt_rd:', rdl_urt) #_str)
           utime.sleep(0.1)
           
        else:
            tt = tt +1
            utime.sleep(0.3)
            #break
def rd_urt1():
    tt=0
    while tt<10:
        if urt.any():
           rdl_urt= urt.readline()
           
           #rdl_urt_str=str(rdl_urt.decode('utf-8'))
           
           print('urt_rd:', rdl_urt) #_str)
           utime.sleep(0.1)
        else:
            tt = tt +1
            utime.sleep(0.1)
            #break
def inz_sim():
    clr_urt_ipB()
    #at_cmd= str(dpl_set)+'\r\n'
    print('AT_CMD:',cmd_at)
    urt.write(cmd_at)
    #utime.sleep(1)
    rd_urt1()
    print('AT_CMD:',cmd_at)
    urt.write(cmd_at)
    #utime.sleep(1)
    rd_urt1()
   
    print('AT_CMD:',cmd_at_cops_1)
    urt.write(cmd_at_cops_1)
    #utime.sleep(1)
    rd_urt1()
    print('AT_CMD:',cmd_at_clip_1)
    urt.write(cmd_at_clip_1)
    #utime.sleep(1)
    rd_urt1()
   
    print('AT_CMD:',cmd_ate0)
    urt.write(cmd_ate0)
    #utime.sleep(1)
    rd_urt1()
    #
    print('AT_CMD:',cmd_at_creg_1)
    urt.write(cmd_at_creg_1)
    #utime.sleep(1)
    rd_urt1()
    #
    print('AT_CMD:',cmd_at_cfun_1)
    urt.write(cmd_at_cfun_1)
    #utime.sleep(1)
    rd_urt1()
    print('AT_CMD:',cmd_at_cmgf_1)
    urt.write(cmd_at_cmgf_1)
    #utime.sleep(1)
    rd_urt1()
    
    print('AT_CMD:','AT&W')
    urt.write('AT&W\r\n')
    #utime.sleep(1)
    rd_urt()
    
    print('AT_CMD:',cmd_at_cmgd_1_4)
    urt.write(cmd_at_cmgd_1_4)
    #utime.sleep(1)
    rd_urt()
    print('AT_CMD:',cmd_at_cmgd_1_3)
    urt.write(cmd_at_cmgd_1_3)
    #utime.sleep(1)
    rd_urt()
    
    #cmd_at_cclk='AT+CCLK?\r\n'
    #cmd_at_clts_1='AT+CLTS=1\r\n'
    print('AT_CMD:',cmd_at_clts_1)
    urt.write(cmd_at_clts_1)
    #utime.sleep(1)
    rd_urt()
    print('AT_CMD:',cmd_at_cclk)
    urt.write(cmd_at_cclk)
    #utime.sleep(1)
    rd_urt()
#def rd_gprs_dat_time():
   ##
def rd_sim_dttm():
    clr_urt_ipB()
    utime.sleep(0.1)
    print('AT_CMD:',cmd_at)
    urt.write(cmd_at)
    #utime.sleep(1)
    rd_urt1()
   
    print('AT_CMD: AT+CCLK?\r\n')
    urt.write('AT+CCLK?\r\n')
    utime.sleep(1)

    rd_ln = ''
    date = ''
    time = ''
    tt=0
    print('in while tt < 10:')
    while tt < 10:
        if urt.any():
            try:
                rd_ln = urt.readline()
                print('rd_ln:', rd_ln)
                rd_ln_str = str(rd_ln.decode('utf-8'))
                print('rd_ln_str:', rd_ln_str)
                rd_ln_str = str(rd_ln_str[0:len(rd_ln_str)-2])
                print('rd_ln_str1:',rd_ln_str)
                utime.sleep(0.3)
                rd_ln = urt.readline()
                print('rd_ln:', rd_ln)
                rd_ln_str = str(rd_ln.decode('utf-8'))
                print('rd_ln_str:', rd_ln_str)
                #rd_ln_str = str(rd_ln_str[0:len(rd_ln_str)-2])
                rd_ln_str = str(rd_ln_str[8:len(rd_ln_str)-6])
                print('rd_ln_str2:',rd_ln_str)
                stt=rd_ln_str.split(',')
                print('stt:', stt)
                date = str(stt[0])
                time = str(stt[1])
                print('date:', date)
                print('time:', time)
                utime.sleep(0.4)
                
            except:
                print('exception_RDDT')
            #ble.send(rd_ln_str)
            #stb.append(rd_ln_str)
                
            utime.sleep_ms(50)
            break
        else:
            utime.sleep_ms(500)
            tt= tt+1

    return str(date), str(time) 
       
def read_sms():
    global cmd_at_cmgl_unread
   
    clr_urt_ipB()
    utime.sleep(0.1)
    
    print('AT_CMD:',cmd_at)
    urt.write(cmd_at)
    #utime.sleep(1)
    rd_urt1()
    
    print(cmd_at_cmgl_unread)
    urt.write(cmd_at_cmgl_unread)
    #??utime.sleep(1) #(4)
    rd_ln = ''
    mbno = ''
    sms_msg= ''
    tt=0
    while tt < 10:
        if urt.any():
            try:
                rd_ln = urt.readline()
                #print('rd_ln:', rd_ln)
                rd_ln_str = str(rd_ln.decode('utf-8'))
                #print('rd_ln_str:', rd_ln_str)
                rd_ln_str = str(rd_ln_str[0:len(rd_ln_str)-2])
                print('rd_ln_str1:',rd_ln_str)
                utime.sleep(0.3)
                rd_ln = urt.readline()
                #print('rd_ln:', rd_ln)
                rd_ln_str = str(rd_ln.decode('utf-8'))
                #print('rd_ln_str:', rd_ln_str)
                rd_ln_str = str(rd_ln_str[0:len(rd_ln_str)-2])
                print('rd_ln_str2:',rd_ln_str)
                stt=rd_ln_str.split(',')
                mbno = str(stt[2])
                print('MBno2:', mbno)
                utime.sleep(0.4)
                rd_ln = urt.readline()
                print('rd_ln3:', rd_ln)
                rd_ln_str = str(rd_ln.decode('utf-8'))
                print('rd_ln_str3:', rd_ln_str)
                rd_ln_str = str(rd_ln_str[0:len(rd_ln_str)-2])
                print('rd_ln_str3:',rd_ln_str)
                sms_msg = rd_ln_str
                print('MBno3:', mbno)
                print('SMS:', sms_msg)
                utime.sleep(0.5)
                '''
                urt.write(cmd_at)
                utime.sleep(0.5)
                print('AT_cmd:', cmd_at_cmgd_1_4)
                urt.write(cmd_at_cmgd_1_4)
                utime.sleep(0.5)
                rd_urt()
                '''
                print('AT_cmd:', cmd_at_cmgd_1_3)
                urt.write(cmd_at_cmgd_1_3)
                utime.sleep(0.5)
                rd_urt()
                
            except:
                print('exception_RDSMS')
            #ble.send(rd_ln_str)
            #stb.append(rd_ln_str)
                
            utime.sleep_ms(50)
            break
        else:
            utime.sleep_ms(500)
            tt= tt+1
    return mbno, sms_msg

def send_sms(mbno,sms_msg_send): #wsms1,wsms2,wsms3,wsms4,wsms5):
    #send_sms(mbno,sm_str,st_str,ah_str,at_str,ap_str)
    global cmd_at_cmgs
    print('AT_CMD:', cmd_at)
    urt.write(cmd_at)
    #utime.sleep(0.1)
    rd_urt1()
    print('AT_CMD:', cmd_at)
    urt.write(cmd_at)
    #utime.sleep(2)
    rd_urt1()
    #??clr_urt_ipB()
    sms_comd= cmd_at_cmgs+mbno+'\r\n'
    print('in sms_comd:',sms_comd)
    urt.write(sms_comd)
    
    #utime.sleep(2)
    rd_urt()
    ###
  
    ###
    #wsms1= 'value of sensor1\r\n'
    #print('wsms1:', wsms1)
   
    urt.write(sms_msg_send+'\r\n')
    utime.sleep(0.1)
    urt.write(b'\x1a')   #ctrl z
    utime.sleep(0.5)
    rd_urt()
    utime.sleep(0.2) 
    
def wr_at(at_cmd):
    print('AT_CMD:', at_cmd)
    urt.write(at_cmd+'\r\n')
    utime.sleep(0.1)
    rd_urt()
#####
def at_resp():
    rd_ln = ''
    rd_ln_str=''
    tt=0
    while tt <120:
        if urt.any():
            print('in at_resp()...')
            try:
                rd_ln = urt.readline()
                rd_ln_str = str(rd_ln.decode('utf-8'))
                rd_ln_str = str(rd_ln_str[0:len(rd_ln_str)-2])
                print('at_resp()L1:', rd_ln)
                st=rd_ln_str.split(':')
                if st[0]=='+SMTPFT':
                    st=st[1].split(',')
                    if st[0]=='1': rd_ln_str=str(st[1])
                    print('st[1]:', rd_ln_str)
                    break
            except:
                print('exception_W_R_at')
                utime.sleep_ms(50)
                break
        else:
            utime.sleep_ms(200)
            tt= tt+1
    return rd_ln_str


##### 

#####
def send_email(email_add,user_name,numb,mbno):
    wr_at('AT')
    wr_at('AT+SAPBR=3,1,"Contype","GPRS"')
    #wr_at('AT+SAPBR=3,1,"APN","WWW"')  #for vadofone
    wr_at('AT+SAPBR=3,1,"APN",""')  #for AirTell
    #??wr_at('AT+SAPBR=1,1')
    utime.sleep(1)
    cmd_AT_SAPBR_1_1='AT+SAPBR=1,1'+'\r\n'
    print('AT_cmd:',cmd_AT_SAPBR_1_1)
    urt.write(cmd_AT_SAPBR_1_1) #('AT+SAPBR=1,1'+'\r\n')
    utime.sleep(3)
    rd_urt()
    
    wr_at('AT+SAPBR=2,1')
    wr_at('AT+EMAILCID=1')
    wr_at('AT+EMAILTO=180')
    
    wr_at('AT+SMTPSRV="mail.smtp2go.com",2525')
    wr_at('AT+SMTPAUTH=1,"ganeshanaik99@gmail.com","HR7bATg94nXQKnrA"')
    
    wr_at('AT+SMTPFROM="ganeshanaik99@gmail.com","ESP32"')
   # wr_at('AT+SMTPRCPT=0,0,"nandithanaik8@gmail.com","Nanditha"')
    wr_at('AT+SMTPRCPT=0,0,"'+email_add+'","'+user_name+'"')
    msg_body=''
    if numb==0:
        wr_at('AT+SMTPSUB="SOIL DATA"')
        msg_body= "Please see the Attached file DATA.txt."
    if numb==1:
        wr_at('AT+SMTPSUB="SOIL PICTURE"')
        msg_body= "Please see the Attached file pic_img1.jpg"

    #wr_at('AT+SMTPBODY=20')
    wr_at('AT+SMTPBODY='+str(len(msg_body)))
    utime.sleep(1)
    urt.write(msg_body)
    utime.sleep(0.1)
    rd_urt()
    wr_at('AT')
    if numb==0: wr_at('AT+SMTPFILE=1,"DATA.txt",0')
    if numb==1: wr_at('AT+SMTPFILE=2,"pic_img1.jpg",1')
    wr_at('AT')
    wr_at('AT+SMTPSEND')
    utime.sleep(2)
    rd_resp=at_resp()
    print('rd_resp:', rd_resp)
    max_bsnd =32
    ck_al=0
    try:
        sttm= rd_resp.split(',')
        max_bsnd=int(sttm[1])
        print('Maximum chr. allows to send:',max_bsnd)
        ck_al=1
    except:
        print('error in at_resp()')
    if ck_al==1:
        
        
        #utime.sleep(2)
        wr_at('AT')
        ###
        fn = ''
        if numb==0:
            os.chdir('/sd')
            utime.sleep(0.5)
            fn='DATA.txt' 
        if numb==1:fn='pic_img1.jpg'
        stt=os.stat(fn)
        fchrs= int(stt[6])
        print('size of file:', fchrs)
        utime.sleep(5)
        #
        fchrs_rm= fchrs
        if numb==0:f = open("DATA.txt","r")
        if numb==1:f = open("pic_img1.jpg","r")
        chrs_ln= 1024
        while fchrs_rm > chrs_ln: #1024:
            cmd_at_smtpft= 'AT+SMTPFT='+str(chrs_ln)+'\r\n'
            print('AT_cmd:', cmd_at_smtpft)
            #rd_urt()
            clr_urt_ipB()
            utime.sleep(0.1)
            urt.write(cmd_at_smtpft)
            utime.sleep(0.5)
            rd_urt()
            #rd_urt()
            for i in range (chrs_ln):
                chrs=f.read(1)
                urt.write(chrs)
            fchrs_rm = fchrs_rm-chrs_ln #1024
            utime.sleep(0.1)
            clr_urt_ipB()
        #
        
        #if fchrs > 10 and fchrs<1025:
        if fchrs_rm > 0 :  #  and fchrs<1025:
            cmd_at_smtpft= 'AT+SMTPFT='+str(fchrs_rm)+'\r\n'
            print('AT_cmd:', cmd_at_smtpft)
            urt.write(cmd_at_smtpft)
            utime.sleep(0.1)
            rd_urt() 
            #rd_resp=at_resp()
            for i in range (fchrs_rm):
                chrs=f.read(1)
                urt.write(chrs)
            
                #print(chrs)
            #?f.close()
            utime.sleep(3)
            
            #rd_resp=at_resp()
            #print('rd_resp:', rd_resp)
            rd_urt()
        print('AT_cmd:','AT+SMTPFT=0'+'\r\n')
        urt.write('AT+SMTPFT=0'+'\r\n')
        utime.sleep(1)
        rd_urt()
        #rd_resp=at_resp()
        #print('rd_resp:', rd_resp)
        f.close()
        if numb==0: os.chdir('/')
        utime.sleep(1)
        
    wr_at('AT')
    wr_at('AT+SAPBR=0,1')
    utime.sleep(0.3)
    sms_msg_send = 'Network error.. Try Again.!'
    if ck_al==1:
        sms_msg_send = 'Check the Email/spam..for DATA_FILE'
    send_sms(mbno,sms_msg_send)

####