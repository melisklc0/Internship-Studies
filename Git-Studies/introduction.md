## Git Bash Giriş

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

```bash
```

---

