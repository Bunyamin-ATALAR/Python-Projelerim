"""Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve
 sürücünün toplam ne kadar ödemesini gerektiğini hesaplayın."""

yakıt=float(input("kilometrede ne kadar yakıyor:"))
yol=int(input("kaç km yol yaptı:"))

"""Benzinin Litresine 30 TL dedim."""
litre=yol/100*yakıt
odeme=yol/100*yakıt*30

print("Fiyat {}TL\n{} Litre Yakıt Tüketmişsiniz.".format(odeme,litre))
