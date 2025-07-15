nama = input("masukkan nama anda: ")
NoHp = input("masukkan No HP anda: ")
pesanmenu = input("""Pesan menu apa? 
makanan | minuman
masukkaan pilihan anda
= """).lower()

if pesanmenu == 'makanan' :
    print('''menu makanan:
===================================
1. nasi goreng harga = Rp 15.000
2. mie goreng  harga = Rp 12.000
3. ayam geprek harga = Rp 18.000
''')
elif pesanmenu == 'minuman' :
    print('''menu minuman:
===================================
1. aneka jus     harga = Rp 15.000
2. soft drink    harga = Rp 10.000
3. sweet ice tea harga = Rp 5.000
''')
else :
    print('salah masukkan menu')

pesanan = input('masukkan pesanan: ').lower()
jumlah = int(input('masukkan jumlah pesanan: '))

if pesanan == 'nasi goreng' :
    harga = 15000
elif pesanan == 'mie goreng' :
    harga = 12000
elif pesanan == 'ayam geprek' :
    harga = 18000
elif pesanan == 'aneka jus' :
    harga = 12000
elif pesanan == 'soft drink' :
    harga = 10000
elif pesanan == 'sweet ice tea' :
    harga = 5000
else :
    print('salah masukkan pesanan')

total = harga * jumlah

print('===================================')
print('nama pembeli      :', nama)
print('no hp             :', NoHp)
print('menu yang dipesan :', pesanan)
print('jumlah pesanan    :', jumlah)
print('total harga       :', total)