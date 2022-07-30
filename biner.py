import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(Fore.BLUE+"=" * 26)
print(Fore.GREEN+"MERUBAH BINER KE DESIMAL")
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
