class konversi :
    def __init__ (self, rupiah, kurs_dollar) :
        self.rupiah = rupiah 
        self.dollar = 0
        self.kurs_dollar = kurs_dollar

    def rupiah_dollar (self) :
        self.dollar = self.rupiah / self.kurs_dollar
        
    def cetak (self) :
        print('hasil konversi rupiah ke dollar adalah :', self.dollar)
    
asu = konversi(10000, 15942)

asu.rupiah_dollar()

asu.cetak




