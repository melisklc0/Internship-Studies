# 1. Git Branch Nedir? Nasıl Çalışır? (Detaylı Anlatım + Örnekler)

## 📌 Branch (Dal) Nedir?

Git'te branch, projeyi ana koddaki akışı bozmadan geliştirmek için kullandığımız bir yöntemdir.  
Her branch aslında kodun ayrı bir kopyası gibi davranır.  
Ana kod (genelde `main` branch) üzerinde çalışmadan yeni bir özellik geliştirmek ya da hata gidermek için yeni bir branch açılır.

---

## 🔧 Neden Branch Kullanılır?

- Ana kodu (main) bozmadan çalışmak
- Yeni özellik geliştirmek
- Takım çalışmasında birbirinden bağımsız işler yapmak
- Kodları test ettikten sonra ana koda eklemek (merge)

---

## 🛠️ Temel Branch Komutları

### 🔍 Mevcut branch'leri listele
```bash
git branch
```
> Aktif branch'in yanında `*` işareti olur.

---

### ➕ Yeni bir branch oluştur
```bash
git branch feature/landing-page
```
> Sadece branch oluşturur, geçiş yapmaz.

---

### 🔁 Yeni branch'e geçmek
```bash
git switch feature/landing-page
```
> `checkout` yerine `switch` kullanımı önerilir (daha okunabilir ve net).

---

### 🏃‍♀️ Kısa yol: branch oluştur ve geç
```bash
git checkout -b feature/landing-page
```
> Hem branch oluşturur hem de o branch'e geçer.

---

### 🔄 Ana branch'e dönmek
```bash
git switch main
```

---

### 🔗 Branch'leri birleştirme (Merge)
```bash
git merge feature/landing-page
```
> Aktif olan branch'e, belirtilen branch'teki değişiklikleri birleştirir.

---

### ❌ Branch silmek
```bash
git branch -d feature/landing-page
```
> Merge edilmiş branch’i siler.  
Zorla silmek istersen `-D` kullanılır:
```bash
git branch -D feature/landing-page
```

---

## ⚠️ Merge Conflict Nedir? Ne Yapılır?

Aynı dosyada, aynı satırlarda iki branch farklı değişiklik yaptıysa, Git hangisini alacağını bilemez. Bu duruma `merge conflict` denir.

### Merge conflict olduğunda:
- Dosyada çatışan kısımlar `<<<<<<<`, `=======`, `>>>>>>>` işaretleri ile gösterilir.
- Manuel olarak düzenlenir.
- Ardından şu komutlar verilir:
```bash
git add .
git commit
```

---

## 📌 Pratik Branch Senaryosu

1. Ana koddayız (`main`):
```bash
git checkout main
```

2. Yeni branch açıp geçiyoruz:
```bash
git checkout -b feature/search-bar
```

3. Kodları yazıp commit ediyoruz:
```bash
git add .
git commit -m "feat: add search bar"
```

4. Ana branch’e dönüp merge ediyoruz:
```bash
git switch main
git merge feature/search-bar
```

5. Temizlik: branch’i siliyoruz:
```bash
git branch -d feature/search-bar
```

6. GitHub’a push ediyoruz:
```bash
git push origin main
```

---

## 📙 Branch İsimlendirme Önerileri

| Prefix      | Açıklama             | Örnek                  |
|-------------|----------------------|------------------------|
| `feature/`  | Yeni özellik         | `feature/profile-page` |
| `bugfix/`   | Hata düzeltme        | `bugfix/navbar-crash`  |
| `hotfix/`   | Acil düzeltme        | `hotfix/payment-error` |
| `test/`     | Test amaçlı deneme   | `test/theme-color`     |

---

## ✅ Branch Kullanırken Dikkat Edilecekler

- Ana koda (`main`) doğrudan müdahale etme.
- Merge işlemi öncesi ana branch'i güncelle (`git pull origin main`).
- Branch isimlerini anlamlı ve standartlara uygun belirle.
- Merge sonrası kullanılmayan branch’leri sil.
- Commit mesajlarını kısa ve açıklayıcı yaz (`feat:`, `fix:`, vs.).

---

## 🔚 Sonuç

