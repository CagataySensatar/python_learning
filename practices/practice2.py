# practice2.py

# Quiz: Aşağıdaki soruları kendi başınıza çözmeye çalışın.
# Cevapları kod olarak yazmayın, sadece soruları cevaplayın!

# 1. Bir değişken tanımlayın ve içine isminizi atayın. Sonra bu değişkeni ekrana yazdırın.
a = "Cagatay"
print(a)
# 2. Bir liste oluşturun ve içine 5 farklı sayı ekleyin. Listenin 3. elemanını ekrana yazdırın.
my_list= [1,2,3,4,5]
print(my_list[2])
# 3. Bir for döngüsü ile 1'den 10'a kadar olan sayıları ekrana yazdırın.
b = 10
for i in range(1, b):
    print(i)
# 4. Bir fonksiyon yazın, bu fonksiyon kendisine verilen iki sayının toplamını döndürsün.
def toplam (x ,y):
    return x + y
print(toplam(5, 10))    
# 5. Bir sözlük (dictionary) oluşturun, anahtarları 'ad', 'yaş', 'şehir' olsun ve uygun değerler atayın. 'şehir' anahtarının değerini ekrana yazdırın.
my_dict = {'ad' : 'cagatay', 'yas': 25, 'sehir': 'istanbul'} 
print(my_dict['sehir'])
# 6. Bir if-else yapısı ile bir sayının pozitif mi, negatif mi yoksa sıfır mı olduğunu ekrana yazdırın.
a = int(input("Bir sayi giriniz:"))
if a > 0:
    print("Pozitif")
elif a < 0:
    print("Negatif")
else:
    print("Sıfır")

# 7. Bir while döngüsü ile 5 kere "Python öğreniyorum!" yazdırın.
counter = 0
while counter < 5:
    print ("Pyhton öğreniyorum!")
    counter += 1

# 8. Bir string değişkeni alın ve tüm harflerini büyük harfe çevirip ekrana yazdırın.
var_string = "Selamlar herkese!"
print(var_string.upper())


# 9. Bir listeyi küçükten büyüğe sıralayın ve ekrana yazdırın.
my_list = [5, 8 ,9,6, 2, 1, 4, 3, 7]
my_list.sort()
print(my_list)  

# 10. Bir fonksiyon yazın, verilen bir listenin içindeki en büyük sayıyı döndürsün.
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def buyuk_sayi(liste):
    en_buyuk = liste[0]
    for sayi in liste[1:]:
        if sayi > en_buyuk:
            en_buyuk = sayi
    return en_buyuk
print(buyuk_sayi(list_numbers))
# Başarılar! Cevaplarınızı kod olarak bu dosyaya yazabilirsiniz.