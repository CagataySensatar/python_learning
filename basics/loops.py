# ==========================================
# PYTHON'DA DÖNGÜLER (LOOPS) DETAYLI ANLATIM
# ==========================================

# 1️⃣ FOR DÖNGÜSÜ (for loop)
# Bir listenin, dizinin veya belli aralıktaki sayıların üzerinde sırayla gezinmek için kullanılır.

print("FOR Döngüsü ile liste elemanlarını yazdırma:")
meyveler = ["elma", "armut", "muz"]
for meyve in meyveler:
    print(meyve)  # Her seferinde listenin bir elemanını alır ve yazdırır

# Mantık: Listenin başından sonuna kadar her bir eleman için bloğu çalıştırır.

print("\nFOR Döngüsü ile range() kullanmak:")
# range(5) => 0, 1, 2, 3, 4 (5 dahil değil)
for i in range(5):
    print(i)

print("\nFOR Döngüsü ile başlangıç, bitiş ve adım kullanmak:")
# range(başlangıç, bitiş, adım)
for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)

# ------------------------------------------------------------

# 2️⃣ WHILE DÖNGÜSÜ (while loop)
# Belirli bir koşul doğru olduğu sürece çalışır.
print("\nWHILE Döngüsü ile sayaç örneği:")
sayi = 1
while sayi <= 5:
    print(sayi)
    sayi += 1  # Sayaç her seferinde 1 artar. Koşul yanlış olunca döngü biter.

# Mantık: Koşul True olduğu sürece kod bloğu tekrar tekrar çalışır.

# ------------------------------------------------------------

# 3️⃣ break ve continue Kullanımı
print("\nFOR Döngüsünde break kullanımı (döngüyü kırma):")
for i in range(10):
    if i == 5:
        print("Döngü kırıldı!")
        break  # Döngü tamamen sona erer
    print(i)

print("\nFOR Döngüsünde continue kullanımı (turu atlama):")
for i in range(1, 6):
    if i == 3:
        continue  # Bu turdaki işlemleri atla, döngüye başa dön
    print(i)

# ------------------------------------------------------------

# 4️⃣ for-else ve while-else Kullanımı
# Döngü 'break' ile kırılmazsa, else bloğu çalışır.
print("\nFOR Döngüsünde else kullanımı:")
for i in range(3):
    print(i)
else:
    print("Döngü tamamlandı!")  # break ile çıkılmazsa çalışır

print("\nWHILE Döngüsünde else kullanımı:")
n = 0
while n < 3:
    print(n)
    n += 1
else:
    print("While döngüsü doğal yolla tamamlandı!")  # break olmazsa çalışır

# ------------------------------------------------------------

# 5️⃣ İç İçe Döngüler (Nested Loops)
print("\nİç içe FOR döngüsü ile tablo gibi çıktı almak:")
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i: {i}, j: {j}")
# Mantık: Her 'i' değeri için tüm 'j' değerleri tek tek döner

# ------------------------------------------------------------

# 6️⃣ Kullanıcıdan Veri Alana Kadar While Döngüsü
print("\nKullanıcıdan doğru şifreyi girene kadar while döngüsü ile denetim:")
while True:
    parola = input("Parolanızı girin (python ile çıkış): ")
    if parola == "python":
        print("Doğru parola!")
        break
    else:
        print("Yanlış, tekrar deneyin.")

# ------------------------------------------------------------

# 7️⃣ Pratik Bilgiler

print("\nBir listeyi tersten gezmek:")
for x in reversed([1, 2, 3, 4]):
    print(x)

print("\nHem indeks hem değeri almak için enumerate kullanmak:")
liste = ["a", "b", "c"]
for i, val in enumerate(liste):
    print(f"İndeks: {i}, Değer: {val}")

# ------------------------------------------------------------

# Özet:
# - FOR: Eleman sayısı belli olan koleksiyonlarda/tekrarlarda tercih edilir.
# - WHILE: Koşul doğru oldukça, ne kadar döneceği belli olmayan durumlarda tercih edilir.
# - break: Döngüyü tamamen bitirir.
# - continue: Sadece ilgili turu atlar, döngüye devam eder.
# - for-else/while-else: Döngü doğal şekilde biterse 'else' bloğu çalışır.
# - İç içe döngüler: Çok boyutlu veri işleme ve tablo üretme için idealdir.
# - enumerate: Hem indeks hem elemanı aynı anda elde etmek için çok kullanışlıdır.
