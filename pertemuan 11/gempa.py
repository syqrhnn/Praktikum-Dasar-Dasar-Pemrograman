class Gempa:

    def __init__(self, skala, lokasi):  
        self.skala = skala 
        self.lokasi = lokasi

    def dampak(self):
        
        print(f"gempa berlokasi di {self.lokasi}")
        print(f"skala dari gempa ini adalah : {self.skala} Skala Richter")
        if self.skala < 2:
            print("Dampak gempa tidak berasa")
        elif self.skala > 2 and self.skala <= 4:
            print("Dampak gempa bangunan retak-retak")
        elif self.skala > 4 and self.skala <= 6:
            print("Dampak gempa bangunan roboh")
        elif self.skala > 6:
            print("Dampak gempa bangunan roboh dan berpotensi tsunami")
        else :
            print("Dampak gempa tidak diketahui")




