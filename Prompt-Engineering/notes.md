# Prompt Engineering Guide

## 1. Giriş

### a. LLM Ayarları
---
**Temperature**: Rastlantısallığı arttırır. Yaratıcılık gerektiren şeylerde yüksek sıcaklık, daha somut şeylerde düşük sıcaklık tercih edilir.

**Top_p**: Belirleyiciliği kontrol eder. Kesin ve gerçek yanıtlar için düşük, daha çeşitli yanıtlar için yüksek tutulur.

### b. İstem Unsurları
---
**Talimat** - modelin gerçekleştirmesini istediğiniz belirli bir görev veya talimat

**Bağlam** - modeli daha iyi yanıtlara yönlendirebilecek dış bilgiler veya ek bağlam

**Giriş Verisi** - yanıtını bulmakla ilgilendiğimiz giriş veya soru

**Çıktı Göstergesi** - çıktının türü veya formatı.

### c. Genel İpuçları
---
Belirginlik, basitlik ve özlülük genellikle daha iyi sonuçlar verir.

Karmaşık görevlerimiz varsa bunu daha basit görevlere bölerek yaptırabiliriz.

"Yaz", "Sınıflandır", "Özetle", "Çevir", "Sırala" vb. gibi komutlar kullanabiliriz.

Yönergeleri ### gibi bir belirteçle ayırabiliriz.

İyi bir formata ve açıklayıcı bir isteme sahip olmak daha önemlidir. 

# 2. Talimatlar

## a. Sıfır Örnekli İstem
Herhangi bir örnek veya gösterim olmadan modelin bir yanıt vermesi için doğrudan istem yapılır.

*İstem:*
```bash
Metni tarafsız, olumsuz ya da olumlu olarak sınıflandırın. 
Metin: Tatilin normal olduğunu düşünüyorum.
Hissiyat: 
```
*Çıktı:*
```bash
Tarafsız
```

## b. Az Örnekli İstem
Görevleri bağlam içinde öğrenme yeteneği vardır. Daha iyi performans için modele yol gösterir.

*İstem:*
```bash
Bir "whatpu", Tanzanya'ya özgü küçük, tüylü bir hayvandır. "Whatpu" kelimesinin kullanıldığı örneğin bir cümlesi şudur:
Afrika'daki seyahatimiz sırasında bu çok şirin whatpu'ları gördük.
"Farduddle" yapmak, çok hızlı bir şekilde zıplamak anlamına gelir. "Farduddle" kelimesinin kullanıldığı bir cümlenin örneği şudur:
```
*Çıktı:*
```bash
Maçı kazandığımızda, hepsi sevinçle farduddle yapmaya başladık.
```

**Önemli Noktalar**:

Etiket boşluğu ve giriş metni arasındaki dağılım, etiketlerin doğruluğundan bağımsız olarak model performansını etkiler.

Etiketlerin formatı önemlidir.

Rastgele ve tutarlı olmayan etiketler versek bile gerçek etiket dağılımına benzemeleri modelin öğrenmesine yardımcı olur.

## c. Düşünce Zinciri (CoT) İstemleri
Sorunun çözümüne yönelik örneği akıl yürütme yöntemleriyle beraber verdiğimizde model de bu şekilde çözüyor.

*İstem:*
```bash
Bu gruptaki tek sayılar çift bir sayıya eşittir: 4, 8, 9, 15, 12, 2, 1.
A: Tüm tek sayıları (9, 15, 1) topladığımızda 25 bulunur. Cevap Yanlıştır.
Bu gruptaki tek sayılar çift bir sayıya eşittir: 15, 32, 5, 13, 82, 7, 1.
A:
```
*Çıktı:*
```bash
Tüm tek sayıları (15, 5, 13, 7, 1) topladığımızda 41 bulunur. Cevap Yanlıştır.
```
### Sıfır Örnek CoT İstemi
Hiç örnek vermeden direkt akıl yürütme ile soruyu çözdürmeye çalışıyoruz.

*İstem:*
```bash
Pazara gittim ve 10 elma aldım. 2 elmayı komşuya ve 2 elmayı tamirciye verdim. Sonra 5 elma daha aldım ve 1'ini yedim. Kaç elmayla kaldım?
Adım adım düşünelim.
```
*Çıktı:*
```bash
Öncelikle, 10 elma ile başladınız.
2 elmayı komşuya ve 2 elmayı tamirciye verdiniz, yani 6 elmanız kaldı.
Sonra 5 tane daha elma aldınız, yani şimdi 11 tane elmanız oldu.
Son olarak, 1 elma yediniz, bu durumda 10 elmanız kaldı.
```

### Otomatik Düşünceler Zinciri (Auto-CoT)
Adım adım düşünelim tekniğini geliştirmeyi amaçlıyor. 

Auto-CoT iki ana aşamadan oluşur:

**Aşama 1):** soru kümelemesi: veri setindeki soruları birkaç kümeye ayırır
**Aşama 2):** gösterim örneklendirmesi: her kümeden temsili bir soru seçer ve Zero-Shot-CoT ile basit sezgilere dayanarak akıl yürütme zinciri oluşturur


## d. Üretilmiş Bilgi Sistemleri
Modelin sadece bilgi kullanmasını değil, aynı zamanda önce bilgi üretip sonra tahmin yapmasını öneriyor. Yani modelin doğrudan cevaba atlamadan önce düşünmesini sağlıyor. Bu yöntem, özellikle ortak bilgi ve mantık gerektiren görevlerde kullanılıyor.

*İstem:*
```bash
Soru: Golfün bir parçası, diğerlerinden daha yüksek bir puan toplamayı denemektir. Evet mi Hayır mı?
Bilgi: Golfün amacı, bir set deliği en az sayıda vuruşla oynamaktır. Bir golf turu genellikle 18 delikten oluşur. Her delik, standart bir golf sahasındaki turda bir kez oynanır. Her vuruş bir puan olarak sayılır ve oyunun galibi, toplam vuruş sayısına göre belirlenir.
Açıklama ve Yanıt: 
```
*Çıktı:*
```bash
Hayır, golfün amacı diğerlerinden daha yüksek bir puan toplamayı denemek değildir. Asıl amaç, bir set deliği en az sayıda vuruşla oynamaktır. Oyunun galibi, toplam vuruş sayısına, total puan sayısına göre belirlenir.
```



*İstem:*
```bash

```
*Çıktı:*
```bash

```
