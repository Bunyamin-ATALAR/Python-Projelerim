print("""******************************
Harf Notu Hesaplama
******************************
""")

vize1=int(input("İlk Vize Notunuzu Giriniz:"))
vize2=int(input("İkinci Vize Notunuzu Giriniz:"))
final=int(input("Final Notunuzu Giriniz:"))

fvize1=vize1*0.30
fvize2=vize2*0.30
ffinal=final*0.40

note= fvize1+fvize2+ffinal

print(note)

if note>=90:
    print("AA {} GEÇTİNİZ!..".format(note))

elif note>=85:
    print("BA {} GEÇTİNİZ!..".format(note))

elif note>=80:
    print("BB {} GEÇTİNİZ!..".format(note))

elif note>=75:
    print("CB {} GEÇTİNİZ!..".format(note))

elif note>=70:
    print("CC {} GEÇTİNİZ!..".format(note))

elif note>=65:
    print("DC {} GEÇTİNİZ!..".format(note))

elif note>=60:
    print("DD {} GEÇTİNİZ!..".format(note))

elif note>=55:
    print("FD {} GEÇTİNİZ!..".format(note))

elif 0<=note<55:
    print("FF {} KALDINIZ!..".format(note))

else:
    print("İşlem Hatası!..")