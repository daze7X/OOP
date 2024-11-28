class Hewan:
    def suara(self):
        return "Hewan mengeluarkan suara"

class Kucing(Hewan):
    def suara(self):
        return "Meong"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk"

# Contoh pemanggilan
print(Hewan().suara())   # Hewan mengeluarkan suara
print(Kucing().suara())  # Meong
print(Anjing().suara())  # Guk guk
