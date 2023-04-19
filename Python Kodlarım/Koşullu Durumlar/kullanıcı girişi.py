print("""***********************
Kullanıcı Girişi İşlemi
***********************""")

xkullanıcıadı = "Bunyamin"
xparola = 616161

kullanıcıadı = input("Kullanıcı Adı Giriniz:")
parola = int(input("Parolanızı Giriniz:"))

if (kullanıcıadı == xkullanıcıadı and parola != xparola):
    print("Parolanız Yanlış!..")

elif (kullanıcıadı != xkullanıcıadı and parola == xparola):
    print("Kullanıcı Adı Hatalı!..")

elif (kullanıcıadı != xkullanıcıadı and parola != xparola):
    print("Kullanıcı Adı ve Parola Hatalı!..")

elif (kullanıcıadı == xkullanıcıadı and parola == xparola):
    print("Giriş İşlemi Başarılı!..")

else:
    print("Geçersiz İşlem!..")