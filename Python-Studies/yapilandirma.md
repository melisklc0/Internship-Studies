# Python Projelerinde Yapılandırmalar

## 1. Python Projesi Nasıl Yapılandırılır?

```
my_project/
│
├── .venv/               # Sanal ortam (genelde `.gitignore`'a eklenir)
├── my_project/          # Asıl Python modülleri burada
│   ├── __init__.py
│   └── main.py
│
├── tests/               # Test dosyaları burada yer alır
│   └── test_main.py
│
├── requirements.txt     # Bağımlılık listesi (pip ile yüklenir)
├── pyproject.toml       # Modern yapılandırma dosyası (opsiyonel ama önerilir)
├── setup.py             # Paketleme için kullanılır (opsiyonel)
└── README.md            # Proje açıklaması
```

---

## 2. Virtual Environment (venv)

Her proje kendi bağımlılıklarıyla izole çalışsın diye kullanılır.

### Öncelikle bi venv oluşturdum.
```bash
python -m venv .venv
```

### Sonrasında bunu aktive etmemiz gerekiyor.
```bash
.venv\Scripts\activate
```
Çıktı:
```bash
(base) C:\Users\melis>.venv\Scripts\activate

(.venv) (base) C:\Users\melis>
```

### Çıkış yapacağımız zaman da bu komutu kullanmalıyız.
```bash
deactivate
```
Çıktı:
```bash
(.venv) (base) C:\Users\melis>deactivate

(base) C:\Users\melis>
```

---

## 3. pip ve requirements.txt

### pip ile kurulum yapabiliriz.
```bash
pip install requests
```
Çıktı:
```bash
(base) C:\Users\melis>pip install requests
Requirement already satisfied: requests in d:\anaconda3\lib\site-packages (2.32.2)
Requirement already satisfied: charset-normalizer<4,>=2 in d:\anaconda3\lib\site-packages (from requests) (2.0.4)
Requirement already satisfied: idna<4,>=2.5 in d:\anaconda3\lib\site-packages (from requests) (3.7)
Requirement already satisfied: urllib3<3,>=1.21.1 in d:\anaconda3\lib\site-packages (from requests) (2.2.2)
Requirement already satisfied: certifi>=2017.4.17 in d:\anaconda3\lib\site-packages (from requests) (2024.12.14)

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip
```

### Projedeki tüm bağımlılıkları export yani dışa aktarmak için şu komutu kullanırız.
```bash
pip freeze > requirements.txt
```

### Daha öncesinde bağımlılıkları yazmış olduğumuz bir requirements.txt dosyasından kurulum yapabiliriz.
```bash
pip install -r requirements.txt
```

---

## 4. pyproject.toml Kullanma

Python 3.8+ ile birlikte gelen *pyproject.toml*, bağımlılıkları ve yapılandırmayı merkezi olarak kontrol etmemizi sağlar. *poetry* veya *pdm* gibi araçlarla kullanılır.

### poetry ile proje başlatmak:
```bash
pip install poetry
poetry init
poetry add requests
poetry install
```
Install ettikten sonraki çıktı bizi bu şekilde bi yapılandırmaya yönlendiriyor:
```bash
Package name [melis]:  poetry add requests
Version [0.1.0]:  poetry install
Description []:  
Author [melisklc0 <klmelis@hotmail.com>, n to skip]:  Melis
License []:
Compatible Python versions [>=3.12]:

Would you like to define your main dependencies interactively? (yes/no) [yes]
```
---

## 5. Python Paket Yapısı

Eğer projeyi bir *pip install edilebilir paket* haline getireceksek:

### İlk olarak bir setup.py ayarlamalıyız.
```python
from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "numpy"
    ]
)
```

### Kurulumu da gayet basit bi şekilde yapılıyor.
```bash
pip install .
```

---

## 6. tests Klasörü ve pytest

Testleri `tests/` klasörüne yazarak, `pytest` ile çalıştırabiliriz. Her fonksiyon başında da yine test_ eklememiz gerekiyor.
```bash
pip install pytest
pytest tests/
```

---

## 7. .gitignore Dosyası

Buraya git tarafından kontrol edilmesini istemediğimiz dosyaları belirtiyoruz.
Örnek bir dosya:
```bash
__pycache__/
.venv/
*.pyc
.env
```

---

## 8. Paket Yayımlamak, PyPI

Dosyaları paket haline getirip yayımlamak için ilk olarak elimizde *setup.py*, *pyproject.toml* ve *README.md* hazır olmalı.
Sonrasında *python -m build* komutu ile paket oluşturuyoruz ve *twine* ile yüklüyoruz:
```bash
pip install twine
twine upload dist/*
```

---
Bunu VSCode üzerinde yapmak istediğimiz zaman da şu yolu izliyoruz:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
code .
```

---

