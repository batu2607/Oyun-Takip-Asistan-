Oyun Takip ve Süre Ölçer

Bu proje, Python ile geliştirilmiş konsol tabanlı bir oyun başlatma ve oynama süresi takip asistanıdır.
Kullanıcının bilgisayarındaki oyunları listelemesini, yeni oyunlar eklemesini, oyunları başlatarak oturum sürelerini
saniye bazında takip etmesini ve kalıcı olarak JSON formatında saklamasını sağlar.

Özellikler
- **Oyun Ekleme & Silme:** Bilgisayarınızdaki oyunların `.exe` veya kısayol yollarını sisteme kaydedebilir, istemediğiniz oyunları silebilirsiniz.
- **Oyun Listeleme:** Kayıtlı tüm oyunları ve bu oyunlarda toplam kaç dakika geçirdiğinizi listeleyebilirsiniz.
- **Süre Takibi:** Oyunu başlattığınız andan itibaren oturum süresini hesaplar ve kapatıldığında toplam süreye ekler.
- **Kalıcı Veri Tabanı:** Tüm veriler `oyun_takip_verileri.json` dosyasında otomatik olarak saklanır, program kapatılsa bile veriler silinmez.

Kullanılan Teknolojiler
- **Python 3.x**
- **JSON Modülü** (Veri saklama ve okuma için)
- **OS & Time Modülleri** (Dosya yönetimi ve zaman hesaplamaları için)

