#Karnivora 1

from Animal import Animal

class Karnivora(Animal):  
    def __init__(self, name, makanan, hidup, berkembang_biak, cara_berburu_mangsa, gigi):  
        super().__init__(name, makanan, hidup, berkembang_biak)  
        self.cara_berburu_mangsa = cara_berburu_mangsa
        self.gigi = gigi

    def info_karnivora(self):
        super().info_animal()  
        print(f'Cara berburu mangsa  \t\t :', self.cara_berburu_mangsa,
              '\nGigi \t\t\t\t :', self.gigi)

singa = Karnivora('Singa', 'Daging', 'Darat', 'Melahirkan', 'Terkam Dan Menggigit', 'Memiliki Gigi Taring')
singa.info_karnivora()

print('============================================================')

#Karnivora 2

from Animal import Animal

class Karnivora(Animal):  
    def __init__(self, name, makanan, hidup, berkembang_biak, cara_berburu_mangsa, paruh):  
        super().__init__(name, makanan, hidup, berkembang_biak)  
        self.cara_berburu_mangsa = cara_berburu_mangsa
        self.paruh = paruh

    def info_karnivora(self):
        super().info_animal()  
        print(f'Cara berburu mangsa  \t\t :', self.cara_berburu_mangsa,
              '\nParuh \t\t\t\t :', self.paruh)

elang = Karnivora('Elang', 'Daging', 'Darat dan udara', 'Bertelur', 'Terkam Dengan Cakar', 'Memiliki Paruh Setajam Silet')
elang.info_karnivora()

print('============================================================')

#Karnivora 3

from Animal import Animal

class Karnivora(Animal):  
    def __init__(self, name, makanan, hidup, berkembang_biak, cara_berburu_mangsa, gigi):  
        super().__init__(name, makanan, hidup, berkembang_biak)  
        self.cara_berburu_mangsa = cara_berburu_mangsa
        self.gigi = gigi

    def info_karnivora(self):
        super().info_animal()  
        print(f'Cara berburu mangsa  \t\t :', self.cara_berburu_mangsa,
              '\nGigi \t\t\t\t :', self.gigi)

hiu = Karnivora('Ikan Hiu', 'Daging', 'Air Laut', 'Melahirkan', 'Menggunakan Garis Literalnya Untuk Mendeteksi Gerakan Mangsa', 'Memiliki Gigi Taring')
hiu.info_karnivora()

print('============================================================')