# practice/try_except_practice.py
"""
TRY / EXCEPT — PRATIK SORULAR
Cevapları yazmadan sadece çözümlerini bu dosyada kodlayabilirsin.
"""

# 1) Güvenli bölme fonksiyonu yaz:
#    - Parametreler: a, b
#    - b = 0 ise ZeroDivisionError yakala ve None döndür.
#    - Başarılıysa sonucu döndür.

def bolme (a, b):
    try:
       sonuc = a / b 
       return sonuc
    except ZeroDivisionError:
        print ("Lütfen bölen sayısını 0 girmeyiniz.")
        return None
print(bolme(2,0))
print(bolme(2,1))

# 2) Kullanıcıdan tamsayı alana kadar input iste:
#    - int() çeviriminde ValueError yakala, uyarı ver ve tekrar iste.
#    - Doğru sayı girildiğinde sayıyı döndür.
while True :
    
    try:
     a = int(input("Lütfen bir tam sayı giriniz: "))
     print("Girdiğiniz sayı bir tam sayıdır.")
     break
    
    except ValueError:
        print("Lütfen tam sayı giriniz. ")
        


# 3) Bir listeyi toplayan fonksiyon yaz:
#    - Parametre: liste
#    - Parametre liste değilse TypeError yakala ve None döndür.
#    - Elemanlardan biri sayı değilse (toplam sırasında) uygun hata yönetimi yap.

def listfunc(liste):
   try:
      if not isinstance(liste , list):
        raise TypeError("Parametre liste olmalı.")
    
      toplam = 0
   
      for i in liste:
        try:
            i += toplam
        except ValueError:
            print("Girdiğiniz değerler birbirleri ile toplanamaz")
   except TypeError as e:
      print("Hata: ", e)
      return None
a = [1,2,3,4,3,2]
b= [1,2,3.1,"b","c"]
c= (1,2)  
listfunc(a)
listfunc(b)    
listfunc(c)
      


# 4) Metin olarak gelen değeri 'a,b' formatında parse eden fonksiyon yaz:
#    - Format yanlışsa kendi Custom Exception (ör. InputFormatError) fırlat.
#    - Doğru formatta ise iki sayıyı int'e çevirip tuple olarak döndür.
#    - Kullanan tarafta try/except ile test et.

# 5) else/finally kullanımını gösteren bir akış kur:
#    - try içinde riskli bir işlem yap (örn: int çevirimi)
#    - else içinde başarılı akışı yazdır
#    - finally içinde "temizlik" mesajı yazdır

# 6) Kullanıcıdan "3, 5, 10" gibi bir sayı listesi al:
#    - Bölüp sayılara çevirirken ValueError yakala (hatalı parça sayısını raporla)
#    - Sadece başarıyla çevrilenleri topla ve sonucu yazdır

# 7) Bir sözlükten istenen anahtarı oku:
#    - KeyError yakala ve "anahtar bulunamadı" yaz
#    - Anahtar varsa değeri döndür

# 8) İndeks erişimi:
#    - Bir listeden verilen index'i oku
#    - IndexError yakala, kullanıcıya liste sınırlarını bildir

# 9) raise kullanımı:
#    - Not değeri alan bir fonksiyon yaz (0–100 dışında ise ValueError fırlat)
#    - Kullanan tarafta try/except ile kontrol et

# 10) Bonus – çoklu except:
#     - Kullanıcıdan iki sayı iste, bölme yap
#     - ValueError (yanlış tip) ve ZeroDivisionError (0) durumlarını ayrı ayrı yakala
#     - Başarılı akışta sonucu yazdır
