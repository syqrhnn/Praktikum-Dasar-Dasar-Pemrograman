#Amphibi 1

from Animal import Animal

class amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernafas ):
        super (). __init__ (name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernafas = bernafas
    
    def info_amphibi(self):
        super().info_animal ()
        print(f'jenis air \t\t\t :', self.jenis_air,
        '\nBernafas \t\t\t :', self.bernafas)

salamander = amphibi('Salamander', 'Cacing', 'Dua Alam', 'Bertelur', 'Air Tawar', 'Kulit dan Paru-Paru')
salamander.info_amphibi()

print('============================================================')

#Amphibi 2

from Animal import Animal

class amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernafas ):
        super (). __init__ (name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernafas = bernafas
    
    def info_amphibi(self):
        super().info_animal ()
        print(f'jenis air \t\t\t :', self.jenis_air,
        '\nBernafas \t\t\t :', self.bernafas)

axolotl = amphibi('Axolotl', 'Cacing', 'Air dan Darat', 'Bertelur', 'Air Tawar', 'Kulit Dan Paru-Paru')
axolotl.info_amphibi()

print('============================================================')

#Amphibi 3

from Animal import Animal

class amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernafas ):
        super (). __init__ (name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernafas = bernafas
    
    def info_amphibi(self):
        super().info_animal ()
        print(f'jenis air \t\t\t :', self.jenis_air,
        '\nBernafas \t\t\t :', self.bernafas)

katak = amphibi('Katak', 'Serangga', 'Dua Alam', 'Bertelur', 'Air Tawar', 'Kulit dan Paru-Paru')
katak.info_amphibi()

print('============================================================')

