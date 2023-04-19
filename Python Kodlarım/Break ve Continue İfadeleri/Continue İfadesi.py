for i in range(0,11):
    if (i==3 or i==5):
        continue
    print("i:",i)

#Burda (if continue) i=3 ve i=5 olunca sorguyu başa alarak tekrar döndür demiş oluyoruz.#
#Bu sayede i 3'e ve 5'e gelince bu sayıları ekrana yazmıyor ve i'yi güncelleyerek döngüyü başa alıyor#
#i güncellenince en başa dönmüyor bir sonraki ifadeden devam ediyor#
#1,2,4,6,7,8,9,10#