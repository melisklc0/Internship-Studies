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
├── requirements.txt     # Bağımlılık (dependency) listesi
├── pyproject.toml       # Modern yapılandırma dosyası 
├── setup.py             # Paketleme için kullanılır
└── README.md            # Proje açıklaması
```

---

## 2. Virtual Environment

Her proje kendi bağımlılıklarıyla izole çalışsın diye kullanılır. Bu sayede farklı projelerde farklı versiyonlardaki kütüphaneler çakışmadan çalışabilir.

Burada manuel olarak oluşturalım. Öncelikle bir sanal ortam .venv oluşturdum.
```bash
python -m venv .venv
```

Sonrasında bunu aktive etmemiz gerekiyor.
```bash
.venv\Scripts\activate
```

Sanal ortam içerisinde istediğimiz gibi dependency ekleyebiliriz. Bu dependency yalnızca bu ortam için geçerli olur.
```bash
pip install requests
```

requirements.txt ile ortamın kopyasını oluşturabiliriz. Projedeki tüm bağımlılıkları export yani dışa aktaralım:
```bash
pip freeze > requirements.txt
```

Daha öncesinde bağımlılıkları yazmış olduğumuz bir requirements.txt dosyasından kurulum yapabiliriz.
```bash
pip install -r requirements.txt
```

Sanal ortamdan çıkış yapacağımız zaman da bu komutu kullanmalıyız.
```bash
deactivate
```

## 3. Python Paket Yapısı

Eğer projeyi bir *pip install edilebilir paket* haline getireceksek:

İlk olarak bir setup.py ayarlamalıyız. İlk olarak bir setup.py ayarlamalıyız. Bu dosya sayesinde proje bir Python paketi haline gelir ve pip ile kurulabilir olur.
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

Kurulumu da gayet basit bi şekilde yapılıyor.
```bash
pip install .
```

Projeyi paketleyip dağıtmak istersek, örneğin PyPI’ye yüklemek için *setup.py* dosyası gereklidir. Projenin yeniden kullanılabilir olmasını sağlar. Başkalarının projeyi yükleyip kullanmasını kolaylaştırır.

---

## 4. Poetry Kullanma

Python 3.8+ ile birlikte gelen *pyproject.toml*, bağımlılıkları ve yapılandırmayı merkezi olarak kontrol etmemizi sağlar. *poetry* veya *pdm* gibi araçlarla kullanılır.

### poetry ile proje başlatmak:
Öncelikle poetry install ettim, ve yeni bir proje oluşturdum.
```bash
pip install poetry
poetry new poetry-project
```
Oluşturulan projede bir src klasörü, tests klasörü, README.md ve bir *pyproject.toml* dosyası var. pyproject.toml dosyası içerisinde bazı versiyon bilgileri var. 
```bash
[project]
name = "poetry-project"
version = "0.1.0"
description = ""
authors = [
    {name = "melisklc0",email = "klmelis@hotmail.com"}
]
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
]

[tool.poetry]
packages = [{include = "poetry_project", from = "src"}]


[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```
Sonrasında,
```bash
poetry add requests
```
komutu ile gerekli request leri indirdim. Projeye tekrar baktığımda artık gerekli versiyon dependency olarak eklenmiş oldu.

```bash
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "requests (>=2.32.3,<3.0.0)"
]
```

Eklemiş olduğum bu dependency leri kullanabilmek için tekrar install yaptım.
```bash
poetry install
```

Bu bana bir *poetry.lock* dosyası oluşturdu. Böylece bütün eklediğim dependencies projeye sabitlenmiş oldu. Daha sonrasında projeyi çalıştırmam gerektiğinde bir virtual environment oluşturdum. 
```bash
poetry env activate
```

Bu env içerisinde pytest de eklemek istedim. Yapmak istediğimiz testleri `tests/` klasörüne yazarak, `pytest` ile çalıştırabiliriz. Her fonksiyon başında da yine test_ eklememiz gerekiyor.
```bash
poetry add pytest --group dev
```

*pyproject.toml* dosyasına tekrar baktığımda artık bunu da bir depency olarak eklemiş oldum.
```bash
[tool.poetry.group.dev.dependencies]
pytest = "^8.3.5"
```

Bu request leri kaldırmak istediğimizde de bu komutu kullanabiliriz:
```bash
poetry remove requests
```

Projeyi yayımlamak için bu komutları kullanabiliriz:
```bash
poetry build
poetry publish
```

Var olan env listesine bakalım:
```bash
poetry env list
poetry-project-ogCdDx9I-py3.13 (Activated)
```

Artık kullanmadığımda yer kaplamaması için env i siliyorum:
```bash
poetry env remove poetry-project-ogCdDx9I-py3.13
```

---

## 5. Python UV Kullanma
Yukarıdaki yöntemleri kullanmak da uygundur, fakat UV; pip, virtualenv, pip-tools, pipenv, poetry gibi araçların yerini çok daha hızlı ve modern şekilde almayı hedefleyen bir araçtır.

Öncelikle uv install ettim.
```bash
pip install uv
```
### Script ile UV
Yeni bir *uv-project* projesi oluşturdum. Bu projenin içerisine *main.py* dosyası açtım. Bu dosya ile öncelikle şuanki python versiyonunun *3.13.3* olduğunu öğrendim.
```bash
import sys
print(sys.version)
```

Tekrar terminale geldim. İndirebileceğim python versiyonlarına baktım:
```bash
uv python list
```

Özel bir versiyon indirelim. UV pip'ten çok daha hızlı bir şekilde indirdi.
```bash
uv python install 3.8
```

Projeyi default ile de çalıştırabiliriz, özel bir versiyonla da çalıştırabiliriz.
```bash
uv run main.py
uv run --python 3.8 main.py
```

Dependency i script üzerinde de ekleyebiliriz. *main.py* içerisine *rich* import ettim. Rich desteklemeyen bir versiyonla çalıştırmak istediğimde hata alacağım. Bunu direkt script üzerinde dahil edebiliriz:
```bash
uv run --with rich --python 3.8 main.py
```

Ama sürekli bu şekilde tek tek eklememize gerek yok. Bunun için init kullanabiliriz.
```bash
uv init --script main.py --python 3.8
```

Bu komut, *main.py* içerisine bir dependency script ekledi.
```bash
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///

