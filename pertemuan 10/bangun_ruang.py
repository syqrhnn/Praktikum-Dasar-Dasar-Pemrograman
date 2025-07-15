import math

# Fungsi untuk menghitung luas permukaan kubus
def luas_kubus(sisi):
    luas =  6 * sisi ** 2
    print(f'luas kubus {sisi} * {sisi} = {luas}')

# Fungsi untuk menghitung luas permukaan balok
def luas_balok(panjang, lebar, tinggi):
    luas =  2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    print(f'luas balok {2} * ({panjang} * {lebar} + {panjang} * {tinggi} + {lebar} * {tinggi}) = {luas}')

# Fungsi untuk menghitung luas permukaan kerucut
def luas_kerucut(jari_jari, tinggi):
    s = math.sqrt(jari_jari ** 2 + tinggi ** 2)  
    luas =  math.pi * jari_jari * (jari_jari + s)
    print(f'luas kerucut {math.pi} * {jari_jari} * ({jari_jari} + {s}) = {luas}')

# Fungsi untuk menghitung luas permukaan bola
def luas_bola(jari_jari):
    luas = 4 * math.pi * jari_jari ** 2
    print(f'luas bola {4} * {math.pi} * {jari_jari} * {jari_jari} = {luas}')
