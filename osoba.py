class Osoba:
    def __init__(self, meno, vek):
        self.meno = meno
        self.vek = vek        
    def predstav_sa(self):
        return f"Ahoj, volám sa {self.meno} a mám {self.vek} rokov."