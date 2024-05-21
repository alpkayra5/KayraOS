import colorama
from colorama import Fore, Back, Style
import time
from time import sleep
import os
import datetime
from datetime import date
os.system('cls')
print ("Dikkat: Bu sistem şuanlık sadece Windows işletim sistemleri üzerinde çalışıyor. İlerde Linux içinde geliştireceğim !")
print ("Devam etmek için ENTER")
input()
os.system('cls')
print (Fore.LIGHTBLUE_EX)
print ("""




'##:::'##::::'###::::'##:::'##:'########:::::'###::::::::'#######:::'######::
 ##::'##::::'## ##:::. ##:'##:: ##.... ##:::'## ##::::::'##.... ##:'##... ##:
 ##:'##::::'##:. ##:::. ####::: ##:::: ##::'##:. ##::::: ##:::: ##: ##:::..::
 #####::::'##:::. ##:::. ##:::: ########::'##:::. ##:::: ##:::: ##:. ######::
 ##. ##::: #########:::: ##:::: ##.. ##::: #########:::: ##:::: ##::..... ##:
 ##:. ##:: ##.... ##:::: ##:::: ##::. ##:: ##.... ##:::: ##:::: ##:'##::: ##:
 ##::. ##: ##:::: ##:::: ##:::: ##:::. ##: ##:::: ##::::. #######::. ######::
..::::..::..:::::..:::::..:::::..:::::..::..:::::..::::::.......::::......:::

                                             

                                             _               
                         __   _____ __ _ ___(_) ___   __ _  
                         \ \ / / _ |__` |__ | |/ _ \ / _` | 
                          \ V /\__  | | / __| | (_) | | | |    1.2.6
                           \_/ |___/  |_\___|_|\___/|_| |_| 
                                                     



      
""")
time.sleep(2.5)
os.system('cls')
print (Fore.LIGHTRED_EX)
print ("Lütfen bir sistem seçiniz:")

system = """1. KayraOS Starter
        2. Boot System"""
print (system)
secenek = input()
if secenek == "2" :
    os.system('cls')
    os.system('color B6')
    print (Back.RED)
    print ("Welcome to Kyr Boot Manager and Utility")
    print (Fore.LIGHTYELLOW_EX)
    ozellikler = open("ozellik.txt")
    
    print (ozellikler.read())
    input ()
if secenek == "1" :
    os.system('cls')
    print ("Stater module has been loading  [%25]")
    time.sleep(0.1)
    print ("Starter module has been loaded  [OK]")
    time.sleep(0.1)
    print ("Applications loading  [OK]")
    time.sleep(0.1)
    print ("Applications being designed  [OK]")
    time.sleep(0.1)
    print ("Internet starting [OK]")
    time.sleep(0.1)
    print ("CONFIGURING THE SYSTEM")
    time.sleep(0.1)
    print ("CONFIGURING THE SYSTEM")
    time.sleep(0.1)
    print ("CONFIGURING THE SYSTEM")
    time.sleep(0.1)
    print ("CONFIGURING THE SYSTEM")
    time.sleep(0.1)
    print ("CONFIGURING THE SYSTEM")
    time.sleep(0.1)
    print ("CONFIGURING THE SYSTEM")
    time.sleep(0.1)
    print ("CONFIGURING THE SYSTEM  [OK]")
    time.sleep(1)
    print ("Hello World !")
    os.system('cls')
    
tekrar = 1
while tekrar == 1:
    time.sleep(0.5)
    print (Fore.LIGHTBLUE_EX)
    print ("Hoş geldiniz !")
    tarih = date.today()
    print (tarih)
    print ("KayraOS v1.5.2")
    print ("""

| 1. Görev Yöneticisi |

| 2. İnternette arat |

| 3. Hesap makinesi |
           
| 4. Şifre yöneticisi |

| 5. Sistem işlemleri |

| 6. Web Uygulamaları |
           
| 7. Oyunlar |
              """)
    secenek2 = input("Baslatici===")
    if secenek2 == "1" :
        os.system('taskmgr.exe')
    if secenek2 == "2" :
        os.system('cls')
       
        seceneknet = input("Google'da mı aratacaksınız yoksa bir siteye giriş mi yapacaksınız ? (G/S)")
        if seceneknet == "G" :
            print ("Lütfen boşluk yerine + koyunuz.")
            arat = input("Ara===")
            os.system('start https://google.com/search?q='+arat)
        if seceneknet == "S" :
            arat2 = input("Lütfen domain girin===")
            print ("NOT: Lütfen domaini yazmadan önce http/https yazmayı unutmayın.")
            os.system('start '+ arat2)
    if secenek2 == "3" :
        os.system('cls')
        print ("""
               Lütfen işlem seçin:
               1. Çarpma
               2. Toplama
               3. Çıkarma
               4. Bölme
               """)
        secenek3 = input("İslem===")
        if secenek3 == "1" :
            print ("Sayı bir:")
            x = int(input())
            print ("Sayi iki:")
            y = int(input())
            time.sleep(0.5)
            os.system('cls')
            sonuc1=x * y
            print (sonuc1)
        if secenek3 == "2" :
             print ("Sayı bir:")
             x1 = int(input())
             print ("Sayi iki:")
             y1 = int(input())
             time.sleep(0.5)
             os.system('cls')
             sonuc2=x1 + y1
             print (sonuc2)

        if secenek3 == "3" :
            print ("Sayı bir:")
            x2 = int(input())
            print ("Sayı iki:")
            y2 = int(input())
            time.sleep(0.5)
            os.system('cls')
            sonuc3=x2-y2
            print (sonuc3)
        if secenek3 == "4" :
            print ("Sayı bir:")
            x3 = int(input())
            print ("Sayı 2:")
            y3 = int(input())
            time.sleep(0.5)
            os.system('cls')
            sonuc4=x3/y3
            print (sonuc4)
    if secenek2 == "4" :
        os.system('cls')
        print (Fore.CYAN)
        print ("Şifre yöneticisine hoş geldiniz !!!")    
        print ()
        kullanici = input("Kullanıcı adınız===")
        sifre = input("Şifrenizi giriniz===")
        if kullanici == "admin" and sifre == "admin" :
            print ("Hoş geldiniz !!!")
            time.sleep(1)
            os.system('cls')
            print ("Kayıtlı şifreleriniz :::")
            sifreler = open("text.txt")
            print (sifreler.read())
        else :
            print ("Hatalı kullanıcı adı veya şifre !")
    if secenek2 == "5" :
        os.system('cls')
        print ("  'kapat' veya 'ybaslat'  ")
        sistemislemleri = input()
        if sistemislemleri == "kapat" :
            exit()
        if sistemislemleri == "ybaslat" :
            time.sleep(0)
    if secenek2 == "6" :
        os.system('cls')
        print ("""
1. LocalHost başlat




""")
        secenek4=input(">")
        if secenek4 == "1" :
            print ("Lütfen port no giriniz:")
            port=input(">")
            os.system('python -m http.server ' + port)
            
    if secenek2 == "7" :
        print ("DAHA GELİŞTİRİLMEDİ")
        
else :
    exit()
