from abc import ABC, abstractmethod

# Membuat kelas abstrak
class Kendaraan(ABC):
    @abstractmethod
    def bergerak(self):
        pass  # Metode abstrak (harus diimplementasikan oleh subclass)

# Kelas Turunan
class Mobil(Kendaraan):
    def bergerak(self):
        return "Mobil berjalan di jalan raya."

class Pesawat(Kendaraan):
    def bergerak(self):
        return "Pesawat terbang di udara."

# Penggunaan
mobil = Mobil()
pesawat = Pesawat()

print(mobil.bergerak())  # Output: Mobil berjalan di jalan raya.
print(pesawat.bergerak())  # Output: Pesawat terbang di udara.
