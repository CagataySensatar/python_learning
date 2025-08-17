# 1. Basit Fonksiyon
# "Merhaba Dünya!" yazdıran bir fonksiyon yaz.
# def selam_ver():
#     print("Hello World")

# 2. Parametre Alan Fonksiyon
# Parametre olarak isim alan ve kişiye özel selamlama yapan bir fonksiyon yaz.
# def selam_x(isim):
#     print(f"Merhaba {isim}")

# selam_x("Cagatay")

# 3. Return ile Fonksiyon
# Parametre olarak bir sayı al, karesini döndür.
# def square(num):
#     return num * num

# a = square(2)
# print(a)
# 4. Birden Fazla Değer Döndüren Fonksiyon
# İki sayı al, hem toplamını hem çarpımını döndür.

# def sumquare(x , y):
#     return x * y , y + x
# print(sumquare(2,3))

# 5. Varsayılan Parametre
# İsmi parametre olarak alan, ama verilmezse "Misafir" olarak varsayılan selamlama yapan fonksiyon yaz.

# def selamlama(isim = "Misafir"):
#     print(f"Selam {isim}")

# selamlama("Cagatay")
# selamlama()
# 6. *args Kullanımı
# Parametre olarak sınırsız sayıda sayı al, en küçüğünü döndür.
def arginfo (*args):
    return min(args)
print(arginfo(1,8,5,6,8,4,2))


# 7. **kwargs Kullanımı
# Parametre olarak sınırsız sayıda anahtar=değer al, her birini "anahtar: değer" formatında yazdır.
def infkwargs(**args):
    for key, value in args.items():
        print(f"Key: {key}, Value: {value}")
infkwargs(ad ="Cagatay",soyad = "Sensatar", yas = 25)

# 8. Lambda Fonksiyonu
# Bir lambda fonksiyonu ile verilen sayının küpünü hesapla.
kup_al = lambda x: x**3
print(kup_al(3))
# 9. Fonksiyon İçinde Fonksiyon
# Dış fonksiyon: sayının karesini al
# İç fonksiyon: karesinin 2 katını döndür
def kareal (sayi):
    a = sayi ** 2
    
    def ikiyecarp (a):
        return a *2
    return ikiyecarp(a)
print(kareal(2))


