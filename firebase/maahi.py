import socket
import sys
import time
import pygame as pg
import re
import sys
import os
import socket
import RPi.GPIO as gp
gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(12,gp.OUT)
gp.setup(10,gp.OUT)
gp.setup(3,gp.OUT)
gp.setup(18,gp.OUT)
gp.setup(29,gp.OUT)
gp.setup(40,gp.OUT)
gp.setup(16,gp.OUT)
gp.setup(38,gp.OUT)
gp.setup(40,gp.OUT)
gp.setup(32,gp.OUT)
gp.setup(36,gp.OUT)
gp.setup(16,gp.OUT)

gp.setup(33,gp.OUT)
gp.setup(35,gp.OUT)
gp.setup(37,gp.OUT)

gp.setup(29,gp.OUT)
gp.setup(31,gp.OUT)
gp.setup(32,gp.OUT)

gp.setup (21,gp.OUT)
gp.setup (23,gp.OUT)
buf=''

try :
    file = open("/home/pi/Desktop/dp.txt", 'r')
    data1=file.read(1)
    print(data1)
    data2=file.read(1)
    print (data2)
    data3=file.read(1)
    print (data3)
    data4=file.read(1)
    print(data4)
    data5=file.read(1)
    print (data5)
    data6=file.read(1)
    print (data6)
    data7=file.read(1)
    print (data7)
    data8=file.read(1)
    print (data8)
    file.close()
except :
    print ("error reading file")


rl1=data1;rl2=data2;rl3=data3;rf1=data4;rf2=data5;rf3=data6;led1=data7;led2=data8;

if(data1=="1"):
    gp.output(3,0)
    print ("room1 lights on")
else:
    gp.output(3,1)
    print ("room1 lights off")
if(data2=="1"):
    print ("room 2 lights on")
    gp.output(36,0)
else:
    print ("room2 lights off")
    gp.output(36,1)
    
if(data3=="1"):
    print ("room3 lights on")
    gp.output(38,0);gp.output(40,0); gp.output(18,0); gp.output(33,0); gp.output(35,0); gp.output(37,0)
else:
    print ("room3 lights off")
    gp.output(38,1); gp.output(18,1); gp.output(40,1); gp.output(33,1); gp.output(35,1); gp.output(37,1)
    
if(data4=="1"):
    gp.output(16,0)
    print ("room1 fans on")
else:
    gp.output(16,1)
    print ("room1 fans off")
if(data5=="1"):
    print ("room2 fans on")
else:
    print ("room2 fans off")

if(data6=="1"):
    print ("room3 fans on")
    gp.output(29,0);gp.output(31,0);gp.output(32,0)
else:
    print ("room3 fans off")
    gp.output(29,1);gp.output(31,1);gp.output(32,1)

if(data7=="1"):
    print ("blinking led")
    gp.output(23,0)
else :
    print("led's blinking stopped")
    gp.output(23,1)
if(data8=="0"):
    print ("outer led's stopped")
    gp.output(21,1)
else:
    gp.output(21,1)

search = "lights"
search1 = "on"
search2 = "off"
search3 = "fans"
search4 = "projector"
search5 = "room"
search6 = "1"
search7 = "2"
search8 = "open"
search9 = "unlock"
search10 = "door"
search11 = "mahi"
search12 = "501"
search13 = "doors"
search14 = "one"
search15 = "two"
search16 = "three"
search17 = "3"
str1="Mahi 501"
str2="mahi 501"
search18="open"
search19="curtains"
search20="close"
search21="curtain"
search22="blink"
search23="LED"
search24="stop"


li = ['lights']
on = ['on']
off = ['off']
fan = ['fans']
door = ['door']
doors = ['doors']
opn = ['open']
ul = ['unlock']
pro = ['projector']
mahi=['mahi']
numb=['501']
clo=['close']
ope=['open']
curtains=['curtains']
curtain=['curtain']
room = ['room']
roomno1 = ['1']
roomno2 = ['2']
one = ['one']
two = ['two']
three = ['three']
roomno3 = ['3']
blink = ['blink']
led = ['LED']
stop = ['stop']

