import os
while(1):
    if( os.stat("comd.txt").st_size != 0 ):
        f=open("comd.txt","r")
        print(str(f.read()))
        f.close()
        f=open("comd.txt","w")
        f.write("")
        f.close()
    
