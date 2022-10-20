# Binary convert to decimal
Convert biner number to decimal number with Python🐍

<hr>

binary to decimal conversion program with ``Python``, I made this for a computer system lesson in the number system section in my school <a href="https://dhikaweb7.github.io">SMK RADEN PAKU</a>

> Running in terminal (for Linux and Mac) or cmd (for Windows) 

> Indonesian language 🇮🇩

# Preview

![Screenshot_20220730-063742](https://user-images.githubusercontent.com/107765982/181860789-5a1ac69c-6e09-4f3c-b9c9-018ed4d74f2b.png)

Requirement

 - Python3
 - Colorama (Optional but my prefer about the colors😅)

```Python

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(Fore.BLUE+"=" * 26)
print(Fore.GREEN+"MERUBAH BINER KE DESIMAL >
print(Fore.BLUE+"=" * 26)
print(Fore.CYAN+"=" * 25)
print(Fore.RED+"SMK RADEN PAKU X TKJ 1 |")
print(Fore.CYAN+"=" * 25)
b_num = list(input("MASUKAN ANGKA BINER: "))
value = 0

for i in range(len(b_num)):
        digit = b_num.pop()
        if digit == '1':
                value = value + pow(2, i)
print("Hasil desimal adalah :", value)

```

# Install

Install Python3

```bash

apt-get-install Python3

```

Install Colorama

```bash

pip install colorama

```

Cloning repo 

```url

git clone https://github.com/Dhikaweb7/Biner-convert-to-decimal

```

<hr>


# Number of System

``BINARY``

``DECIMAL`` 

> ``HEXADECIMAL`` 

> ``OKTAL``
