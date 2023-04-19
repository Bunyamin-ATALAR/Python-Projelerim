"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu
kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""

print("""***********************************
Beden Kitle İndeksi Hesaplama
***********************************""")

boy=float(input("Boyunuzu Giriniz:"))
kilo=float(input("Kilonuzu Giriniz:"))

formul= kilo/(boy*boy)

if (formul < 18.5):
    print("Beden Kitle İndeksiniz {} Zayıfsınız!..".format(formul))

elif (18.5<= formul <25):
    print("Beden Kitle İndeksiniz {} Normal Değerdesiniz!..".format(formul))

elif (25<= formul <30):
    print("Beden Kitle İndeksiniz {} Fazla Kilolusunuz!..".format(formul))

elif (formul>=30):
    print("Beden Kitle İndeksiniz {} Obezsiniz!..".format(formul))

else:
    print("İşlem Hatası!..")
