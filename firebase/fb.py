from firebase import firebase
firebase = firebase.FirebaseApplication('https://maahi-6619e.firebaseio.com/', None)
while(1):
    try:
        result = firebase.get('/command', None)
        if("None" not in result):
            f=open("comd.txt",'w')
            f.write(str(result))
            f.close()
            firebase.delete('/command', None)
    except:
        print("")
        


