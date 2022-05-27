
#-Gerekli modulleri projeye dahil ediyoruz 

import string
import random



#-Sifre içerisinde kullanılacak özel karakterler
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!.@#>-$%_^&'=*:(<)")
characters = list(string.ascii_letters + string.digits + "!.@#>-$%_^&'=*:(<)")

def generate_random_password():
	#-Kullanıcıdan sifre uzunluğunu alıyoruz
	length = int(input("Şifre uzunluğunu giriniz: "))

	#-Karakter türü sayılarını alıyoruz
	alphabets_count = int(input("Sifrede kaç adet harf olmalı: "))
	digits_count = int(input("Sifrede kaç adet rakam olmalı: "))
	special_characters_count = int(input("Sifrede kaç adet özel karakter olmalı: "))

	characters_count = alphabets_count + digits_count + special_characters_count

	#-Toplam uzunluk karakter sayısından uzunmu kontrol ediyor toplam uzunluktan büyük olduğu halde yazdırmıyoruz
	if characters_count > length:
		print("Karakterlerin toplam sayısı şifre uzunluğundan büyük")
		return


	#-Sifreyi baslatıyoruz
	password = []
	
	#-Rastgele özel karakter atıyoruz
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))


	#-Rastgele rakam atıyoruz
	for i in range(digits_count):
		password.append(random.choice(digits))


	for i in range(special_characters_count):
		password.append(random.choice(special_characters))


	#-Ttoplam karakter sayısı şifre uzunluğundan azsa uzunluğa eşit yapmak için rastgele karakterler ekliyoruz
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))


	#-Şifreyi karıştırıyoruz
	random.shuffle(password)

	#-Liste tipini string tipe dönüştürüp yazdırıyoruz
	print("".join(password))



generate_random_password()