Branch kullanımı Git’in en güçlü yönlerinden biri.  
Kodun güvenli, yönetilebilir ve işbirliğine açık şekilde geliştirilmesini sağlar.  
Her yeni özellik, her hata düzeltmesi, hatta her deneme için bir branch açmak, kod kalitesini ve düzenini ciddi şekilde artırır.





# 2. Git Commit Mesajları Nasıl Olmalı?

Commit mesajı, Git tarihçesindeki **en önemli dokümantasyon** aracıdır.  
Kod değişikliği kadar commit mesajı da ciddi bir iştir.

---

## 🧠 Neden Düzgün Commit Mesajı Yazmalıyım?

- Ekip üyeleri neyin neden değiştiğini, ne zaman değiştiğini anlar.
- Değişiklikleri git log ile hızlıca arayıp bulmak kolaylaşır.

---

## 📐 İdeal Commit Mesajı Yapısı

### 🔹 Basit Format (Bireysel projeler için):

```bash
git commit -m "özellik eklendi: kullanıcı girişi tamamlandı"
```

### 🔸 Gelişmiş Format (Takım çalışması/standart için):

```text
<tip>: <kısa açıklama>

[İsteğe bağlı detaylı açıklama paragrafı]

[İlgili ticket veya issue numarası]
```

---

## 📚 Kullanılan Tipler (Conventional Commits Standardına göre)

| Tip        | Açıklama                                  |
|------------|-------------------------------------------|
| `feat`     | Yeni özellik ekleme                       |
| `fix`      | Hata düzeltmesi                           |
| `refactor` | Refactoring (davranışı değiştirmeden kod düzenleme) |
| `docs`     | Sadece dökümantasyon değişikliği          |
| `style`    | Biçimsel düzenleme (indent, boşluk vs.)   |
| `test`     | Test dosyası ekleme/düzenleme             |
| `chore`    | Yapılandırma, bağımlılık, build vs. işleri |
| `perf`     | Performans iyileştirmeleri                |

---

## ✍️ Örnek Commit Mesajları

```bash
git commit -m "feat: kullanıcı giriş ekranı eklendi"
git commit -m "fix: şifre sıfırlamada oluşan null hatası düzeltildi"
git commit -m "docs: README dosyasına kullanım örneği eklendi"
git commit -m "style: kod biçimi ESLint kurallarına göre güncellendi"
git commit -m "refactor: login fonksiyonu sadeleştirildi"
git commit -m "chore: .gitignore güncellendi"
```

---

## 📏 Commit Mesajı Yazım Kuralları

- **İngilizce veya Türkçe** tercihinde tutarlı ol (karma yapma)
- Kısa ve net yaz, **ilk harfi küçük** harfle başla
- Nokta (.) kullanma (bir cümle değil, bir eylemdir)
- Bir işi bir commit'e sığdır (küçük commit > büyük commit)

---

## ⚠️ Kötü Commit Mesajı Örnekleri

```bash
git commit -m "güncellendi"
git commit -m "bug fix"
git commit -m "son hali"
git commit -m "test"
```

Bu mesajlar **anlamsız ve iz bırakmaz**. Geçmişe dönüp ne yapıldığını anlamak mümkün değildir.

---

## 💡 En İyi Uygulamalar

- Commit yapmadan önce: "Bu mesajı 3 ay sonra görsem ne anlardım?" diye düşün.
- Geliştirmenin sonunda değil, **her anlamlı değişiklikte commit yap**.
- `git log` çıktısının okunabilir olması için mesaj kalitesine dikkat et.
- Commit mesajı ile değişiklik birbiriyle **doğrudan ilişkili** olmalı.

---

## 🎁 Bonus: Git Commit Mesajı Template (VSCODE için)

`.git/.gitmessage.txt` dosyası oluştur:

```text
# tip: açıklama
#
# feat:     yeni özellik
# fix:      bug fix
# refactor: kod temizliği
# docs:     dokümantasyon
# chore:    yapılandırma
# style:    kod biçimi
# test:     testler
```

Ve Git'e şunu söyle:

```bash
git config --global commit.template ~/.git/.gitmessage.txt
```

---

## 📌 Sonuç

Commit mesajı yazmak zaman almaz ama seni ve takımı çok şeyden kurtarır.  
Kaliteli mesajlar, profesyonel Git kullanımının en temel göstergesidir.  
Kodu kadar mesajı da düzgün olan geliştirici bir adım öndedir. 🚀

