class AkunBank:
    def __init__(self, nomor_rekening, saldo):
        self.nomor_rekening = nomor_rekening
        self.__saldo = saldo

    # Getter untuk saldo
    def get_saldo(self):
        return self.__saldo

    # Setter untuk saldo
    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("Saldo tidak bisa negatif!")

# Pembuatan objek AkunBank
akun = AkunBank("123456789", 1000)

# Menggunakan getter dan setter
print("Saldo awal:", akun.get_saldo())
akun.set_saldo(1500)  # Update saldo
print("Saldo setelah diupdate:", akun.get_saldo())
