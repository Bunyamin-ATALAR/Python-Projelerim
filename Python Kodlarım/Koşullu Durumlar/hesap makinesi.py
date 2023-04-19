print("""**********************************************
Hesap Makinesi İşlemi
1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
**********************************************""")

a=int(input("Birinci Sayiyi Giriniz:"))
b=int(input("İkinci Sayiyi Giriniz:"))

islem=int(input("Hangi İşlemi Yapmak İstiyorsunuz?:"))

if (islem==1):
    print("{} ile {} toplamı {}".format(a,b,a+b))

elif (islem==2):
    print("{} ile {} Çıkarması {}".format(a,b,a-b))

elif (islem==3):
    print("{} ile {} Çarpması {}".format(a,b,a*b))

elif (islem==4):
    print("{} ile {} Bölmesi {}".format(a,b,a/b))

else:
    print("Yanlış İşlem Yaptınız!..")