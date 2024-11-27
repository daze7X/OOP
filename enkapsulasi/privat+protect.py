class Kendaraan:
    def __init__(self, var1, var2):
        self.__variabel_privat = var1      # Atribut privat
        self._variabel_proteksi = var2     # Atribut proteksi

    def tampilkan_nilai(self):
        print(f"Variabel Privat: {self.__variabel_privat}")
        print(f"Variabel Proteksi: {self._variabel_proteksi}")


class Bajaj(Kendaraan):
    def akses_proteksi(self):
        # Bisa mengakses _variabel_proteksi karena ini adalah kelas turunan
        print(f"Mengakses Variabel Proteksi: {self._variabel_proteksi}")
        # Tidak bisa mengakses __variabel_privat secara langsung di sini


# Penggunaan
obj = Kendaraan(10, 20)
obj.tampilkan_nilai()

obj_turunan = Bajaj(30, 40)
obj_turunan.akses_proteksi()
