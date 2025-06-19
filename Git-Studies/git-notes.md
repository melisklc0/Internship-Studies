# Git Önemli Konular

## 1. Git Reposu Oluşturma ve İlk Commit
Git kullanarak bir klasörde nasıl yeni bir depo oluşturduğumu ve içerisine nasıl dosya eklediğimi adım adım anlattım.


Öncelikle git bash üzerinde repo açmak istediğim klasöre geliyorum.
```bash
$ cd D:/Üniversite/Internship-Studies
```

Sonrasında doğru dizinde olduğumdan emin oldum.
```bash
$ pwd
/d/Üniversite/Internship-Studies
```

Dizini bir repo haline getirdim.
```bash
$ git init
Initialized empty Git repository in D:/Üniversite/Internship-Studies/.git/
```

Git çalışmaları yapacağım dizini takip edilmesi için ekledim.
```bash
$ git add Git-Studies
```

Son durumu kontrol edelim.
```bash
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   Git-Studies/test.txt
        new file:   Git-Studies/test2.txt
        new file:   Git-Studies/test3.txt
```
Detaylı bir mesaj ile commit yaptım.
```bash 
$ git commit -m "feat: add Git-Studies klasörü

Git-Studies klasörü içinde test.txt, test2.txt ve test3.txt
dosyaları eklendi. İlk testler için örnek içeriklerle hazırlandı."

[main (root-commit) 04dd738] feat: add Git-Studies klasörü
 3 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 Git-Studies/test.txt
 create mode 100644 Git-Studies/test2.txt
 create mode 100644 Git-Studies/test3.txt
```

Commit geçmişini de görüntüleyebiliriz.
```bash
$ git log
commit 04dd738543a574314a0573c0e9921c10018abc8f (HEAD -> main)
Author: melisklc0 <klmelis@hotmail.com>
Date:   Fri May 30 18:06:49 2025 +0300

    feat: add Git-Studies klasörü

    Git-Studies klasörü içinde test.txt, test2.txt ve test3.txt
    dosyaları eklendi. İlk testler için örnek içeriklerle hazırlandı.
```

## 2. Dosya Takibi ve Geri Alma İşlemleri
Yapılan değişiklikleri de görebiliriz.
```bash
$ git diff
diff --git a/Git-Studies/test.txt b/Git-Studies/test.txt
index e69de29..6184aa7 100644
--- a/Git-Studies/test.txt
+++ b/Git-Studies/test.txt
@@ -0,0 +1 @@
+açıklama: test1 dosyasıdır
```
Tekrardan add yaparak bu dosyayı geçici alana aldım. Artık diff yaptığımda değişiklik görünmüyor.

Dosyada yapılan değişikleri geri alabiliriz.
```bash
$ git restore test.txt
```

Dosyayı geçici alana eklediysem ve bunu geri almak istiyorsam şu komutu kullanıyoruz:
```bash
$ git reset
Unstaged changes after reset:
M       Git-Studies/test.txt
M       Git-Studies/test2.txt
```

Tekrar duruma bakalım:
```bash
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   test.txt
        modified:   test2.txt
```

## 3. Uzak Depo ile Senkronizasyon
Uzaktaki dosyaları yerel depoya çekmek için fetch kullanalım. Bu, güncellemeleri getiriyor ama henüz çalışma alanına yansıtmıyor.
```bash
$ git fetch
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (4/4), 1.01 KiB | 114.00 KiB/s, done.
From https://github.com/melisklc0/Internship-Studies
   b403b98..6a0f66e  main       -> origin/main 
```

Aradaki farka bakalım. Bu komut ile main (yerel depomda) olmayıp, origin/main (uzaktaki depo)'da olan değişiklikleri görürüz. 
```bash
$ git diff main..origin/main
diff --git a/Git-Studies/test3.txt b/Git-Studies/test3.txt
index e69de29..1263233 100644
--- a/Git-Studies/test3.txt
+++ b/Git-Studies/test3.txt
@@ -0,0 +1 @@
+test3 dosyasıdır.^M
```

