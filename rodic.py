from osoba import Osoba

class Rodic(Osoba):
    def __init__ (self,meno,vek,povolanie):
        super().__init__(meno,vek)
        self.povolanie = povolanie
    
    def predstav_sa(self):
        return f"Ahoj, volám sa {self.meno} a mám {self.vek} rokov a chodí, do {self.povolanie}."