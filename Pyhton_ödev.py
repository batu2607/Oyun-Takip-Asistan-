    
import json
import os
import time

DATA_FILE = "oyun_takip_verileri.json"


def verileri_yukle():
  if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as dosya:
      return json.load(dosya)
  return {}


def verileri_kaydet(veriler):
  with open(DATA_FILE, "w", encoding="utf-8") as dosya:
    json.dump(veriler, dosya, ensure_ascii=False, indent=4)


def oyun_ekle(veriler):
  print("\n--- Yeni Oyun Ekle ---")
  isim = input("Oyunun adi: ").strip()
  if not isim:
    print("Oyun adi bos olamaz!")
    return

  print(
      "İpucu: Oyunun kısayoluna veya .exe dosyasına Shift tuşuna basılı"
      " tutarak sağ tıklayıp 'Yol olarak kopyala' diyebilirsin."
  )
  yol = (
      input("Oyunun dosya yolu (.exe veya kısayol): ").strip().strip('"')
  )

  if not yol:
    print("Dosya yolu boş olamaz!")
    return

  veriler[isim] = {"yol": yol, "toplam_sure": 0.0}
  verileri_kaydet(veriler)
  print(f"'{isim}' basariyla eklendi!")


def oyun_sil(veriler):
  oyunlari_listele(veriler)
  if not veriler:
    return

  print("\n--- Oyun Sil ---")
  secim = input("Silmek istediginiz oyunun adini tam olarak yazin: ").strip()

  if secim in veriler:
    del veriler[secim]
    verileri_kaydet(veriler)
    print(f"'{secim}' basariyla silindi!")
  else:
    print("Bu isimde bir oyun bulunamadi!")


def oyunlari_listele(veriler):
  if not veriler:
    print("\nHenuz kayitli oyun yok.")
    return

  print("\n--- Kayitli Oyunlar ---")
  for i, (isim, bilgi) in enumerate(veriler.items(), 1):
    dakika = bilgi["toplam_sure"] / 60
    print(f"{i}. {isim} - Toplam Oynama: {dakika:.2f} dakika")


def oyun_oyna(veriler):
  oyunlari_listele(veriler)
  if not veriler:
    return

  secim = input("\nOynamak istediginiz oyunun adini yazin: ").strip()

  if secim not in veriler:
    print("Boyle bir oyun bulunamadi!")
    return

  oyun_bilgisi = veriler[secim]
  yol = oyun_bilgisi["yol"]

  print(f"\n'{secim}' baslatiliyor...")

  baslangic_zamani = time.time()

  try:
    os.startfile(yol)

    print(
        "Süre takip ediliyor! İşiniz bitip oyunu kapattığınızda buraya dönüp"
        " ENTER tuşuna basın."
    )
    input(
        "--- OYUN BİTTİĞİNDE BURAYA GELİP ENTER'A BASIN ---"
    )  

  except Exception as e:
    print(f"\nOyun baslatilirken hata olustu: {e}")
    return

  bitis_zamani = time.time()
  gecen_sure = bitis_zamani - baslangic_zamani

  oyun_bilgisi["toplam_sure"] += gecen_sure
  verileri_kaydet(veriler)

  print(
      "\n[KONTROL RAPORU] Oyun oturumu kaydedildi!"
      f"\n- Bu oturumda gecen sure: {gecen_sure:.2f} saniye"
      f" ({(gecen_sure/60):.2f} dakika)"
      f" \n- Dosyaya kaydedilen yeni toplam sure:"
      f" {(oyun_bilgisi['toplam_sure']/60):.2f} dakika"
  )


def ana_menu():
  veriler = verileri_yukle()
  while True:
    print("\n==============================")
    print("   OYUN TAKIP VE SURE OLCER")
    print("==============================")
    print("1. Oyunlari Listele & Sureleri Gor")
    print("2. Yeni Oyun Ekle")
    print("3. Oyun Oyna ve Sure Tut")
    print("4. Oyun Sil")
    print("5. Cikis")

    secim = input("Seciminiz (1-5): ").strip()

    if secim == "1":
      oyunlari_listele(veriler)
    elif secim == "2":
      oyun_ekle(veriler)
    elif secim == "3":
      oyun_oyna(veriler)
    elif secim == "4":
      oyun_sil(veriler)
    elif secim == "5":
      print("Programdan cikiliyor. Iyi gunler!")
      break
    else:
      print("Gecersiz secim, lutfen 1-5 arasi bir sayi girin.")


if __name__ == "__main__":
  ana_menu()    