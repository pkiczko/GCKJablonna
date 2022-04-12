#pętla powtarzająca czynność określoną ilość razy
for i in range(10):
    print(i)

def kop_diamenty(ilosc):
    for i in range(ilosc):
        print(f"Kopię diaksy, wykopałem {i+1} diament(-y/-ów).")

kop_diamenty(3)
print(f"##################")
##################
ilosc_diamentow = 6
import time

def kop_diamenty_jesli_sa(ilosc):
    for i in range(ilosc):
        if (ilosc_diamentow >= i+1):
            print(f"Kopię diaksy, wykopałem {i+1} diament(-y/-ów).")
            time.sleep(1)
        else:
            print("Wykopałeś już wszystkie diamenty!")
            break
kop_diamenty_jesli_sa(17)



