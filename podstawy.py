#pętla powtarzająca czynność określoną ilość razy
for i in range(100000000000000):
    print(i)


def kop_diamenty(ilosc):
    for i in range(ilosc):
        print(f"Kopię diaksy, wykopałem {i+1} diament(-y/-ów).")

kop_diamenty(3)
print(f"##################")
####################
ilosc_diamentow = 6
####################
import time

def kop_diamenty_jesli_sa(ilosc):
    for i in range(ilosc):
        if (ilosc_diamentow >= i+1):
            print(f"Kopię diaksy, wykopałem {i+1} diament(-y/-ów).")
            time.sleep(1)
        else:
            print("Wykopałeś już wszystkie diamenty!")
            break

#Wykonywanie zdefiniowanych funkcji
kop_diamenty_jesli_sa(17)

#funkcja bardziej złożona
def kopanie(wybor, sztuk):
    match wybor:
        case 1:
            print(f"Kopię diaksy, wykopałem 1 diament.")
        case 2:
            print(f"Kopię diaksy, wykopałem {sztuk} diamenty.")
        case 3:
            print(f"Kopię diaksy, wykopałem {sztuk} diamentów.")

def kop_inteligentnie_diamenty_jesli_sa(ilosc):
    for i in range(ilosc):
        if (ilosc_diamentow >= i+1):
            if (i+1 == 1):
                kopanie(1, i+1)
            elif (i+1 <= 3):
                kopanie(2, i+1)
            else:
                kopanie(3, i+1)
            time.sleep(1)
        else:
            print("Wykopałeś już wszystkie diamenty!")
            break

kop_inteligentnie_diamenty_jesli_sa(9)

#########################################
#######Tworzenie własnej funkcji#########
#########################################

def policz_do_trzech():
    print('Raz, dwa, trzy!')

def obecny():
    print('Obecny!')

obecny()
policz_do_trzech()

def obecny_z_imieniem(imie):
    print(f'{imie} obecny!')

obecny_z_imieniem('Janek')






