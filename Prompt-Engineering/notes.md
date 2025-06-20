# Prompt Engineering Guide

# Giriş

### LLM Ayarları
---
**Temperature**: Rastlantısallığı arttırır. Yaratıcılık gerektiren şeylerde yüksek sıcaklık, daha somut şeylerde düşük sıcaklık tercih edilir.

**Top_p**: Belirleyiciliği kontrol eder. Kesin ve gerçek yanıtlar için düşük, daha çeşitli yanıtlar için yüksek tutulur.

### İstem Unsurları
---
**Talimat** - modelin gerçekleştirmesini istediğiniz belirli bir görev veya talimat

**Bağlam** - modeli daha iyi yanıtlara yönlendirebilecek dış bilgiler veya ek bağlam

**Giriş Verisi** - yanıtını bulmakla ilgilendiğimiz giriş veya soru

**Çıktı Göstergesi** - çıktının türü veya formatı.

### Genel İpuçları
---
Belirginlik, basitlik ve özlülük genellikle daha iyi sonuçlar verir.

Karmaşık görevlerimiz varsa bunu daha basit görevlere bölerek yaptırabiliriz.

"Yaz", "Sınıflandır", "Özetle", "Çevir", "Sırala" vb. gibi komutlar kullanabiliriz.

Yönergeleri ### gibi bir belirteçle ayırabiliriz.

İyi bir formata ve açıklayıcı bir isteme sahip olmak daha önemlidir. 

# Teknikler

## 1. Sıfır Örnekli İstem
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

## 2. Az Örnekli İstem
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

## 3. Düşünce Zinciri (CoT) İstemleri
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
----
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
----
### Otomatik Düşünceler Zinciri (Auto-CoT)
Adım adım düşünelim tekniğini geliştirmeyi amaçlıyor. 

Auto-CoT iki ana aşamadan oluşur:

**Aşama 1):** soru kümelemesi: veri setindeki soruları birkaç kümeye ayırır
**Aşama 2):** gösterim örneklendirmesi: her kümeden temsili bir soru seçer ve Zero-Shot-CoT ile basit sezgilere dayanarak akıl yürütme zinciri oluşturur


## 4. Üretilmiş Bilgi Sistemleri
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

## 5. Prompt Chaining
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

## 6. Düşünce Ağacı (ToT)
Problemi çözmek için adımları dallandırarak farklı düşünceler üzerinden en iyi sonuca ulaşmaya çalşıyor. 

*İstem:*
```bash
Aşağıdaki problemi çözmek için üç farklı düşünce yolu oluştur.
Her düşünce yolu çözüm için farklı bir yaklaşım önersin.
Her adımı açıkla. En sonunda en mantıklı yolu seç ve sonucu belirt.

Soru: Bir tren saatte 60 km hızla 3 saat boyunca yol alıyor. Toplam kaç kilometre gitmiştir?
```

*İstem:*
```bash
Bu soruyu çözmek için üç farklı uzman düşünce yolunu yazacak.
Her uzman adım adım ilerleyecek.
Her adımda eğer hatalı olduğunu fark eden uzman süreci bırakacak.
En sonunda kalan uzmanlar doğru sonuca ulaşacak.

Soru: Eğer tüm A’lar B ise, ve tüm B’ler C ise, tüm A’lar C midir?
```
Tarzında promptlar yazılabilir.

## 7. LLM Yardımcı Teknikler
### Veri Alımı Artırılmış Üretim (RAG)
RAG yöntemi, dil modellerine Wikipedia gibi harici kaynaklardan bilgi getirerek bağlam sağlar, böylece modeli yeniden eğitmeye gerek kalmadan güncel ve güvenilir çıktılar üretir. 

Halüsinasyon sorununu hafifletmeye yardımcı olur. Halüsinasyon sorunu, yapay zeka modellerinin gerçekte olmayan veya yanlış bilgiler uydurmasıdır.

----

### Otomatik Akıl Yürütme ve Araç Kullanımı (ART)
ART, dil modelinin yeni bir görevi çözerken örneklerden öğrenmesini ve gerektiğinde hesap makinesi gibi dış araçları kullanmasını sağlar. Araç kullanırken durur, sonucu alır ve sonra devam eder. Ayrıca kolayca yeni araçlar ekleyebilir ya da hataları düzeltebiliriz.

----

### Otomatik İstem Mühendisi (APE)
APE, yapay zekanın kendi başına daha iyi talimatlar (promptlar) yazmasını sağlayan bir sistemdir.

Önce yapay zekaya bazı örnekler veriliyor, o da bunlara bakarak farklı görevleri nasıl çözebileceğini anlatan talimatlar üretiyor. Sonra bu talimatlar deneniyor ve en iyi sonuç veren seçiliyor.

Bu sistem, insanların yazdığı "Adım adım düşünelim" gibi klasik ifadelerden daha başarılı talimatlar bulabiliyor. Mesela “Doğru cevabı bulduğumuzdan emin olmak için bunu adım adım çözelim” gibi bir cümle, zor matematik sorularında yapay zekanın daha iyi düşünmesine yardımcı oluyor.

