# Huawei Ai Kurs Notları

# Ai Overview

Symbolism:   
Connectionism: Simple processing yerine nöronlar kullanılmalı.  
Behaviorism: Çevreyle etkileşim yaptıkça ai kendini geliştirebilir.

**Strong AI:** Bu görüş gerçek problemi çözebilen makineler olabilir der, self aware ve zeki modeller.  
**Weak AI**: Zeki görünürler ama aslında gerçek problemleri çözemezler. Self awareness yoktur.

**4 element:** data, algorithm, computing power, scenario.  
Bunlar için de ai ile cloud computing, big data, IoT gibi konuları birleştirmeliyiz.

Genel olarak AI teknolojileri:
- Computer vision
- Speech processing
- Natural language processing (NLP)

Bazı kullanım alanları: medikal, retail(market), autonomous driving vs.

**Full Stack:**  
ModelArts workflow, Mindspore (ai computing network), CANN (chip operator library), Da vinci core mimarisi (+ ARM CPU), 

**Endişeler:**  
Privacy issues: Verilerin nerden geldiği ile ilgili gizlilik endişeleri  
Fake images: Görüntülerin gerçek mi fake mi olduğunu anlayamamak  
İşsizlik: Bazı işler ai tarafından devralınabilir  

**Yazılım trendleri:**   
- Frameworks: MindSpore, Tensorflow, Pytorch  
Akademik çalışmalarda pytorch daha çok öne çıkarken, endüstride tensorflow taşıma kolaylığı ile daha çok ön plana çıkmış.  
- Computer vision: GAN algoritması görüntü üretme   
- NLP field: transformer mimarisi  
-Reinforcement learning field: Alphastar etc.

> By "all AI scenarios", Huawei means different deployment scenarios for AI, including public clouds, private clouds, edge computing in all forms, industrial IoT devices, and consumer devices.


# Machine Learning Overview

Coverage rate: kurallar gerçek dünya verilerine her zaman uyumlu olmayabilir, how much data do the rules can fit?

**Rule-based method:** elimizde değişen bi veriseti varsa kurallar da buna göre sürekli değişmelidir, bu da çok karmaşık olabilir.  
**Machine learning:** model, verisetini öğrenerek karar verme mekanizmasını, yani kuralları kendi kendine öğrenir.

Kompleks ya da açıklanamayan kurallar, değişen senaryolar, değişen veriler vs. gibi durumlarda makine öğrenmesi tercih edilir.

Fonksiyonun bir ideal mapping function u olmalıdır. source domain X ile target domain Y yi eşler.
Objective function (f): Bu fonksiyon öğrenilir, direkt olarak elde edilemez. 

Başka bir (g) fonksiyonu tanımlayarak f i olabildiğince tahmin etmeye çalışabiliriz. Bu fonksiyon f'e yaklaşan bir tahmini fonksiyondur.

## Görevler:

**Classification:** Algoritma genel olarak bi f fonksiyonundan sınıflara çıktı veren bir fonksiyondur.  f: R^n -> (1,2,..,k)

**Regression:** Model, veriye göre bir çıktı tahmin etmeye çalışır. Algoritması genel olarak bir çıktı fonksiyonu verir. f: R^n -> R   
Örn. sigorta ücretini tahmin etmeye çalışan bir model. 

**Clustering:** Etiketsiz, büyük bir verisetindeki verileri, içerisindeki benzerliğe göre birçok gruba böler. Aynı kategorideki veriler birbirine daha çok benzer. Örn. image retrieval, user profile management.

Tahmin etme problemleri için %80-%90 olarak classification ve regression kullanılır.

## Çeşitleri

**Supervised learning:** Labeled data. Tangible(elle tutulur, somut) ve intangible(soyut) objeleri sınıfandırmada kullanılır. Obje hakkında bilgi vermeden. 

Product recommendatitons, segment customers based on customer data, diognose a disease etc.

**Unsupervised learning:** Unlabeled data. Makineyi büyük değişken verilere maruz bırakılır. Clustering sıklıkla kullanılır.

**Semi-supervised learning:** Küçük miktarda labeled verinin doğrudan öğrenilmesine yardımcı olmak için büyük miktarda unlabeled veri kullanır. Sınıf videolarından öğrencilerin öğrenme şeklini anlamak vb.

**Reinforcement learning:** Algoritmayı ödül ve ceza yöntemine göre eğitir. Agent, çevresi ile etkileşime girer, doğru ise ödül, yanlış ise ceza verilir.

