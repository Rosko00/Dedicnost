from osoba import Osoba
from dieta import Dieta
from rodic import Rodic

def main():
    osoba = Osoba ("Marián", 43)
    dieta = Dieta ("Hanka", 6, "Základná škola mládežnícka")
    rodic = Rodic ("Anna", 73, "Dôchodca")
    
    print (osoba.predstav_sa()) 
    print (dieta.predstav_sa())
    print (rodic.predstav_sa())
    
if __name__ == "__main__":
    main()
