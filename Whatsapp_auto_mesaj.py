#-CMD Açıp pip install pywhatkit yazarak gerekli modülü yükleyiniz import pywhatkit as kit yazarak import ediniz

import pywhatkit as kit

try :               #-Mesaj gönderilecek numara             
    kit.sendwhatmsg("+90**********","Mesajınızı buraya yazmalısınız",20,49) #-Gönderme saati
    print("Gönderme başarılı.")  #-Mesaj giderse Gönderme başarılı yazsın
except :
    print("Beklenmeyen bir hata oluştu.") #-Gitmezse hata mesajı dönsün
