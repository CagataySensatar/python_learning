# basics/variables_and_type.py
# Bu dosya, Python'da değişkenler ve veri tipleri ile ilgili temel bilgileri içermektedir.
# Python'da Veri Tipleri ve Tip Belirleme
# Python dinamik olarak değişkenlerin tipini belirler

# type() fonksiyonu ile bir değişkenin tipini öğrenebiliriz
# id() fonksiyonu ile bir değişkenin bellek adresini öğrenebiliriz

# Örnek değişkenler ve tipleri
x = 5
print(f"x'in değeri: {x}, tipi: {type(x)}")  # <class 'int'>

y = "Merhaba"
print(f"y'nin değeri: {y}, tipi: {type(y)}")  # <class 'str'>

z = 3.14
print(f"z'nin değeri: {z}, tipi: {type(z)}")  # <class 'float'>

# Python değişkenlere değer atandığında otomatik olarak tip belirler
# Bu özelliğe "dinamik tipleme" denir
# Integer (int) - Tam sayılar
# Kullanım alanları: Sayaçlar, indeksler, yaş, miktar gibi tam sayı gerektiren durumlar
# Örnek: Ürün adedi, kullanıcı yaşı, döngü sayacı
int_variable = 6

# Float - Ondalıklı sayılar
# Kullanım alanları: Bilimsel hesaplamalar, finansal işlemler, ölçümler
# Örnek: Sıcaklık değerleri, para birimi, ağırlık ölçümleri
float_variable = 7.5

# String (str) - Metin dizileri
# Kullanım alanları: Metin işleme, kullanıcı girdileri, dosya isimleri
# Örnek: Kullanıcı adı, adres bilgisi, mesajlar
string_variable = "Selamlar"

# Boolean (bool) - Mantıksal değerler
# Kullanım alanları: Koşul kontrolleri, durum kontrolü, bayraklar
# Örnek: Kullanıcı giriş durumu, form doğrulama
bool_variable = True

# Liste (List)
# Kullanım alanları: Sıralı veri koleksiyonları, dinamik veri yapıları
# Özellikler: Değiştirilebilir, sıralı, farklı veri tipleri içerebilir
# Örnek: Alışveriş sepeti, to-do listesi, menü öğeleri
empty_list = []
my_list = [1, 2, 3, "Python", True]

# Sözlük (Dictionary)
# Kullanım alanları: Anahtar-değer eşleşmeleri, veri organizasyonu
# Özellikler: Değiştirilebilir, anahtarlar benzersiz olmalı
# Örnek: Kullanıcı profilleri, yapılandırma ayarları, dil çevirileri
empty_dict = {}
my_dict = {"isim": "Ali", "yaş": 25}

# Tuple
# Kullanım alanları: Değişmez veri koleksiyonları, çoklu değer döndürme
# Özellikler: Değiştirilemez, sıralı, performanslı
# Örnek: Koordinatlar, RGB renk değerleri, tarih bilgisi
empty_tuple = ()
my_tuple = (1, 2, "Python")

# Complex - Karmaşık sayılar
# Kullanım alanları: Bilimsel hesaplamalar, mühendislik uygulamaları
# Örnek: Elektrik mühendisliği hesaplamaları, sinyal işleme
complex_num = 3 + 4j

# Tip dönüşümü örnekleri
# Farklı veri tipleri arasında dönüşüm yapılabilir
sayi1 = "42"  # String
sayi2 = int(sayi1)  # Integer'a dönüşüm
sayi3 = float(sayi1)  # Float'a dönüşüm
print("Sayı1: ", sayi1, "Tipi",type(sayi1))
print("Sayı2: ", sayi2, "Tipi", type(sayi2))
print("Sayı3: ", sayi3, "Tipi", type(sayi3))

# Set (Küme)
# Kullanım alanları: Benzersiz elemanlar, küme işlemleri
# Özellikler: Değiştirilebilir, sırasız, tekrarsız elemanlar
empty_set = set()
my_set = {1, 2, 3, "Python"}

# None tipi
# Kullanım alanları: Boş değer temsili, varsayılan parametre değerleri
# Örnek: Fonksiyon dönüş değeri, başlangıç değeri
none_variable = None
print(f"None değişkeni tipi: {type(none_variable)}")

# Bytes
# Kullanım alanları: Binary veri işleme, dosya işlemleri
# Örnek: Dosya okuma, ağ iletişimi
bytes_data = b"Hello"
print(f"Bytes veri tipi: {type(bytes_data)}")

# Range
# Kullanım alanları: Sayı dizileri, döngüler
# Örnek: For döngüleri, liste oluşturma
range_example = range(5)
print(f"Range örneği: {list(range_example)}")








