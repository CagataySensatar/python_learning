# Python Operatörler ve Koşullu İfadeler Öğretici

# 1. Aritmetik Operatörler
print("--- Aritmetik Operatörler ---")
a = 10
b = 3
print(f"Toplama: {a + b}")        # 13
print(f"Çıkarma: {a - b}")        # 7
print(f"Çarpma: {a * b}")         # 30
print(f"Bölme: {a / b}")          # 3.333...
print(f"Tam Bölme: {a // b}")     # 3
print(f"Mod: {a % b}")            # 1
print(f"Üs: {a ** b}")            # 1000

# 2. Karşılaştırma Operatörleri
print("\n--- Karşılaştırma Operatörleri ---")
x = 5
y = 8
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")    # Eşit mi?
print(f"x != y: {x != y}")    # Eşit değil mi?
print(f"x < y: {x < y}")      # Küçük mü?
print(f"x > y: {x > y}")      # Büyük mü?
print(f"x <= y: {x <= y}")    # Küçük eşit mi?
print(f"x >= y: {x >= y}")    # Büyük eşit mi?

# 3. if-elif-else Kullanımı
print("\n--- if-elif-else Örneği ---")
puan = 75

if puan >= 90:
    print("A - Mükemmel")
elif puan >= 80:
    print("B - İyi")
elif puan >= 70:
    print("C - Orta")
elif puan >= 60:
    print("D - Geçer")
else:
    print("F - Başarısız")

# 4. Mantıksal Operatörler
print("\n--- Mantıksal Operatörler ---")
yas = 25
mezun = True

if yas >= 18 and mezun:
    print("İş başvurusu yapabilirsiniz")
    
if yas < 18 or not mezun:
    print("İş başvurusu yapamazsınız")

# 5. İç içe if kullanımı
print("\n--- İç İçe if Örneği ---")
kullanici_adi = "admin"
sifre = "1234"

if kullanici_adi == "admin":
    if sifre == "1234":
        print("Giriş başarılı!")
    else:
        print("Şifre yanlış!")
else:
    print("Kullanıcı adı yanlış!")

# 6. While Döngüsü ile Koşul Örneği
    print("\n--- While Döngüsü Örneği ---")
    sayac = 0
    while sayac < 3:
        print(f"Sayaç: {sayac}")
        sayac += 1

    # 7. Ternary Operator Örneği
    print("\n--- Ternary Operator ---")
    yas = 20
    durum = "Yetişkin" if yas >= 18 else "Çocuk"
    print(f"Durum: {durum}")

    # 8. in Operatörü Örneği
    print("\n--- in Operatörü ---")
    meyveler = ["elma", "armut", "muz"]
    print(f"'elma' listede mi?: {'elma' in meyveler}")
    print(f"'kiraz' listede mi?: {'kiraz' in meyveler}")

    # 9. is Operatörü Örneği
    print("\n--- is Operatörü ---")
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    print(f"a is b: {a is b}")  # False
    print(f"a is c: {a is c}")  # True