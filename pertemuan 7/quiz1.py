nama_kendaraan = input ("masukkan nama kendaraan: ")
jenis_bensin = input ("masukkan jenis bensin: ")

if jenis_bensin == 'pertalite' :
    harga = 10000
    jarak_tempuh = 12
elif jenis_bensin == 'pertamax' :
    harga = 14000
    jarak_tempuh = 13
elif jenis_bensin == 'pertamax turbo' :
    harga = 17000
    jarak_tempuh = 13.5
else :
    print('salah masukkan jenis bensin')


kota = input ("masukkan kota: ")

if kota == 'jakarta' :
    jarak = 20
elif kota == 'bekasi' :
    jarak = 35.7
elif kota == 'depok' :
    jarak = 5
elif kota == 'tanggerang' :
    jarak = 99
elif kota == 'bogor' :
    jarak = 120.6
else :
    print('salah masukkan nama kota')

pemakaian_bensin = jarak / jarak_tempuh
total = pemakaian_bensin * harga


print('===================================')
print('nama kendaraan    :', nama_kendaraan)
print('jenis bensin      :', jenis_bensin)
print('kota yang dituju  :', kota)
print('pemakaian bensin  :', int(pemakaian_bensin), 'liter')
print('total harga       : Rp', int(total))