> “Bir commit mesajı, kodun hikayesidir.”





# 3. Git Tag Nedir? Nasıl Kullanılır? (Detaylı Anlatım + Örnekler)

## 🔖 Git Tag Nedir?

`git tag`, bir Git deposundaki **belirli commit’leri etiketlemek (işaretlemek)** için kullanılır.

Genellikle:
- **Sürüm numaraları (v1.0, v2.1.3 gibi)** vermek için
- **Dağıtıma çıkılan versiyonları sabitlemek için**
- **Release sürecini takip etmek için** kullanılır.

---

## 🧠 Tag Türleri

### 1. Lightweight Tag (Hafif Etiket)

- Sadece commit hash'ine işaret eder.
- Ekstra bilgi (açıklama, tarih, imza vs.) içermez.

```bash
git tag v1.0.0
```

---

### 2. Annotated Tag (Açıklamalı Etiket)

- Kullanıcı, tarih, açıklama, GPG imzası gibi metadata içerir.
- Tercih edilen yöntemdir.

```bash
git tag -a v1.0.0 -m "İlk stabil sürüm"
```

---

## 📌 Mevcut Tag’leri Listelemek

```bash
git tag
```

> Tüm tag'leri sıralar.

---

## 🔍 Belirli bir pattern’e göre tag filtrelemek

```bash
git tag -l "v1.*"
```

> `v1.` ile başlayan tüm tag’leri listeler.

---

## 📍 Bir Tag’in Gösterilmesi

```bash
git show v1.0.0
```

> O tag’in işaret ettiği commit ve metadata bilgisi görüntülenir.

---

## 🕹️ Belirli Bir Commit'e Tag Eklemek

```bash
git tag -a v1.1.0 <commit-hash> -m "Yeni özellik eklendi"
```

> Önce `git log` ile commit hash’i bulup ekleyebilirsin.

---

## 🚀 Tag’leri Remote (GitHub gibi) Repolara Göndermek

### Tek bir tag’i göndermek:
```bash
git push origin v1.0.0
```

### Tüm tag’leri göndermek:
```bash
git push origin --tags
```

---

## ❌ Tag Silme

### Lokal tag silme:
```bash
git tag -d v1.0.0
```

### Remote tag silme:
```bash
git push origin --delete v1.0.0
```

---

## 🔄 Tag’li Commit’e Checkout (Geçiş)

Tag’e doğrudan geçmek için:
```bash
git checkout v1.0.0
```

> **Not**: Tag'e geçtiğinde “detached HEAD” modunda olursun, yani değişiklik yaparsan yeni bir branch açman gerekebilir.

---

## 📦 GitHub Üzerinde Tag Kullanımı (Release)

1. GitHub repo sayfasında "Releases" sekmesine git
2. `Draft new release` butonuna bas
3. Bir tag adı seç (örnek: `v1.2.0`)
4. Açıklama ekle
5. Yayınla

> Bu işlem, GitHub üzerinde release süreci başlatmak için kullanılır.

---

## 🛠️ Tag Kullanım Senaryosu

### Versiyonlama
```bash
git tag -a v2.0.0 -m "API yeniden yazıldı"
git push origin v2.0.0
```

### CI/CD Pipeline Tetikleme

- `v*` tag'leri geldiğinde otomatik olarak build/test/deploy işlemlerini tetiklemek.

---

## 🧪 Tag Örnekleri

| Tag        | Açıklama                          |
|------------|-----------------------------------|
| `v1.0.0`   | İlk kararlı sürüm                 |
| `v1.1.0`   | Yeni özellikler eklendi           |
| `v1.1.1`   | Küçük hata düzeltmeleri           |
| `v2.0.0`   | Büyük değişiklik, kırıcı sürüm     |
| `release-2025-06` | Haziran 2025 dağıtımı         |

---

## 📖 Semantik Versiyonlama (Semantic Versioning - SemVer)

Genel yapı: `MAJOR.MINOR.PATCH`

- `MAJOR`: Geriye dönük uyumsuz değişiklik
- `MINOR`: Yeni özellik (uyumlu)
- `PATCH`: Hata düzeltmesi

> Örnek: `v2.3.5`  
2 → MAJOR, 3 → MINOR, 5 → PATCH

