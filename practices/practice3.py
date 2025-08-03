# ===============================
# Day 1 – Conditionals Practice (if / elif / else)
# ===============================



# 1. Kullanıcıdan bir sayı al, pozitif/negatif/sıfır olup olmadığını yazdır.
a = float(input("Bir sayı giriniz: "))
if a > 0 :
    print("Pozitif")
elif a < 0 :
    print("Negatif")  ,
else : 
    print("Sıfır")
# 2. Kullanıcıdan yaş al, 18 veya daha büyükse "Ehliyet alabilir", küçükse "Ehliyet alamaz" yazdır.
age = int(input("Yaşınızı giriniz:"))
if age >=18:
    print("Ehliyet alabilir")
else:
    print("Ehliyet alamaz") 

# 3. Kullanıcıdan üç sayı al, en büyüğünü ekrana yazdır.
num_list = []
num_list = [float(input("Birinci sayıyı giriniz: ")), 
            float(input("İkinci sayıyı giriniz: ")), 
            float(input("Üçüncü sayıyı giriniz: "))]
max_num = num_list[0]
for num in num_list:
    if num > max_num:
        max_num = num
print("En büyük sayı:", max_num)

# 4. Kullanıcıdan bir sayı al, sayının çift mi tek mi olduğunu ekrana yazdır.
num_x = int(input("Bir sayı giriniz1: "))

if num_x  %  2 == 0:
    print("Girdiğiniz sayı çift bir sayıdır.")
elif num_x % 2 == 1:
    print("Girdiğiniz sayı tek bir sayıdır.")
else:
    print("Girdiğiniz sayı tam sayı değildir")




# 5. Kullanıcıdan 0-100 arasında bir not al.
#90-100: "A", 80-89: "B", 70-79: "C", 60-69: "D", 0-59: "F"
#Harf notunu ekrana yazdır.

student_note = int(input("Notunuzu giriniz: "))
note_words = ""
if  90<= student_note <= 100:
    note_words = "A"
elif 80<= student_note <= 89:
    note_words = "B"
elif 70<= student_note <= 79:
    note_words = "C"
elif 60 <= student_note <= 69:
    note_words = "D"
else:
    note_words = "F"
    print("Dersten kaldınız.")
    

print(f"Harf Notunuz {note_words}")


# 6. Kullanıcıdan bir gün ismi al.
# Hafta sonu ("cumartesi", "pazar") ise "Hafta sonu",
# diğer günler için "Hafta içi" yazdır.
week_of_day = input("Bir gün ismi giriniz: ")
week_day = ["pazartesi","salı","çarşamba","perşembe","cuma" ]
week_end = ["cumartesi","pazar"]
if week_of_day.lower() in week_day:
    print("Haftaiçi")
else:
    print("Haftasonu")


# 7. Kullanıcıdan şifre al.
# Eğer şifre "python123" ise "Giriş başarılı", değilse "Hatalı şifre" yazdır.

while True :
 password = input("Şifrenizi giriniz: ")
 if password == "python123":
     print("Giriş başarılı!")
     break
 else:
     print("Hatalı şifre!")
     

# 8. Kullanıcıdan 1-50 arasında bir sayı al.


while True:
    num_y = int(input("1 ve 50 arasında bir sayı giriniz: "))
    if 1 <= num_y <= 50:
        if num_y % 3 == 0 and num_y % 5 == 0:
            print("FizzBuzz")
        elif num_y % 3 == 0:
            print("Fizz")
        elif num_y % 5 == 0:
            print("Buzz")
        else:
            print(num_y)
        break
    else:
        print("Lütfen 1 ve 50 arasında bir sayı giriniz.")

# Hem 3'e hem 5'e bölünüyorsa "FizzBuzz"
# Sadece 3'e bölünüyorsa "Fizz"
# Sadece 5'e bölünüyorsa "Buzz"
# Hiçbirine bölünmüyorsa sayının kendisini yazdır.
