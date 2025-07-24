import math
# Matematiksel Operatörler Örnekleri

a = float(input("İlk sayıyı girin: "))
b = float(input("İkinci sayıyı girin:"))

# Toplama
toplam = a + b
print("Toplama:", toplam)

# Çıkarma
cikarma = a - b
print("Çıkarma:", cikarma)

# Çarpma
carpma = a * b
print("Çarpma:", round(carpma,2))

# Bölme
bolme = a / b
print("Bölme:", round(bolme, 3))

# Tam bölme (bölümün tam kısmı)
tam_bolme = a // b
print("Tam Bölme:", tam_bolme)

# Kalan (mod alma)
mod = a % b
print("Kalan (mod):", mod)

# Üs alma
us = a ** b
print("Üs alma:", us)

# Kareköklü ve trigonometrik işlemler
karekok = math.sqrt(a)
print(" a sayısının karekökü:", karekok)

mutlak_deger = abs(b)
print(" b sayısının mutlak değeri:", mutlak_deger)

math_sin_a = math.sin(a)
math_sin_b = math.sin(b)

print("sin(a):", round(math_sin_a, 3))
print("sin(b):" ,round(math_sin_b, 3))

sinus_toplam = math_sin_a + math_sin_b
print("a ve b'nin sinüslerinin toplamı:", sinus_toplam)


