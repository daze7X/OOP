class KendaraanPrivat:
    def __init__(self, var1):
        self.__variabel_privat = var1  # Atribut privat

    def tampilkan_privat(self):
        print(f"Variabel Privat: {self.__variabel_privat}")


# Penggunaan
obj_privat = KendaraanPrivat(10)
obj_privat.tampilkan_privat()  # Output: Variabel Privat: 10

# Mencoba mengakses atribut privat langsung
try:
    print(obj_privat.__variabel_privat)  # Akan error
except AttributeError:
    print("Tidak bisa mengakses __variabel_privat secara langsung!")
