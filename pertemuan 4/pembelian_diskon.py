pembelian = int(input("masukkan jumlah pembelian: "))
diskon = pembelian * (10/100)
total_harga = pembelian - diskon

if pembelian >= 100 :
    print('selamat kamu mendapatkan diskon 10%')
elif pembelian < 100 :
    print('maaf blum ada diskon untukmu')
else :
    print('blankkk')
if pembelian >= 100 :
    print('jadi total harga yang harus kamu bayar adalah: Rp.' + str(total_harga))
elif pembelian < 100 :
    print('jadi total harga yang harus kamu bayar adalah: Rp.' + str(pembelian))
