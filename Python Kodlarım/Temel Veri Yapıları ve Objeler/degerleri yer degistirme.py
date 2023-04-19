"""Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin."""

a=int(input("birinci sayiyi giriniz:"))
b=int(input("ikinci sayiyi giriniz:"))

a,b=b,a

print(a,b)