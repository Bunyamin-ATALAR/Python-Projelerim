"""Kullanıcıdan aldığınız
3 tane sayıyı çarparak ekrana yazdırın.
Ekrana yazdırma işlemini format metoduyla yapmaya çalışın."""

a=int(input("birinci sayiyi giriniz:"))
b=int(input("ikinci sayiyi giriniz:"))
c=int(input("üçüncü sayiyi giriniz:"))
print("bilgiler kaydediliyor...")
carp=a*b*c
print("Cevap {}".format(carp))