import sys
from rich import print
print(sys.version)
```

Buraya kullanmak istediğimiz tam versiyonu, gerekli dependency leri yazabilirim. Bu ekleme işlemini terminal üzerinden de yapabilirim.
```bash
uv add --script main.py "rich"
```
Kendisi eklemiş oldu:
```bash
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "rich",
# ]
# ///
```

### Projeler için UV
Şimdi biraz da uv'yi projeler için nasıl kullanabileceğimize bakalım. Yeni bir *uv-project2* projesi oluşturdum.
```bash
uv init
```

Bu şekilde projeyi kendisi hazırlıyor. Bir *.python-version*, *main.py*, README.md ve bir *pyproject.toml* dosyası oluşturdu. Bu *pyproject.toml* dosyası içerisinde gerekli dependency ve versiyon listeleri bulunuyor:
```bash
[project]
name = "uv-project2"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = []
```

Şimdi bazı dependencies ekleyelim. Bunu default da yapabiliriz, özel olarak da ekleyebiliriz:
```bash
uv add requests
uv add requests==2.32.3
```

Dosya da güncellendi:
```bash
dependencies = [
    "requests>=2.32.3",
]
```

Bir dependency kaldırmak için:
```bash
uv run main.py
uv run --python 3.8 main.py
```

Bunu yaptığımızda uv kendisi bir *.venv* ekledi. Bir dependency değişikliği yaptığımızda virtual enviroment kendisi güncellenecek. Ayrıca bir *uv.lock* da ekledi. Bu dosyada tam versiyonları depolar. 

```bash
uv remove requests
```

Eğer versiyon uyuşmayan bir dependency eklemek istersem bana hata verecektir. Bunu düzeltmek için *pyproject.toml* ve *.python-version* dosyaları üzerinde python versiyonumu biraz daha düşürmem ve uygun versiyona güncellemem gerekiyor.

Şimdi dependency olarak eklemediğimiz bir kütüphane, örneğin pygame import edelim.
```bash
uv run main.py
ModuleNotFoundError: No module named 'pygame'
```

Burada hata alacağız. pygame'i dependency listesine ekleyelim.
```bash
dependencies = [
    "requests>=2.32.3",
    "pygame"
]
```
Şimdi tekrar run yaptığımızda, uv pygame i kendisi install etti ve projeyi çalıştırdı.
```bash
Installed 1 package in 464ms
pygame 2.6.1 (SDL 2.28.4, Python 3.10.17)
Hello from the pygame community. https://www.pygame.org/contribute.html
Hello from uv-project2!
```

Son olarak yapılan değişiklikleri ve tüm projeyi senkronize ettim.
```bash
uv sync
```

---

## 6. .gitignore Dosyası

Buraya git tarafından takip edilmesini istemediğimiz dosyaları belirtiyoruz.
Bu sayede sanal ortam klasörleri, derlenmiş dosyalar, geçici dosyalar, kişisel yapılandırma dosyaları gibi dosyalar Git'e eklenmez.

Örnek bir *.gitignore* dosyası:
```bash
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
.env/

# Distribution / packaging
build/
dist/
*.egg-info/

# VSCode, PyCharm gibi IDE dosyaları
.vscode/
.idea/

# Log dosyaları
*.log

# Ortam değişkenleri
.env

# Jupyter notebook checkpoint'leri
.ipynb_checkpoints/

```

---

