"""
PYTHON FONKSİYONLAR – KONU ANLATIMI (GÜNCEL)
----------------------------------------------
Fonksiyonlar, bir işi tekrar tekrar yazmak yerine tek yerde tanımlayıp gerektiğinde çağırmamızı sağlar.

SÖZDİZİMİ:
    def fonksiyon_adi(parametre1, parametre2, ...):
        # yapılacak işlemler
        return değer

return vs print:
- 'return': Fonksiyonun ürettiği değeri dışarıya verir, başka değişkene atanabilir veya başka işlemde kullanılabilir.
- 'print': Sadece ekrana yazar, dışarıya bir değer döndürmez.
- Genel kural: Eğer sonucu başka yerde kullanmak istiyorsan 'return', sadece göstermek istiyorsan 'print'.

-------------------------------------------------
1) Basit Fonksiyon
-------------------------------------------------
# def selam_ver():
#     ""Ekrana sabit bir selamlama yazar.""
#     print("Merhaba!")

# selam_ver()

-------------------------------------------------
2) Parametre Alan Fonksiyon
-------------------------------------------------
def selam_ver_isme(isim):
    ""Parametre olarak isim alır ve kişiye özel selamlama yapar.""
    print(f"Merhaba {isim}!")  # Burada return yok çünkü sadece ekrana yazdırıyoruz

selam_ver_isme("Çağatay")

-------------------------------------------------
3) Return ile Fonksiyon
-------------------------------------------------
def kare_al(sayi):
    ""Verilen sayının karesini döndürür.""
    return sayi ** 2

sonuc = kare_al(5)
print("Sonuç:", sonuc)

-------------------------------------------------
4) Birden Fazla Değer Döndürme
-------------------------------------------------
def islemler(sayi1, sayi2):
    ""Toplam ve çarpımı döndürür.""
    return sayi1 + sayi2, sayi1 * sayi2  # tuple döner

toplam, carpim = islemler(3, 4)
print("Toplam:", toplam, "Çarpım:", carpim)

-------------------------------------------------
5) Varsayılan Parametre
-------------------------------------------------
def selamla(isim="Misafir"):
    print(f"Hoş geldin {isim}!")

selamla()           # Hoş geldin Misafir!
selamla("Zeynep")   # Hoş geldin Zeynep!

-------------------------------------------------
6) Anahtar Kelime Parametreleri (**kwargs)
-------------------------------------------------
def kisi_bilgileri(**bilgiler):
    ""Sınırsız sayıda anahtar=değer çifti alır.""
    for key, value in bilgiler.items():  # .items() => [(key, value), ...] listesi
        print(f"{key}: {value}")

kisi_bilgileri(ad="Çağatay", yas=25, sehir="İstanbul")

Burada 'for key, value in bilgiler.items()' ifadesi:
- Her döngüde 'key' → anahtar, 'value' → değer olur.
- Çünkü .items() her öğeyi tuple olarak döner: ('ad', 'Çağatay')
- Yani tuple başına 1 indeks sayılır, tuple içi key ve value olarak ikiye ayrılır.

-------------------------------------------------
7) *args ile Sınırsız Parametre
-------------------------------------------------
def sayilari_topla(*sayilar):
    toplam = sum(sayilar)
    return toplam

print(sayilari_topla(1, 2, 3, 4))  # 10

-------------------------------------------------
8) İç İçe Fonksiyon
-------------------------------------------------
def dis_fonksiyon(metin):
    def ic_fonksiyon():
        return metin.upper()
    return ic_fonksiyon()

print(dis_fonksiyon("merhaba"))

-------------------------------------------------
9) Lambda Fonksiyon (Kısayol)
-------------------------------------------------
kare = lambda x: x ** 2
print(kare(6))

# map ile kullanımı
sayilar = [1, 2, 3]
print(list(map(lambda x: x + 10, sayilar)))  # [11, 12, 13]

-------------------------------------------------
ÖZET:
- print → ekrana yazar, dışarıya veri vermez.
- return → dışarıya veri verir, başka yerde kullanılabilir.
- **kwargs → sınırsız key=value parametresi
- *args → sınırsız sayıda normal parametre
- for key, value in dict.items() → dict’in key-value çiftlerini tuple tuple döner, otomatik olarak parçalanır.
- lambda → tek satırlık mini fonksiyon, özellikle kısa süreli dönüşüm, filtreleme, sıralama işlemlerinde kullanılır.
"""

# ----------------------------------------------------
# PRATİKLER
# ----------------------------------------------------

# 1. İsme özel selamlama (print kullanarak)
def selam_ver_isme(isim):
    print(f"Merhaba {isim}!")

selam_ver_isme("Çağatay")

# 2. İki sayının karesini döndür (return kullanarak)
def kare_al(sayi):
    return sayi ** 2

print(kare_al(5))

# 3. kwargs ile kişi bilgilerini yazdır
def kisi_bilgileri(**bilgiler):
    for key, value in bilgiler.items():
        print(f"{key}: {value}")

kisi_bilgileri(ad="Çağatay", yas=25, sehir="İstanbul")

# 4. Lambda ile listedeki sayıları 2 ile çarp
sayilar = [2, 4, 6]
print(list(map(lambda x: x * 2, sayilar)))  # [4, 8, 12]

# 5. args ile sınırsız sayı topla
def sayilari_topla(*sayilar):
    return sum(sayilar)

print(sayilari_topla(1, 2, 3, 4, 5))  # 15
