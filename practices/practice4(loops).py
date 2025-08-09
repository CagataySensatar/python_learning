# 1. for döngüsü ile 1’den 10’a kadar olan sayıları ekrana yazdır.
for x in range(1,11):
    print(x)

# 2. Bir liste içinde verilen sayıların toplamını for döngüsüyle bulup yazdır.
numbers = [3, 7, 2, 9, 12, 5]
numbers = [3, 7, 2, 9, 12, 5]
sum_num1 = 0
for i in numbers:
    sum_num1 += i
print(sum_num1)



# 3. Kullanıcıdan pozitif bir sayı al. O sayının faktöriyelini while döngüsü ile hesapla.
faktoriyel = 1
a = int(input("Pozitif bir tam sayı giriniz :"))
if a < 0:
    print("Lütfen pozitif bir sayı giriniz.")
else:
    n = 1
    while n <= a:
        faktoriyel = faktoriyel * n
        n +=1
    print(f"Girdiğiniz sayının faktoriyel değeri: {faktoriyel} ")


# 4. for döngüsüyle 20’den 0’a kadar geriye doğru, yalnızca çift sayıları ekrana yazdır.
for i in range(20,0,-2):
    print(i)

# 5. Kullanıcıdan sürekli sayı al, girilen sayı negatifse döngüyü break ile bitir.
#    Her pozitif girişte “Giriş kabul edildi” yazdır.
while True:
    a = int(input("Bir sayı giriniz: "))
    if a < 0 :
        break
    else:
        print("Giriş kabul edildi!")

# 6. 1’den 20’ye kadar olan sayıları ekrana yazdır. Ancak 3’e tam bölünen sayıları atla (continue ile).
for i in range(1,20):
    if i % 3 == 0:
        continue
    else:
        print(i)

# 7. İç içe iki for döngüsü ile aşağıdaki çıktıyı elde et:
# *
# * *
# * * *
# * * * *
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
# """"""
# 8. Bir listeyi hem elemanlarını hem indekslerini beraber yazdır
#    (ör: “0: elma”, “1: armut” ... gibi).
meyveler = ["elma", "armut", "muz", "kiraz"]

for i, val in enumerate(meyveler):
    print(f"İndeks: {i}, Değer: {val}")

# 9. Bir sayı listesinde en büyük ve en küçük sayıyı bulmak için for döngüsüyle algoritma yaz.
sayi_listesi = [11, 45, 3, 22, 9, 17]
en_buyuk = sayi_listesi[0]
en_kucuk = sayi_listesi[0]
for i in sayi_listesi:
    if i > en_buyuk:
       en_buyuk = i
        
    elif i < en_kucuk:
        en_kucuk = i

print(en_kucuk)
print(en_buyuk)
# 10. Kullanıcıdan şifre alın. Şifre “python2024” ise döngüyü kır, yanlışsa tekrar denet (sonsuz while döngüsü ile).


while True:
    a = input("Şifre giriniz: ")
    if a == "python2024":
        print("Giriş başarılı!")
        break
        
    else:
        print("Şifre yanlış!")
        
# Bonus: Bir listenin yalnızca pozitif elemanlarından oluşan yeni bir liste oluştur.
sayilar = [5, -4, 7, 0, -3, 2, -6, 9]
yeni_liste = []
for i in sayilar:
    if i >=0:
       yeni_liste.append(i)

print(yeni_liste)