## 8. Program Destekli Dil Modelleri (PAL)
Bu yöntem, çözümü Python yorumlayıcısı gibi programlamaya dayalı bir çalışma zamanına devreder.

LangChain ve OpenAI GPT-3 kullanarak, Python yorumlayıcısı ile tarihsel soruları anlayıp yanıtlayabilen basit bir uygulama geliştirelim. Amaç, LLM’nin tarih içeren soruları analiz edip doğru cevabı üretmesini sağlamaktır.

Gerekli importları yapalım.
```bash
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
```
Gerekli yapılandırmaları yapalım. API key .env dosyasında olacak.
```bash
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
```
Soru ve promptun kurulumunu yapalım:
```bash
question = "Bugün 27 Şubat 2023. Tam 25 yıl önce doğmuştum. Doğduğum tarih MM/DD/YYYY formatında neydi?"
```

```bash
DATE_UNDERSTANDING_PROMPT = """
# S: 2015 yılına 36 saat kaldı. Bir hafta sonra günün tarihi MM/DD/YYYY formatında ne olacak?
# Eğer 2015 yılına 36 saat kaldıysa, bugün 36 saat öncesidir.
today = datetime(2015, 1, 1) - relativedelta(hours=36)
# Bir hafta sonrası,
one_week_from_today = today + relativedelta(weeks=1)
# Cevap %m/%d/%Y formatında
one_week_from_today.strftime('%m/%d/%Y')
# S: 2019'un ilk günü bir Salı’dır ve bugün 2019'un ilk Pazartesi'si. Bugünün tarihi MM/DD/YYYY formatında ne?
# Eğer 2019’un ilk günü bir Salı ve bugün 2019’un ilk Pazartesi’si ise, bu, bugünün 6 gün sonrası olduğu anlamına gelir.
today = datetime(2019, 1, 1) + relativedelta(days=6)
# Cevap %m/%d/%Y formatında
today.strftime('%m/%d/%Y')
# S: Konser 06/01/1943'te olması planlanıyordu, ancak bugüne bir gün ertelendi. 10 gün önceki tarih MM/DD/YYYY formatında neydi?
# Eğer konser 06/01/1943’te olması planlanıyor ama bir günlük gecikmeyle bugüne denk geldiyse, o zaman bugün bir gün sonrasıdır.
today = datetime(1943, 6, 1) + relativedelta(days=1)
# 10 gün önce,
ten_days_ago = today - relativedelta(days=10)
# Cevap %m/%d/%Y formatında
ten_days_ago.strftime('%m/%d/%Y')
# S: Bugün 4/19/1969. 24 saat sonra tarih MM/DD/YYYY formatında ne olacak?
# Bugün 4/19/1969.
today = datetime(1969, 4, 19)
# 24 saat sonra,
later = today + relativedelta(hours=24)
# Cevap %m/%d/%Y formatında
today.strftime('%m/%d/%Y')
# S: Jane bugünün 3/11/2002 olduğunu düşündü, ancak bugün aslında 12 Mart, yani 1 gün sonrası. 24 saat sonrası tarih MM/DD/YYYY formatında ne olacak?
# Eğer Jane bugünün 3/11/2002 olduğunu düşündü, ancak bugün aslında 12 Mart ise, o zaman bugün 3/12/2002’dir.
today = datetime(2002, 3, 12)
# 24 saat sonra,
later = today + relativedelta(hours=24)
# Cevap %m/%d/%Y formatında
later.strftime('%m/%d/%Y')
# S: Jane, 2001'in Şubat ayının son gününde doğdu. Bugün onun 16. yaş günü. Dünkünün tarihi MM/DD/YYYY formatında neydi?
# Eğer Jane 2001'in Şubat ayının son gününde doğdu ve bugün onun 16. yaşı ise, o zaman bugün 16 yıl sonrasıdır.
today = datetime(2001, 2, 28) + relativedelta(years=16)
# Dün,
yesterday = today - relativedelta(days=1)
# Cevap %m/%d/%Y formatında
yesterday.strftime('%m/%d/%Y')
# S: {question}
""".format(question=question)
```

Modeli çağıralım:
```bash
llm_out = llm.invoke(DATE_UNDERSTANDING_PROMPT)

print("Model cevabı:")
print(llm_out.content)
```

Burada model kendisi bir kod çıktısı verecektir.
```bash
# S: Bugün 27 Şubat 2023. Tam 25 yıl önce doğmuştum. Doğduğum tarih MM/DD/YYYY formatında neydi?
today = datetime(2023, 2, 27)
born = today - relativedelta(years=25)
born.strftime('%m/%d/%Y')
```
Bu çıktıyı çalıştırmak için de python exec kullanırız.
```bash
exec(llm_out.content)
print("Doğum tarihi:", born.strftime('%m/%d/%Y'))
```

## 9. ReAct 

*İstem:*
```bash

```
*Çıktı:*
```bash

```