"""Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)"""

boy=float(input("boyunuzu giriniz:"))
kilo=int(input("kilonuzu giriniz:"))

print("degerler kaydediliyor...")

BDI=kilo/(boy*boy)
print(BDI)