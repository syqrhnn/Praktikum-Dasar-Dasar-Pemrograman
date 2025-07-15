nilai = int(input("masukkan nilai anda:  "))

if nilai >= 75 :
    print('kamu dinyatakan lulus')
elif nilai < 75 :
    print('kamu dinyatakan tidak lulus')
else:
    print('kamu ga jelas')
if nilai >= 90 : 
    print('degan predikat A')
if nilai >= 75 and nilai < 90 : 
    print('degan predikat B')
if nilai >= 65 and nilai < 75 : 
    print('degan predikat C')
if nilai < 65 : 
    print('degan predikat D')