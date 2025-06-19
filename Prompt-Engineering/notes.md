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

# 2. Teknikler

## a. Sıfır Örnekli İstem
Herhangi bir örnek veya gösterim olmadan modelin bir yanıt vermesi için doğrudan istem yapılır.

Örnek vermeden direkt prompt.

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

*İstem:*
```bash
Aşağıdaki metni üzgün, mutlu ya da tarafsız olarak sınıflandır.
Metin: Yağmurdan dolayı pikniğe gidemedik.
Hissiyat:
```
*Çıktı:*
```bash
Üzgün
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

*İstem:*
```bash
"xmxmx" kelimesi dondurma anlamına gelir.Bu kelimenin kullanıldığı örnek bi cümle: Hava çok sıcak olduğu için xmxmx yedim.
"xaxaxa" etmek, yavaş bir şekilde dans etmek anlamına gelir. Bu kelimenin kullanıldığı örnek bi cümle:
```
*Çıktı:*
```bash
Düğünde yaşlı çiftler müziğin ritmine uyarak xaxaxa ediyorlardı.
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

## e. Prompt Chaining
Karmaşık bir görev daha basit görevlere bölünür. Bir basit görevin çıktısı diğer basit görevin istemi için kullanılarak bir zincir şeklinde devam eder.

*İstem:*
```bash
Verilen slayt içerisindeki ana konu başlıklarını listele.
```
*Çıktı:*
```bash
1. Giriş
2. Yapay Zeka Tarihçesi
3. Makine Öğrenmesi Temelleri
4. Derin Öğrenme ve Uygulamaları
5. Gelecek Trendleri
```
Buradan aldığımız çıktıyı bir sonraki prompt için kullanalım:

*İstem:*
```bash
Bu listedeki konular için birer açıklama yaz.
```
*Çıktı:*
```bash
1. Yapay zeka nedir ve neden önemlidir?
2. Yapay zekanın tarihsel gelişim süreci nasıl olmuştur?
3. Makine öğrenmesi nasıl çalışır?
4. Derin öğrenmenin temel özellikleri nelerdir?
5. Yapay zeka alanında gelecekte hangi trendler beklenmektedir?
```
Yine buradan aldığımız çıktıyı bir sonraki prompt için kullanalım:

*İstem:*
```bash
Bu açıklamalara göre her konu başlığı için bir sınav sorusu oluştur.
```
*Çıktı:*
```bash
1. Yapay zeka nedir ve neden önemlidir?
2. Yapay zekanın tarihsel gelişim süreci nasıl olmuştur?
3. Makine öğrenmesi nasıl çalışır?
4. Derin öğrenmenin temel özellikleri nelerdir?
5. Yapay zeka alanında gelecekte hangi trendler beklenmektedir?
```

## f. Düşünce Ağacı (ToT)
Problemi çözmek için adımları dallandırarak farklı düşünceler üzerinden en iyi sonuca ulaşmaya çalşıyor. 

*İstem:*
```bash
Bu soruyu cevaplandıran üç farklı uzmanı hayal edin.
Tüm uzmanlar düşünmelerinin 1 adımını yazar,
sonra bunu grupla paylaşır.
Sonra tüm uzmanlar bir sonraki adıma geçer, vb.
Eğer herhangi bir uzman herhangi bir noktada hatalı olduğunu fark ederse, o kişi ayrılır.
Soru şu...
```

*İstem:*
```bash

```
*Çıktı:*
```bash

```