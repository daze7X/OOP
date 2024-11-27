class KendaraanProteksi:
    def __init__(self, var2):
        self._variabel_proteksi = var2  # Atribut protected

    def tampilkan_proteksi(self):
        print(f"Variabel Proteksi: {self._variabel_proteksi}")


class Bajaj(KendaraanProteksi):
    def akses_proteksi(self):
        print(f"Mengakses Variabel Proteksi di kelas turunan: {self._variabel_proteksi}")


# Penggunaan
obj_proteksi = KendaraanProteksi(20)
obj_proteksi.tampilkan_proteksi()  # Output: Variabel Proteksi: 20

# Mengakses langsung (meskipun tidak disarankan)
print(obj_proteksi._variabel_proteksi)  # Output: 20

# Mengakses dari kelas turunan
obj_turunan = Bajaj(40)
obj_turunan.akses_proteksi()  # Output: Mengakses Variabel Proteksi di kelas turunan: 40
