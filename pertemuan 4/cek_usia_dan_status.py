usia = int(input("masukkan usiamu: "))

if usia >= 18 <= 24 :
    print('kamu sudah DEWASA')
elif usia >= 13 and usia <= 17 :
    print('kamu saat ini sedang memasuki masa remaja')
elif usia < 18 :
    print('kamu masih anak-anak')
else:
    print('kamu bukan orang')