while 1:
    if( os.stat("comd.txt").st_size != 0 ):
        f=open("comd.txt","r")
        buf=(str(f.read()))
        f.close()
        f=open("comd.txt","w")
        f.write("")
        f.close()    
        words = buf.split(" ")
        print (words)
        r1=re.findall(r"\b" + search + r"\b", buf)
        #print(r1)
        r2=re.findall(r"\b" + search1 + r"\b", buf)
        r3 = re.findall(r"\b" + search2 + r"\b", buf)
        r4 = re.findall(r"\b" + search3 + r"\b", buf)
        r5 = re.findall(r"\b" + search4 + r"\b", buf)
        r6 = re.findall(r"\b" + search5 + r"\b", buf)
        r7 = re.findall(r"\b" + search6 + r"\b", buf)
        r8 = re.findall(r"\b" +search7 + r"\b", buf)
        r9 = re.findall(r"\b" +search8 + r"\b", buf)
        r10 = re.findall(r"\b" +search9 + r"\b", buf)
        r11 = re.findall(r"\b" +search10 + r"\b", buf)
        r12 = re.findall(r"\b" +search11 + r"\b", buf)
        r13 = re.findall(r"\b" +search12 + r"\b", buf)
        r14 = re.findall(r"\b" +search13 + r"\b", buf)
        r15 = re.findall(r"\b" +search14 + r"\b", buf)
        r16 = re.findall(r"\b" +search15 + r"\b", buf)
        r17 = re.findall(r"\b" +search16 + r"\b", buf)
        r18 = re.findall(r"\b" +search17 + r"\b", buf)
        r19 = re.findall(r"\b" +search18 + r"\b", buf)
        r20 = re.findall(r"\b" +search19 + r"\b", buf)
        r21 = re.findall(r"\b" +search20 + r"\b", buf)
        r22 = re.findall(r"\b" +search21 + r"\b", buf)
        r23 = re.findall(r"\b" +search22 + r"\b", buf)
        r24 = re.findall(r"\b" +search23 + r"\b", buf)
        r25 = re.findall(r"\b" +search24 + r"\b", buf)
        print(r1)
        #commandRecieved = str(buf)
        #if li and on in commandRecieved:
        if (r1 == li and r2 == on and r6==room and ((r7==roomno1 or r14 == one) and (r8==roomno2 or r15 == two) and (r18==roomno3 or r17 == three))):
            print ("Turned on the lights in room1 and room2 and room3")
            gp.output(3,0)
            #gp.output(16,0)
            gp.output(36,0)
            time.sleep(0.5)
            gp.output(40,0)
            time.sleep(0.5)
            gp.output(18,0)
            time.sleep(0.5)
            gp.output(33,0)
            time.sleep(0.5)
            gp.output(35,0)
            time.sleep(0.5)
            gp.output(37,0)
            time.sleep(0.5)
            gp.output(38,0)
            rl2="1"
            rl1="1"
            rl3="1"
            try :
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error in lights on in r1 r2 r3")
            

        elif (r1 == li and r3 == off and r6==room and ((r7==roomno1 or r14 == one) and (r8==roomno2 or r15 == two) and (r18==roomno3 or r17 == three))):
            print ("Turned off the lights in room1 and room2 and room3")
            gp.output(3,1)
            #gp.output(16,1)
            gp.output(36,1)
            gp.output(38,1)
            time.sleep(0.5)
            gp.output(18,1)
            time.sleep(0.5)
            gp.output(33,1)
            time.sleep(0.5)
            gp.output(35,1)
            time.sleep(0.5)
            gp.output(37,1)
            time.sleep(0.5)
            gp.output(40,1)
            rl2="0"
            rl1="0"
            rl3="0"
            try :
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to on lights in r1 r2 r3")

            
        elif (r1 == li and r2 == on and r6==room and ((r7==roomno1 or r14 == one) and (r8==roomno2 or r15 == two))):
            print ("Turned on the lights in room1 and room2")
            gp.output(3,0)
            #gp.output(1,0)
            gp.output(36,0)
            rl1="1"
            rl2="1"
            try :
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print("error to on lights in r1 and r2")

        elif (r1 == li and r3 == off and r6==room and ((r7==roomno1 or r14 == one) and (r8==roomno2 or r15 == two))):
            print ("Turned off the lights in room1 and room2")
            gp.output(3,1)
            #gp.output(1,0)
            gp.output(36,1)
            rl1="0"
            rl2="0"
            try :
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print("error to off lights in r1 and r2")
            

        elif (r1 == li and r2 == on and r6==room and (r8==roomno2 or r16 == two)):
            print ("Turned on the lights in room2")
            gp.output(36,0)
            rl2="1"
            try :
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print("error to on lights in r2")

        elif (r1==li and r3==off and r6==room and (r7==roomno1 or r15 == one)):
            print ("Turned off the lights in room1")
            gp.output(3,1)
            rl1="0"
            try :
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to off lights in r1")
            
        elif (r1 == li and r3 == off and r6==room and (r8==roomno2 or r16 == two)):
            print ("Turned off the lights in room2")
            gp.output(36,1)
            rl2="0"
            try :
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to off lights in r2")
                
        elif (r4 == fan and r2 == on and r6==room and (r7==roomno1 or r15 == one)):
            print ("Turned on the fans in room1")
            gp.output(16,1)
            rf1="1"
            try:
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to on fans in r1")

        elif (r4 == fan and r2 == on and r6==room and (r8==roomno2 or r16 == two)):
            print ("Turned on the fans in room2")
            file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
            file.close()
            #gp.output(18,1)
            #rf1="1"
            #file=open("/home/pi/Desktop/dp.txt","w")
            #file.write(rl1+rl2+rl3+rf1+rf2+rf3)

        elif (r4 == fan and r2 == on and r6==room and (r18==roomno3 or r17 == three)):
            print ("Turned on the fans in room3")
            gp.output(29,0)
            time.sleep(0.5)
            gp.output(31,0)
            time.sleep(0.5)
            gp.output(32,0)
            time.sleep(0.5)
            rf3="1"
            try:
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to on fans in r3")
        

        elif (r4 == fan and r3 == off and r6==room and (r7==roomno1 or r15 == one)):
            print ("Turned off the fans in room1")
            gp.output(16,1)
            rf1="0"
            try:
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to off fans in r1")

        elif (r4 == fan and r3 == off and r6==room and (r8==roomno2 or r16 == two)):
            print ("Turned off the fans in room2")
            #gp.output(18,0)
            


        elif (r4 == fan and r3 == off and r6==room and (r18==roomno1 or r17 == three)):
            print ("Turned off the fans in room3")
            gp.output(29,1)
            time.sleep(0.5)
            gp.output(31,1)
            time.sleep(0.5)
            gp.output(32,1)
            time.sleep(0.5)
            rf3="0"
            try:
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to off fans in r3")
            
        elif (r1 == li and r2 == on and r6==room and (r18==roomno3 or r17 == three)):
            print ("Turned on the lights in room3")
            gp.output(18,0)
            time.sleep(0.5)
            gp.output(38,0)
            time.sleep(0.5)
            gp.output(33,0)
            time.sleep(0.5)
            gp.output(35,0)
            time.sleep(0.5)
            gp.output(37,0)
            time.sleep(0.5)
            gp.output(40,0)
            rl3="1"
            try:
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to on lights in r3")

        elif (r1 == li and r3 == off and r6==room and (r18==roomno3 or r17 == three)):
            print ("Turned off the lights in room3")
            gp.output(18,1)
            time.sleep(0.5)
            gp.output(38,1)
            time.sleep(0.5)
            gp.output(33,1)
            time.sleep(0.5)
            gp.output(35,1)
            time.sleep(0.5)
            gp.output(37,1)
            time.sleep(0.5)
            gp.output(40,1)
            rl3="0"
            try:
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to off lights in r3")
        
        elif (r1==li and r2==on and r6==room and (r7==roomno1 or r15 == one)):
            print ("Turned on the lights in room1")
            gp.output(3,0)
            rl1="1"
            try:
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to on lights in r1")

        elif (r1 == li and r2 == on):
            print ("Turned on the lights in all the rooms")
            gp.output(3,0)
            time.sleep(0.5)
            gp.output(36,0)
            time.sleep(0.5)
            gp.output(38,0)
            time.sleep(0.5)
            gp.output(18,0)
            time.sleep(0.5)
            gp.output(33,0)
            time.sleep(0.5)
            gp.output(35,0)
            time.sleep(0.5)
            gp.output(37,0)
            time.sleep(0.5)
            gp.output(40,0)
            rl1="1"
            rl2="1"
            rl3="1"
            try:
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to on lights in r1 r2 and r3")

            #gp.output(10,1)
            #gp.output(13,0)
            #gp.output(11,0)
            #gp.output(15,0)

        elif (r4 == fan and r2 == on):
            print ("Turned on the fans in all the rooms")
            gp.output(29,0)
            time.sleep(0.5)
            gp.output(31,0)
            time.sleep(0.5)
            gp.output(32,0)
            time.sleep(0.5)
            gp.output(16,0)
            rf1="1"
            try:
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to on fans in r1 r2 and r3")
            #gp.output(18,1)
            
        
        elif (r1 == li and r3 == off):
            print ("Turned off the lights in all the rooms")
            gp.output(3,1)
            time.sleep(0.5)
            gp.output(36,1)
            time.sleep(0.5)
            gp.output(38,1)
            time.sleep(0.5)
            gp.output(18,1)
            time.sleep(0.5)
            gp.output(33,1)
            time.sleep(0.5)
            gp.output(35,1)
            time.sleep(0.5)
            gp.output(37,1)
            time.sleep(0.5)
            gp.output(40,1)
            rl1="0"
            rl2="0"
            rl3="0"
            try:
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to off lights in r1 r2 and r3")
            #gp.output(10,0)

        elif (r4 == fan and r3 == off):
            print ("Turned off the fans in all the rooms")
            gp.output(29,1)
            time.sleep(0.5)
            gp.output(31,1)
            time.sleep(0.5)
            gp.output(32,1)
            time.sleep(0.5)
            gp.output(16,1)
            rf1="0"
            try:
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to off fans in r1 r2 and r3")
            #gp.output(18,0)

        elif (r23 == blink and r24 == led):
            print ("Blinking led's")
            gp.output(21,0)
            i=1
            while(i<=20):
                gp.output(23,0)
                time.sleep(0.3)
                gp.output(23,1)
                time.sleep(0.3)
                i=i+1
            gp.output(21,0)
            time.sleep(0.1)
            gp.output(23,0)
            try:
                led1="1"
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to blink led's")
            

        elif ((r24 == led and r3 == off) or (r25 == stop and r24 == led)):
            print ("led's blinking stopped")
            gp.output(23,1)
            gp.output(21,1)
            try:
                led1="0"
                file=open("/home/pi/Desktop/dp.txt","w")
                file.write(rl1+rl2+rl3+rf1+rf2+rf3+led1+led2)
                file.close()
            except :
                print ("error to off blinking led's")
            
        elif (r5 == pro and r2 == on):
            print ("Projector powered on")
            gp.output(29,1)
        
        elif (r5 == pro and r3 == off):
            print ("Projector powered off")
            gp.output(29,0)

        elif ((r11 == door or r13 == doors) and (r9 == opn or r10 == ul)):
            print ("door opened")
           
            try:
                sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sd.connect(('192.168.0.8', 8888))
            except socket.error as err:
                print ('Bind Failed, Error Code:  error in connection:')
            try:
                for args in sys.argv:
                    if (args == "") :
                        args = 'no args'
                    else:
                        output = 'Mahi 501'
                        sd.sendall(output.encode('utf-8'))
            except socket.error as err:
                print ("Bind Failed, Error Code: error in sending data")
            sd.close()
            #while 1:
             #   data = s.recv(64)
              #  print ("Received response:" + str(data))

        elif (r19 == ope and (r20 == curtains or r22 == curtain)):
            print ("Curtains OPened")
           

            sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                sd.connect(('192.168.0.8', 8888))
            except:
                print("error in connection:")
            try:
                output = 'openc'
                sd.sendall(output.encode('utf-8'))
            except socket.error as err:
                print ('Bind Failed, Error Code: error in sending')
            sd.close()
            #while 1:
             #   data = s.recv(64)
              #  print ("Received response:" + str(data))

        elif (r21 == clo and (r20 == curtains or r22 == curtain)):
            print ("Curtains Opened")
           

            sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                sd.connect(('192.168.0.8', 8888))
            except:
                print("error in connection:")
            try:
                for args in sys.argv:
                    if (args == "") :
                        args = 'no args'
                    else:
                        output = 'closec'
                        sd.sendall(output.encode('utf-8'))
            except socket.error as err:
                print ('Bind Failed, Error Code: error in sending data:')
            sd.close()
            #while 1:
             #   data = s.recv(64)
              #  print ("Received response:" + str(data))
            
               
        elif (("Mahi" in buf or "mahi" in buf) and "501" in buf):
            i=0
            while(i<=4):
                gp.output(12,0)
                time.sleep(1)
                gp.output(12,1)
                time.sleep(1)
                i+=1
            gp.output(12,0)
            time.sleep(2)
            pg.mixer.init()
            pg.mixer.music.load("/home/pi/Desktop/sound1.mp3")
            pg.mixer.music.play()
            while True:
                time.sleep(16.5)
                pg.quit()
                break;
            time.sleep(2.5)
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('192.168.0.8', 8888))
            for args in sys.argv:
                if (args == "") :
                    args = 'no args'
                else:
                    output = 'Mahi 501'
                    sd1.sendall(output.encode('utf-8'))
            sd1.close()
            time.sleep(2)

         

                
        else:
            print ("could not process the statement")
            


