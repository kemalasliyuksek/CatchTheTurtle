# 🐢 Catch The Turtle (Kaplumbağayı Yakala)

Bu proje, Python'un `turtle` kütüphanesi kullanılarak geliştirilmiş basit bir oyundur. Oyuncunun rastgele konumlarda beliren kaplumbağayı tıklayarak puan kazanması amaçlanır.

## 🎮 Oyun Hakkında

- **Oyun Süresi**: 20 saniye
- **Hedef**: Kaplumbağayı mümkün olduğunca çok tıklayarak yüksek puan elde etmek
- **Kontrol**: Fare ile tıklama

## 🚀 Nasıl Çalıştırılır

### Gereksinimler
- Python 3.x
- `turtle` kütüphanesi (Python ile birlikte gelir)

### Kurulum ve Çalıştırma

1. Projeyi klonlayın veya indirin
2. Terminal/Komut İstemcisini açın
3. Proje dizinine gidin
4. Aşağıdaki komutu çalıştırın:

```bash
python main.py
```

## 🎯 Oyun Özellikleri

- **Skor Sistemi**: Her tıklamada 1 puan kazanırsınız
- **Zaman Sayacı**: 20 saniye süre sınırı
- **Rastgele Hareket**: Kaplumbağa her 750ms'de rastgele bir konuma hareket eder
- **Görsel Arayüz**: Renkli arka plan ve büyük kaplumbağa karakteri

## 🎨 Oyun Arayüzü

- **Arka Plan**: Açık mavi
- **Kaplumbağa**: Kırmızı renk, 2x büyütülmüş boyut
- **Skor Gösterimi**: Üst kısımda büyük font ile
- **Zaman Gösterimi**: Skorun altında kalan süre

## 🏆 Oyun Sonu

Oyun süresi dolduğunda:
- "Game Over" mesajı görüntülenir
- Final skorunuz gösterilir
- Oyun otomatik olarak kapanır

## 🛠️ Teknik Detaylar

- **Kullanılan Kütüphaneler**: `turtle`, `random`
- **Oyun Döngüsü**: Event-driven (olay tabanlı)
- **Zaman Yönetimi**: `ontimer` fonksiyonu ile
- **Koordinat Sistemi**: Turtle'ın kendi koordinat sistemi

## 📝 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

---

**İyi eğlenceler! 🐢✨** 