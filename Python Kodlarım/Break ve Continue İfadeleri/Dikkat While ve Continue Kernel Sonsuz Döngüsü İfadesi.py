i=0
while (i<10):
    if (i==3):
        i += 1  #Buraya (i+=1) komutunu girmezsen kernel sonsuz ifade döngüsüne girer.#
        continue
    print("i:", i)
    i += 1

#Burda kodumuz normalde 0,1,2 ye kadar çalışır ve sonsuz döngüye girer çünkü continue ifadesi sürekli döngüyü#
#başa döndürdüğü için döngü öylece kalır.Bu yüzden (i+=1) ifadesini continue'den öncede kullanmamız gerekir.#
