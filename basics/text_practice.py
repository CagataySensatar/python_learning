#Bu örnekte, kullanıcıdan bir metin alıp üzerinde çeşitli işlemler yapacağız.

# Öncelikle kullanıcıdan bir metin girmesini istiyoruz.
text = input("Bir metin giriniz:")
print("Girdiğiniz metin:", text)

# Şimdi, girdiğiniz metni ters çevireceğiz.
# Bunun için dilimleme yöntemini kullanıyoruz: [::-1] ifadesi metni sondan başa doğru sıralar.
reversed_text = text[::-1]
print("Ters çevrilmiş metin:", reversed_text)

# Metnin her ikinci karakterini ekrana yazdıralım.
# [::2] ile metnin 0. karakterinden başlayıp ikişer atlayarak karakterleri seçiyoruz.
print("Her ikinci karakter:", text[::2])

# Metni tamamen büyük harfe çevirelim.
# upper() fonksiyonu tüm harfleri büyütür.
uppercase_text = text.upper()
print("Büyük harfli metin:", uppercase_text)

# Metni tamamen küçük harfe çevirelim.
# lower() fonksiyonu tüm harfleri küçültür.
lowercase_text = text.lower()
print("Küçük harfli metin:", lowercase_text)

# Metindeki tüm boşlukları kaldırıyoruz.
no_spaces = text.replace(" ", "")
print("Boşluksuz metin:", no_spaces)

# Metni boşluklardan bölerek kelime sayısını buluyoruz.
word_count = len(text.split())
print("Kelime sayısı:", word_count)





