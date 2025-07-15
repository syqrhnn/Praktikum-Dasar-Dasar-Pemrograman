import math

def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'luas persegi {sisi} * {sisi} = {luas}')   
    print(f'keliling persegi {sisi} * {sisi} * {sisi} * {sisi} = {keliling}')   

def l_persegi_panjang (panjang, lebar):
    luas = panjang * lebar 
    keliling = 2 * panjang * lebar
    print(f'luas persegi panjang adalah {panjang} * {lebar} = {luas}')
    print(f'keliling persegi panjang adalah {2} * {panjang} * {lebar} = {keliling}')


def l_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    print(f'luas segitiga dari', 0.5, "*", alas, "*", tinggi, "=",luas)


def l_lingkaran(r1,r2):
    luas = 3.14 * r1 * r2
    print(f'luas lingkaran', 3.14, "*", r1, "*", r2, "*" "=",luas)

def l_jajar_genjang(alas, tinggi):
    luas = alas * tinggi
    keliling =  2 * (alas + tinggi)
    print(f'luas jajar_genjang adalah', alas, "*", tinggi, "=", luas)
    print(f'keliling jajar genjang {2} * ({alas} + {tinggi}) = {keliling}')

def l_belah_ketupat(d1, d2):
    luas = 0.5 * d1 * d2
    keliling = 2 * d1 + 2 * d2
    print(f'luas belah ketupat', 0.5, "*", d1, "*", d2, "=",luas)
    print(f'keliling belah ketupat {2} * {d1} + {2} * {d2} = {keliling}')

def l_trapesium(alas, tinggi):
    luas = 0.5 * alas * tinggi
    keliling = 2 * alas + 2 * tinggi
    print(f'luas trapesium', 0.5,  "*", alas, "*", tinggi, "=",luas)
    print(f'keliling trapesium {2} * {alas} + {2} * {tinggi} = {keliling}')

def l_layang_layang(d1, d2):
    luas = 0.5 * d1 * d2
    keliling = 2 * d1 + 2 * d2
    print(f'luas layang layang', 0.5,  "*", d1, "*", d2, "=",luas)
    print(f'keliling layang layang {2} * {d1} + {2} * {d2} = {keliling}')