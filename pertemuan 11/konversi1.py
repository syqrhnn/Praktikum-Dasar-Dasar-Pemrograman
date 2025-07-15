class Konversi:
    def __init__(self, rupiah, kurs_dollar):
        self.rupiah = rupiah
        self.kurs_dollar = kurs_dollar
        self.dollar = 0 

    def rupiah_ke_dollar(self):
        self.dollar = self.rupiah / self.kurs_dollar  

    def cetak(self):
        print('Hasil konversi rupiah ke dollar adalah:', self.dollar)

asu = Konversi(22320000, 15942) 

asu.rupiah_ke_dollar()

asu.cetak()