#Mamalia 1

from Animal import Animal

class mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, kulit, golongan_darah):
        super (). __init__(name, makanan, hidup, berkembang_biak)
        self.kulit = kulit
        self.golongan_darah = golongan_darah

    def info_mamalia(self):
        super(). info_animal ()
        print(f'Kulit  \t\t\t\t :', self.kulit, 
        '\nGolongan Darah \t\t\t :', self.golongan_darah)

kucing = mamalia('Kucing', 'Ikan Asin', 'Darat', 'Melahirkan','Berbulu', 'Berdarah Panas')
kucing.info_mamalia()

print('============================================================')

#Mamalia 2

from Animal import Animal

class mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, kulit, golongan_darah):
        super (). __init__(name, makanan, hidup, berkembang_biak)
        self.kulit = kulit
        self.golongan_darah = golongan_darah

    def info_mamalia(self):
        super(). info_animal ()
        print(f'Kulit  \t\t\t\t :', self.kulit, 
        '\nGolongan Darah \t\t\t :', self.golongan_darah)

sapi = mamalia('Sapi', 'Rumput', 'Darat', 'Melahirkan', 'Berbulu', 'Berdarah Panas')
sapi.info_mamalia()

print('============================================================')

#Mamalia 3

from Animal import Animal

class mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, kulit, golongan_darah):
        super (). __init__(name, makanan, hidup, berkembang_biak)
        self.kulit = kulit
        self.golongan_darah = golongan_darah

    def info_mamalia(self):
        super(). info_animal ()
        print(f'Kulit  \t\t\t\t :', self.kulit, 
        '\nGolongan Darah \t\t\t :', self.golongan_darah)

lumba_lumba = mamalia('Lumba-Lumba', 'Ikan Haring, Ikan Spart, Ikan Tenggiri', 'Laut', 'Melahirkan','Halus Dan Kenyal', 'Berdarah Panas')
lumba_lumba.info_mamalia()

print('============================================================')