Bu değişiklikleri çalışma ortamına yansıtalım.
```bash
$ git merge
Updating b403b98..6a0f66e
Fast-forward
 Git-Studies/test3.txt | 1 +   
 1 file changed, 1 insertion(+)
```

Diyelim ki uzak depoda güncellemeler oldu ve ben de yerelde güncelleme yaptım. Bunu push yapmaya çalıştığımda bir hata mesajı alırım:
```bash
$ git push
To https://github.com/melisklc0/Internship-Studies.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/melisklc0/Internship-Studies.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

Değişikleri almak için fetch + merge yapmadan direkt pull yaparsam, git kendisi bir merge işlemi başlatacaktır. Bir commit mesajı yazarak merge işlemini gerçekleştirdim.
```bash
Merge branch 'main' of https://github.com/melisklc0/Internship-Studies
# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.
~
~
~
~
~
~
~
~
~
~
.git/MERGE_MSG[RO] [unix] (17:22 02/06/2025) 
```
Sonrasında tekrar push ile değişiklerimi github'a gönderiyorum.

---

## 4. Branch Kullanımı

Ana koddan bağımsız çalışmamızı sağlar. Böylece projeyi geliştirirken oluşabilecek hatalar ana projeyi etkilemez. Yaptığımız değişiklikler kararlı hale geldikten sonra da ana kodla birleştirilip özellik güvenli bir şekilde eklenmiş olur. 

Eğer yaptığımız değişikliklerde bir hata çıkarsa da branch'i silerek ana koda hiç dokunmamışım gibi geri dönebiliyoruz. Böylece ana kod her zaman stabil ve güvenilir kalıyor.

Öncelikle hangi branch'ta olduğumuza bakalım:
```bash
$ git branch
* main
```

Branch değiştirmek için switch kullanabiliriz. Ancak henüz bir branch oluşturmadığım için switch yaparken yeni bir branch oluşturuyorum:
```bash
$ git switch -c feature/login-system
Switched to a new branch 'feature/login-system'
```
Branch isimlendirmeleri aşağıdaki gibi belirli kurallara göre yapılır:
| Prefix      | Açıklama             | Örnek                  |
|-------------|----------------------|------------------------|
| `feature/`  | Yeni özellik         | `feature/profile-page` |
| `bugfix/`   | Hata düzeltme        | `bugfix/navbar-crash`  |
| `hotfix/`   | Acil düzeltme        | `hotfix/payment-error` |
| `test/`     | Test amaçlı deneme   | `test/theme-color`     |


Branch'ı oluşturduktan sonra login işlemleriyle ilgili yapacağım eklemeleri yapıyorum ve değişiklikleri kaydediyorum.
```bash
$ git add login-system.txt
$ git commit -m "Added example file for notes"
```

Bu değişiklikleri uzak depodaki yeni branch'a gönderiyorum.
```bash
$ git push -u origin feature/login-system
```

Eğer yeni eklediğim kod test edilip kararlı hale getirildiyse ana kodla birleştirme yapmam gerekiyor. Bunun için öncelikle ana brancha geçiyorum.
```bash
$ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

Yeni yaptığım değişiklikler burada görünmeyecek. Ana kodda güncel olup olmadığını kontrol etmek için pull yapıyorum.
```bash
$ git pull origin main
From https://github.com/melisklc0/Internship-Studies
 * branch            main       -> FETCH_HEAD
Already up to date.
```

Eğer ana kod güncel ise birleştirme işlemini yapabilirim.
```bash
$ git merge feature/login-system
Updating 331859e..6899906
Fast-forward
 Git-Studies/login-system.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 Git-Studies/login-system.txt
```

Sonrasında da push ile uzak depoya yolladım.
```bash
$ git push
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/melisklc0/Internship-Studies.git
   331859e..6899906  main -> main
```
Birleştirme yapabilmemiz için ana kodun güncel olması gereklidir. Eski bir versiyona merge işlemi yapmak sistemde çakışmalara neden olabilir.