---

## 🎯 Sonuç

`git tag`, projendeki önemli noktaları işaretlemek için çok kritik bir araçtır.  
Versiyonlama, dağıtım ve değişiklik takibi için **net, sistemli ve açıklamalı tag’ler** kullanmak uzun vadede çok işe yarar.

Kodun geçmişini güvenli ve anlamlı bir şekilde yönetmek için tag’leri alışkanlık haline getir! 🚀





# 4. GitHub Pull Request (PR) Nedir? Nasıl Oluşturulur? (Detaylı Anlatım + Örnekler)

## 🔍 Pull Request Nedir?

Pull Request (PR), GitHub üzerinde bir branch'te yaptığın değişiklikleri başka bir branch’e (genelde `main`) **birleştirmek için** gönderdiğin bir **istektir**.

Pull request, kodun:
- İncelenmesini sağlar (code review)
- Takım çalışmasını düzenler
- Otomatik testleri tetikler (CI/CD varsa)
- Doğrudan ana koda geçmesini engelleyerek güvenliği artırır

> Pull request **lokal Git** komutlarıyla yapılmaz, bu işlem **GitHub arayüzü üzerinden** gerçekleşir.

---

## ⚙️ Pull Request Süreci (Adım Adım)

### 1. Ana repoyu klonla (fork yapılmışsa önce forkla)
```bash
git clone https://github.com/kullaniciAdi/projeAdi.git
cd projeAdi
```

---

### 2. Yeni bir branch oluştur
```bash
git checkout -b feature/contact-form
```

---

### 3. Kodlarını yaz, değişiklikleri ekle ve commit et
```bash
git add .
git commit -m "feat: add responsive contact form"
```

---

### 4. Değişiklikleri kendi GitHub branch’ine gönder (push et)
```bash
git push origin feature/contact-form
```

---

### 5. GitHub’da Pull Request oluştur

GitHub’a gidip:
- Hangi branch’ten → hangi branch’e birleştirme yapılacak onu seç (örnek: `feature/contact-form` → `main`)
- Açıklayıcı bir başlık ve açıklama gir
- “Create pull request” butonuna tıkla

---

### 6. PR süreci

- Kod incelemesi yapılır (reviewers)
- Gerekirse değişiklik istenir
- Sonrasında `Merge` yapılır veya `Close` edilir (reddedilir)
- Merge sonrası branch silinebilir (otomatik veya manuel)

---

## 🛑 PR vs Push

| Özellik         | `git push`                          | Pull Request                       |
|------------------|--------------------------------------|-------------------------------------|
| Amaç             | Lokal değişikliği uzaktaki branch’e gönderir | Değişiklikleri başka branch’e birleştirme isteği |
| Nerede yapılır   | Terminal (Git)                      | GitHub arayüzünde                   |
| Otomatik test    | Genelde hayır                       | Genelde evet (CI/CD varsa)          |
| Kod incelemesi   | Yok                                 | Evet                                |

---

## 💡 Neden Pull Request Kullanılır?

- Takımda kodları doğrudan `main`’e merge etmek yerine kontrol etmek için
- Hatalı/eksik kodların erken fark edilmesi için
- Açıklayıcı commit geçmişi tutmak için
- CI/CD entegrasyonları için

---

## ✅ Pull Request En İyi Uygulamalar

- Branch isimlerini anlamlı tut (örnek: `feature/login-form`)
- Küçük, odaklı değişikliklerle PR oluştur
- Açıklayıcı başlık ve detaylı açıklama yaz
- Gerekirse ekran görüntüsü, video, test sonucu ekle
- “WIP” (work in progress) PR’ları `Draft` olarak aç

---

## 📌 Pull Request Oluşturma Örneği (Gerçek Senaryo)

1. `feature/navbar-fix` adlı branch’te menüyü düzelttin  
2. `git push origin feature/navbar-fix` ile GitHub’a gönderdin  
3. GitHub’da → `Compare & pull request` butonuna tıkladın  
4. Başlık: `fix: mobile navbar height bug`  
5. Açıklama:  
   ```
   Bu PR, mobil görünümde navbar'ın ekran dışında kalması sorununu çözüyor.
   - .navbar yüksekliği `100vh` yerine `auto` yapıldı
   - `overflow-y` kaldırıldı
   Test edildi: iPhone X, Android Pixel
   ```
