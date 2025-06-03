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


## 4. Branch Kullanımı
---

