"""Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın."""

a=int(input("Birinci Sayıyı Giriniz:"))
b=int(input("İkinci Sayıyı Giriniz:"))
c=int(input("Üçüncü Sayıyı Giriniz:"))

if (a>b and a>c):
    print("{} En büyük Sayı A'dır!..".format(a))

elif (b>a and b>c):
    print("{} En büyük Sayı B'dir!..".format(b))

elif (c>a and c>b):
    print("{} En büyük Sayı C'dir!..".format(c))

else:
    print("İşlem Hatası")