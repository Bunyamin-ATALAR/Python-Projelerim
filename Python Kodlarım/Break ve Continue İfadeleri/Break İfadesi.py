i=0
while (i<10):
    if (i==7):
        break
    print("i:",i)
    i+=1

#Burda normalde ifademiz 1'den 10'a kadar ekrana yazılır 10 ifadesi hariç.#
#Ama ifade de if break formulü kullanılmış yani i değeri 7 olunca dur demişiz.#
#O yüzden i değeri 0'dan 6'ya kadar ekrana yazıldı 7'de durdu 7'yi ekrana yazmadı false olarak algıladı.#
#break formulü sadece if ifadesiyle birlikte kullanılır.#
#Zaman zaman iç içe ifadeleriylede kullanıcaz ve iç içe de sadece içe kısmını da durdurabilir.#