6. Reviewer olarak takım arkadaşlarını seçtin  
7. Kodlar incelendi, testler geçti, merge edildi 🚀

---

## ⚠️ Pull Request ile İlgili Hatalar

- PR yapmadan önce `main` branch’ini güncellememek (`git pull origin main`)
- Çok fazla değişiklik içeren tek PR açmak
- Merge çatışmalarını çözmeden PR göndermek
- Aynı anda birden fazla işlevi tek PR’a koymak

---

## 🧠 Bonus: PR Açarken Kullanılan Etiketler

| Etiket    | Anlamı                                |
|-----------|----------------------------------------|
| `feat:`   | Yeni bir özellik                       |
| `fix:`    | Hata düzeltme                          |
| `docs:`   | Sadece dökümantasyon                   |
| `style:`  | Biçimlendirme (boşluk, virgül vs.)     |
| `refactor:` | Yeniden yapılandırma (davranış değişmez) |
| `test:`   | Test kodları                           |
| `chore:`  | Diğer bakım işleri (CI/CD, config vs.) |

---

## 🎯 Sonuç

Pull request, takım halinde çalışırken kaliteli ve güvenli kod akışını sağlamak için vazgeçilmezdir.  
Kodlar asla doğrudan `main`’e push edilmemeli, her zaman PR ile gönderilmelidir.  
Hem bireysel projelerde düzenli kalmanı sağlar, hem ekip içinde profesyonel süreçler oluşturur.





# 5. Git Kullanırken Karşılaşılabilecek Sorunlar ve Yapılmaması Gerekenler

Git güçlü ama dikkat ister. Yanlış bir komut, saatlerce emek verdiğin işi bozabilir.  
Bu notlar seni en yaygın hatalardan korur, iyi Git pratiği kazandırır. 👇

---

## 🚫 Git İle Çalışırken Yapılmaması Gereken Şeyler

### 1. `main` veya `master` branch’inde doğrudan çalışmak

- Ana branch’te çalışmak geri dönüşü zor hatalara yol açar.
- Bunun yerine her iş için ayrı bir **feature branch** oluştur.

✅ **Doğru kullanım:**
```bash
git checkout -b feature/login-page
```

---

### 2. Commit mesajlarını anlamsız yazmak

```bash
git commit -m "deneme"
git commit -m "asdfgh"
```

- Bu mesajlar geçmişte ne yaptığını anlamanı imkânsız hale getirir.
- Anlamlı, standart bir formatla yaz:

✅ **Doğru örnek:**
```bash
git commit -m "feat: kullanıcı giriş ekranı eklendi"
```

---

### 3. Commit yapmadan branch değiştirmek

Eğer commit ya da stash yapmadan başka branch’e geçersen, değişikliklerin **kaybolmaz ama çakışma yaratabilir**.

✅ Önce commit ya da stash et:
```bash
git stash
git checkout main
```

---

### 4. Merge veya Rebase işleminden önce pull yapmamak

- `main` branch’ten uzaklaştıysan, branch’ini merge etmeden önce mutlaka `git pull` ile güncelle.

```bash
git checkout main
git pull origin main
git merge feature/x
```

---

### 5. `force push` (`git push -f`) komutunu rastgele kullanmak

- `git push -f` HEAD geçmişini **geri döndürülemez şekilde** bozar.
- Özellikle ekip içinde çalışırken kesinlikle dikkatli olunmalı.

✅ Gerekli durumlar dışında kullanma. Kullanmadan önce:
```bash
git log --oneline
```
ile geçmişi kontrol et.

---

### 6. `.env`, `node_modules`, `venv`, `__pycache__` gibi dosyaları track etmek

- Bunlar projeye özel veya geçici dosyalardır.
- `.gitignore` içine eklenmeli.

✅ `.gitignore` örneği:
```
*.pyc
__pycache__/
node_modules/
.env
venv/
```

---

## 🔥 Git Kullanırken Karşına Çıkabilecek Yaygın Sorunlar

### 🧩 Merge Conflict (Çakışma)

İki kişi aynı satırı değiştirmişse çatışma olur.

