from osoba import Osoba

class Dieta (Osoba):
    def __init__ (self, meno, vek, skola):
        super(). __init__(meno, vek)
        self.skola = skola
    def predstav_sa (self):
        return f"Ahoj, volám sa {self.meno} a mám {self.vek} rokov a chodí, do {self.skola}." 
    