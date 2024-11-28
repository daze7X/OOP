class Laptop:
    def __init__(self, merk, ram, processor):
        # Constructor untuk menginisialisasi atribut
        self.merk = merk
        self.ram = ram
        self.processor = processor
        print(f"Objek Laptop {self.merk} dengan RAM {self.ram}GB dan processor {self.processor} telah dibuat.")

    def __del__(self):
        # Destructor yang dijalankan saat objek dihancurkan
        print(f"Objek Laptop {self.merk} telah dihancurkan.")

# Pembuatan objek Laptop
laptop1 = Laptop("Asus", 8, "Intel i7")

# Menghapus objek secara eksplisit untuk melihat destructor berfungsi
del laptop1
