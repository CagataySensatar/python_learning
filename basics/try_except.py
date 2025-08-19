# basics/try_except.py
"""
TRY / EXCEPT — KONU ANLATIMI
Bu dosyada try/except ailesinin tüm parçalarını örneklerle göreceksin:
- try / except (temel kullanım)
- Birden fazla except, birden çok hatayı tek except ile yakalama
- 'as e' ile hata nesnesine erişme (mesaj/log)
- else (try hatasız biterse çalışır)
- finally (her durumda çalışır: temizlik işleri)
- raise (kasıtlı hata fırlatma)
- Özel (custom) exception sınıfı tanımlama ve kullanma
-input() → her zaman str döner. Biz int() veya float() gibi fonksiyonlarla çevirmedikçe Python onu otomatik sayı yapmaz.

"""

# ------------------------------------------------------
# 1) TEMEL KULLANIM: try / except
# try bloğuna "hata verebilecek" kodu yazarsın.
# except bloğu, belirttiğin tipte bir hata oluşursa devreye girer.
# ------------------------------------------------------

def bol(a, b):
    try:
        sonuc = a / b
        return sonuc
    except ZeroDivisionError:
        print("Sıfıra bölme hatası yakalandı. None döndürülüyor.")
        return None

print("bol(10, 2) ->", bol(10, 2))  # 5.0
print("bol(10, 0) ->", bol(10, 0))  # None


# ------------------------------------------------------
# 2) BİRDEN FAZLA except
# Farklı hata türleri için farklı tepkiler verebilirsin.
# except ValueError | TypeError:  (Python 3.10+) ile çoklu hata yakalanabilir.
# Eski yöntem: except (ValueError, TypeError):
# ------------------------------------------------------

def sayiya_cevir(metin):
    try:
        return int(metin)
    except ValueError:
        print("ValueError: Sayıya çevrilemedi:", metin)
        return None

print("sayıya_cevir('42') ->", sayiya_cevir("42"))
print("sayıya_cevir('4x') ->", sayiya_cevir("4x"))


def toplam(liste):
    try:
        # TypeError (liste değilse) veya ValueError (elemanlardan biri sayı değilse) yaşanabilir.
        return sum(liste)
    except TypeError as e:
        print("TypeError: Toplanacak yapı uygun değil:", e)
        return None

print("toplam([1,2,3]) ->", toplam([1, 2, 3]))
print("toplam(5) ->", toplam(5))  # TypeError örneği


# ------------------------------------------------------
# 3) 'as e' KULLANIMI
# Hata nesnesine erişip mesajını/logunu alırsın.
# ------------------------------------------------------

def tamsayi_oku(metin):
    try:
        return int(metin)
    except ValueError as e:
        print("Hata mesajı:", e)  # örn: invalid literal for int() with base 10: '4x'
        return None

tamsayi_oku("4x")


# ------------------------------------------------------
# 4) else ve finally
# else: try bloğu HATASIZ tamamlanınca çalışır (başarılı akış sonrası işler).
# finally: HATA OLSA DA OLMASA DA daima çalışır (kapatma/temizlik için).
# ------------------------------------------------------

def ornek_else_finally(deger):
    try:
        x = int(deger)  # burada hata olabilir
    except ValueError:
        print("Geçersiz sayı.")
        return None
    else:
        # try hatasız bittiyse burası çalışır
        print("Dönüşmeden sonra iki katı:", x * 2)
        return x * 2
    finally:
        # her durumda çalışır
        print("finally: temizlik/kapanış işlemleri burada yapılır.")

ornek_else_finally("21")
ornek_else_finally("xx")


# ------------------------------------------------------
# 5) raise — Kasıtlı Hata Fırlatma
# İş kuralı ihlali gibi durumlarda kontrollü olarak hata üretmek için kullanılır.
# raise ValueError("mesaj") gibi.
# ------------------------------------------------------

def not_kontrol(not_degeri):
    if not (0 <= not_degeri <= 100):
        raise ValueError("Not 0–100 aralığında olmalı.")
    return True

# Kullanan taraf try/except ile sarmalayabilir:
try:
    not_kontrol(120)
except ValueError as e:
    print("raise ile fırlatılan hata yakalandı:", e)


# ------------------------------------------------------
# 6) ÖZEL (CUSTOM) EXCEPTION
# Kendi hata sınıfını yazıp belirli durumları bu sınıfla ifade edebilirsin.
# ------------------------------------------------------

class InputFormatError(Exception):
    """Beklenen giriş formatı sağlanmadığında fırlatılır."""
    pass

def parse_cift_sayi(metin):
    """
    Beklenen format: 'a,b'  (örn: '3,5')
    Hatalı formatta InputFormatError fırlatır,
    sayısal çevrim hatalarında ValueError fırlatır.
    """
    if "," not in metin:
        raise InputFormatError("Virgülle ayrılmış iki değer bekleniyor. Örn: '3,5'")
    sol, sag = metin.split(",", 1)
    return int(sol), int(sag)

# Kullanım:
for girdi in ["3,5", "9;x", "7-8"]:
    try:
        print("parse_cift_sayi:", girdi, "->", parse_cift_sayi(girdi))
    except InputFormatError as e:
        print("Format hatası:", e)
    except ValueError as e:
        print("Sayıya çevirme hatası:", e)


# ------------------------------------------------------
# 7) İYİ PRATİKLER (KISA NOTLAR)
# - 'try' bloğunu MÜMKÜN OLDUĞUNCA KÜÇÜK tut (sadece riskli satırlar).
# - Spesifik except kullan; 'except Exception' çok geniştir (gerekmedikçe kullanma).
# - Hataları tamamen yutma (boş except) yapma; en azından log/mesaj bırak.
# - raise ile iş kurallarını netleştir (erken doğrulama).
# - else/finally bloklarını doğru yerde kullan (başarılı akış ve temizlik).
# ------------------------------------------------------


if __name__ == "__main__":
    print("Demo tamamlandı.")
