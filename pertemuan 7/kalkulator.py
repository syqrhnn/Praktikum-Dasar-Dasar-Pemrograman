angka1 = float(input("masukkan angka1: "))
angka2 = float(input("masukkan angka2: "))
operator = input("""pilih operator:
tambah | kurang | kali | bagi | pangkat
masukkaan operator yang akan anda gunakan
= """).lower()

if operator == 'tambah' :
    jumlah = angka1 + angka2
    print('hasil operator =', jumlah )
elif operator == 'kurang' :
    jumlah = angka1 - angka2
    print('hasil operator =', jumlah )
elif operator == 'bagi' :
    jumlah = angka1 / angka2
    print('hasil operator =', jumlah )
elif operator == 'kali' :
    jumlah = angka1 * angka2
    print('hasil operator =', jumlah )
elif operator == 'pangkat' :
    jumlah = angka1 ** angka2
    print('hasil operator =', jumlah )
else :
    print('salah masukkan menu')