## 5. Commit Yönetimi

Örnek bir sunum belgesi oluşturup commitleyelim.
```bash
$ git add ornek-sunum.pptx
$ git commit -m "Added presentation"
```

Ancak commit mesajını değiştirmek istiyorum.
```bash
$ git commit --amend
```
Açılan ekranda düzenlemelerimi yaparak sonrasında ESC ile komut moduna geçiyorum. *wq* ile çıkış yapıyorum.
```bash
Added presentation

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# Date:      Tue Jun 3 09:44:58 2025 +0300
#
# On branch main
# Your branch is ahead of 'origin/main' by 1 commit.
#   (use "git push" to publish your local commits)
#
# Changes to be committed:
#       new file:   ornek-sunum.pptx
```

Başka bir commit'e geçmek istediğimizde commitin ID'sini kullanabiliriz. Öncelikle log'u kontrol edelim:
```bash
$ git log --oneline
dae3603 (HEAD -> main) Added presentation file
6899906 (origin/main, origin/feature/login-system, origin/HEAD, feature/login-system) Added example file for notes
331859e Updated Github-Studies titles
70a1375 Added new titles and notes
4cffaf1 Merge
e417730 Update test1
```

Buradan ihtiyacım olan ID'yi alarak o commit'e dönebilirim.
```bash
$ git checkout 70a1375
Note: switching to '70a1375'.
```

Ana koda geri dönelim ve sonrasında commitleri github'a gönderelim.
```bash
$ git checkout main
Previous HEAD position was 70a1375 Added new titles and notes
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

Son commiti silmek istersek:
```bash
$ git reset --soft HEAD~1
```
Duruma bakalım, burada gördüğümüz gibi commiti geri aldık. Bu değişiklikler geçici alanda kalır ve tekrar commit edilmeyi bekler.
```bash
$ git status
On branch main
Your branch is behind 'origin/main' by 3 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   ornek-sunum.pptx
```

Değişikliği tekrar commit edip devam edelim. Diyelim ki commit ettiğim dosyanın adını değiştirmeyi unuttum. Bunun için yeni bir commit oluşturmak yerine önceki commiti silip değişiklikleri çalışma alanına alalım. 
```bash
$ git reset --mixed HEAD~1
Unstaged changes after reset:
M       Git-Studies/git-notes.md
M       Git-Studies/ornek-sunum.pptx

$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   git-notes.md
        modified:   ornek-sunum.pptx
```

Dosyanın adını düzelttikten sonra tekrar commit ediyorum. Eğer commiti tamamen silmek istersem:
```bash
$ git reset --hard HEAD~1
```

Ancak bu yöntem riskli bir yöntemdir. Çünkü geri alınamaz. Bunun yerine silmek istediğimiz commitin ID'sini kullanarak revert edebiliriz.
```bash
$ git log --oneline
d28dfe6 (HEAD -> main, origin/main, origin/HEAD) Added ornek sunum
2db7d1e Updated login system
0a3d567 Merge
80d4550 Added example text


```
Revert işlemi commiti geri almak için yeni bir commit oluşturuyor. Log'dan gerekli ID'yi alalım.
```bash
$ git log --oneline
5f7956b (HEAD -> main, origin/main, origin/HEAD) Added notes for title 4 and 5
4992e32 Added presentation file again
d28dfe6 Added ornek sunum
2db7d1e Updated login system
```

Revert yapalım ve sonrasında push yapalım.
```bash
$ git revert 4992e32
$ git push
```

Burada gördüğümüz gibi revert işlemi için yeni bir commit eklenmiş oldu.
```bash
$ git log --oneline
1fcea90 (HEAD -> main) Revert: Added presentation file again
5f7956b (origin/main, origin/HEAD) Added notes for title 4 and 5
4992e32 Added presentation file again
```
---

## 6. Fork ve Pull Request Süreci

```bash

```

```bash

```






---

