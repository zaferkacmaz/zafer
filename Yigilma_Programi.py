from distutils.log import error
import math
from operator import truediv 
import os
import time

os.system("cls")
onyazi = "Bu program boru uretilirken olusabilecek et kalinligi yiginlasmasini tahmin etmeye yarayan bir programdir. \nHesaplama mekanizmasi borular icindir. \n\nBorunun çekildiği bandın et kalınlığının uniform ve her yerinde aynı olduğu varsayılmıştır.\n± %10 ~ %20 değişme olabilir bu hesap sadece size bir fikir sunabilir. Kesinlik arz etmemektedir. \nProfiller icinse profilin turk kafasina girmeden hemen onceki boru halinden yararlanir. \nDevam etmek icin tiklayin ..."

D_dis = 0
for i in onyazi:
    print(i,end="",flush=True)
    time.sleep(0.03)
input("")

def AnaFonksiyon(): ## İşlemi hesaplayan ana fonksiyon ##
    os.system("cls")
    Hata_yazisi = "\nHatali giris yaptiniz, tekrar denemek ister misiniz ...? " 
    Hata_yazisi_2 = "\nHatali giris yaptiniz, basa donuluyor ..."
    Cikis_Yazisi  = "\nCikis yapiliyor ..." ## Soru Cevap Kısmı için düzenleme ##
    Soru = "Tekrar denemek ister misiniz... ? "
    inp_1 = "\nLutfen bant genisligini girin ... " ## Hesaplama İçin Bant Genişliğini alan kısım ##
    for i in inp_1:
        print(i,end="",flush=True)
        time.sleep(0.03)
    BG = float(input("==> "))


    Yazi_1 = "\nBu banttan Boru mu Profil mi Uretilecek ? ... "
    for i in Yazi_1:
        print(i,end="",flush=True)
        time.sleep(0.03)
    Cevap = str(input("(B/P) ==> "))

    if Cevap == "B":
        inp_2 = "\nLutfen uretilecek borunun ojinal dis capini girin ...\n"
        for i in inp_2:
            print(i,end="",flush=True)
            time.sleep(0.03)
        D_dis_1 = float(input("==> "))
        D_dis = D_dis_1
        
    elif Cevap == "P":
        inp_p = "\nProfilin Turk Kafalarina girmeden oluşturdugu borunun dis capi " + str((BG/math.pi)) + " olarak tespit edildi "
        for i in inp_p:
            print(i,end="",flush=True)
            time.sleep(0.03)
        D_dis = float(BG/math.pi)

    else:
        for i in Hata_yazisi:
            print(i,end="",flush=True)
            time.sleep(0.03)
        Cvp = str(input("(E/H) ==> ")) 
        if Cvp == "E":
            AnaFonksiyon()
        elif Cvp == "H":
            for i in Cikis_Yazisi:
                print(i,end="",flush=True)
                time.sleep(0.03)
                exit()        
        else:
            for i in Hata_yazisi_2:
                print(i,end="",flush=True)
                time.sleep(0.03)    
                AnaFonksiyon()
            
    inp_3  = "\n\nLutfen borunun uretildigi bandın et kalinligini girin ...\n"  
    for i in inp_3:
        print(i,end="",flush=True)
        time.sleep(0.03)
    t_i = float(input("==> "))

    inc_mik = (math.pi*D_dis - BG) / (D_dis*math.pi)
    kal_mik = (BG - math.pi*D_dis + math.pi*2*t_i) / (math.pi*D_dis - 2*t_i*math.pi)
    t_s = t_i + kal_mik - inc_mik
    os.system("cls")
    print("\n")

    ayrac  = "-------------------------------------------------"
    for i in ayrac:
        print(i,end="",flush=True)
        time.sleep(0.02)
    print("\n\ndis captaki incelme miktari ",inc_mik," 'tir. ")
    print("\n\nic captaki kalinlasma miktari ",kal_mik," 'dir. ")
    print("\n\nGenel yiginti miktari ",t_s," 'dir. 

    for i in Soru:
        print(i,end="",flush=True)
        time.sleep(0.03)
    Cvp_1 = str(input("(E/H) ==> "))
    if Cvp_1 == "E":
        AnaFonksiyon()
    elif Cvp_1 == "H":
        for i in Cikis_Yazisi:
            print(i,end="",flush=True)
            time.sleep(0.03)
            exit()
    else:
        for i in Hata_yazisi_2:
            print(i,end="",flush=True)
            time.sleep(0.03)
            AnaFonksiyon()
AnaFonksiyon()
input("")