📍 Çözüm:
- Git sana hangi dosyada çakışma olduğunu söyler
- Dosyayı aç ve şu şekilde işaretlenmiş yerleri temizle:

```text
<<<<<<< HEAD
bu satır local
=======
bu satır remote
>>>>>>> origin/main
```

🛠️ Temizle → Commit → Merge tamamlanır.

---

### 🚫 “Detached HEAD” Hatası

Tag veya commit hash ile `checkout` yaptıysan HEAD branch’te değildir.

📍 Geçici değişiklik yapacaksan sorun değil. Ama kalıcı çalışacaksan:
```bash
git checkout -b yeni-branch-adi
```

---

### ❌ “fatal: not a git repository”

Bu hata şu anki klasör bir Git deposu değilse çıkar.

📍 Çözüm:
```bash
git init
```
veya doğru klasöre geç:
```bash
cd path/to/repo
```

---

### ❌ “error: failed to push some refs to ...”

Genelde remote repo senin local’inden daha günceldir.

📍 Çözüm:
```bash
git pull --rebase origin main
git push origin main
```

---

### 🗑️ Yanlışlıkla Silinen Dosya veya Commit

📍 Son commit’i geri almak için:
```bash
git reset --soft HEAD~1
```

📍 Commit yapılmadan silinen dosya için:
```bash
git checkout -- silinen_dosya.py
```

---

## ✅ Git Kullanırken Uyman Gereken Kurallar

| Kural | Açıklama |
|------|----------|
| `Küçük commitler` | Her commit, tek bir işi yapsın |
| `Anlamlı commit mesajları` | Takip etmesi kolay olur |
| `Her iş için yeni branch` | Ayrı ayrı test etmesi kolay |
| `.gitignore` dosyasını düzgün kullan | Gereksiz dosyaları takip etme |
| `main`'i koru | Merge dışında değişiklik yapma |
| PR kullan | Direkt `push` yapma, gözden geçirme süreci oluştur |

---

## 🎯 Sonuç

Git güçlü ama disiplinsiz kullanıldığında çok tehlikeli olabilir.  
Bu notlar sayesinde:
- Hataları önceden tahmin eder
- Takım çalışmasında daha uyumlu olursun
- Kendi projende düzenli kalırsın

> "Her commit bir hikâye, her branch bir amaç taşır."



Sokratik yöntemi benimseyin: Doğrudan soru sormak yerine, modelin istenilen çıktıya yönelmesini sağlayacak şekilde promptlarınızı yönlendirici sorulara bölün.

Az örnekli öğrenmeden faydalanın: Asıl prompttan önce, istenen giriş-çıkış eşleşmelerine birkaç örnek verin. Bu, modelin anlayışını ve performansını önemli ölçüde artırabilir.

Yinelemeli yeniden yazım uygulayın: Modelin çıktısını yeni bir prompt olarak tekrar modele verin, böylece yanıtlarını adım adım geliştirip iyileştirmesine olanak tanıyın.

Prompt zincirleme kullanın: Karmaşık görevleri, her birinin çıktısı bir sonraki için giriş olacak şekilde daha küçük promptlara ayırarak çözümleyin.

Prompt zenginleştirmeyi keşfedin: Promptlarınıza ilgili arka plan bilgileri, kısıtlamalar ya da yapılmaması gereken örnekler gibi ek bağlamlar ekleyin.

Prompt toplulaştırmayı deneyin: Birden fazla promptun ya da modelin çıktısını birleştirerek daha sağlam ve çeşitli bir nihai çıktı oluşturun.

Prompt tabanlı ince ayar kullanın: Belirli görevler ya da alanlara özel olarak, dil modellerini az sayıda prompt ve istenen çıktı içeren bir veri kümesiyle ince ayarlayın.

Prompt tabanlı geri getirme dahil edin: Dış kaynaklardan ilgili bilgileri sorgulamak ve getirmek için promptları kullanarak modelin bilgisini artırın.

Prompt tabanlı çeviriyi keşfedin: Promptları farklı dillere ya da üsluba çevirerek yeni bakış açıları ya da yetenekler elde etmeyi deneyin.

Prompt tabanlı akıl yürütmeden faydalanın: Karmaşık görevleri çok adımlı mantıksal süreçlere bölen bir dizi prompt aracılığıyla modeli problem çözmeye yönlendirin.