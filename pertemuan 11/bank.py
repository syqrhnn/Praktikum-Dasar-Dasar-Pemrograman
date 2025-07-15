class Bank: 
    norek = ""
    nama = ""
    saldo = 0
    JmlNasabah = 0
    BANK = "Bank Syariah Nurul Fikri"
    def __init__(self, no, nasabah, saldo):
        self.norek = no
        self.nama = nasabah
        self.saldo = saldo
        Bank.JmlNasabah += 1

    def nabung(self, uang):
        self.saldo += uang

    def tarik(self, uang):
        self.saldo -= uang

    def cetak(self):
        
        print(Bank.BANK,
              "\n===========================",
              "\nNo. Rekening\t:", self.norek,
              "\nNama Nasabah\t:", self.nama,
              "\nSaldo\t\t: Rp ", format(self.saldo, ','),
              "\n--------------------------------------------"
              )
        
Gopal = Bank("123456", "Gopal", 5000000)
Ucok = Bank("123457", "Ucok", 7000000)
Jamal = Bank("123458", "Jamal", 8000000)
Asep = Bank("123459", "Asep", 11000000)

Gopal.nabung(2000000)
Ucok.nabung(1000000)
Jamal.tarik(2000000)
Asep.tarik(6000000)
print(Bank.BANK,
      "\n===========================")
Gopal.cetak()
Ucok.cetak()
Jamal.cetak()
Asep.cetak()
print("Jumlah Nasabah: %i orang" %Bank.JmlNasabah)
