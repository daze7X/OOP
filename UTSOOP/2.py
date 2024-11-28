class Mahasiswa:
    def __init__(self, nama, nim, program_studi):
        self.nama = nama
        self.nim = nim
        self.program_studi = program_studi

# Input dari pengguna
nama = input("Masukkan nama mahasiswa: ")
nim = input("Masukkan NIM mahasiswa: ")
program_studi = input("Masukkan program studi mahasiswa: ")

# Membuat objek mahasiswa
mahasiswa1 = Mahasiswa(nama, nim, program_studi)

# Menampilkan informasi mahasiswa
print("\nInformasi Mahasiswa:")
print(f"Nama: {mahasiswa1.nama}")
print(f"NIM: {mahasiswa1.nim}")
print(f"Program Studi: {mahasiswa1.program_studi}")
