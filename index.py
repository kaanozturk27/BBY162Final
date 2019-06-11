global ad
ad= "veriler.txt"

def listele() :
    with open(ad ,"r") as dosya:
        bilgiler = dosya.readlines()
        i =1
        for bilgi in bilgiler:
            print(i,".",bilgi)
            i+= 1
def ekle():

        with open (ad,"a") as dosya:
         dosya.write(input("_"+"Yazar ismini giriniz")+":")
         dosya.write(input("Eser ismini giriniz")+",")
         dosya.write(input("Tarihi giriniz"))
def arama():

    with open(ad,"r") as dosya:

        aranan = input("Belgede aramak istediğiniz kelimeyi giriniz: ")

        aranan_varmi =dosya.read().find(aranan)

    if aranan_varmi != -1:
        print(aranan)

    else:

        print("Aradığınız Kelime veritabanında bulunmamaktadır.")

while 1:
    print(" Katalogdaki eserleri listelemek için: 1")
    print("----------------------------------------")
    print("Yeni eser girişi için: 2")
    print("----------------------------------------")
    print("Eser adına, yazar adına ya da tarihe göre arama yapmak için: 3")
    print("----------------------------------------")

    secenek = int(input("İşlem yapmak için bir seçenek seçiniz:"))

    if secenek ==1 :
        listele()
    if secenek ==2:
        ekle()
    if secenek ==3 :
       arama()
