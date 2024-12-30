
import math
import time 

class Hesapmakinesi:
    def __init__(self):
        print("Hesap Makinesi Başlatıldı.")

    def hesapla(self, ifade):
        try:
            izinli_fonksiyonlar = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
            izinli_fonksiyonlar.update({"abs": abs, "round": round})

            sonuc = eval(ifade, {"__builtins__": None}, izinli_fonksiyonlar)
            return sonuc
        except Exception as e:
            return f"Hata: {str(e)}"

    def calistir(self):
        print("Hesap Makinesi'ne Hoş Geldiniz!")
        print("İstediğiniz matematiksel ifadeyi yazabilirsiniz.")
        print("Örnekler:")
        print(" - Toplama: 3 + 5")
        print(" - Kök alma: sqrt(16)")
        print(" - Logaritma: log(8, 2)")
        print(" - Sinüs: sin(pi/2)")
        print(" - Çıkmak için 'q' yazın.")
        
        while True:
            ifade = input("\nİfadenizi girin: ")
            print("Bir saniye bekletiyoruz..")
            time.sleep(1)

            if ifade.lower() == 'q':
                print("Hesap makinesi kapatılıyor.")
                break
            sonuc = self.hesapla(ifade)
            print("Sonuç:", sonuc)


hesap_makinesi = Hesapmakinesi()
hesap_makinesi.calistir()
