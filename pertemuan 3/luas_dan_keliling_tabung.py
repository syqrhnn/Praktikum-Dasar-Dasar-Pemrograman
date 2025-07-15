print('Menghitung Luas Permukaan, Volume, dan Keliling Alas')
#Diketahui
phi = 22/7
r = int(input('masukan jari jari tabung: '))
t = int(input('masukan tinggi tabung: '))
#Rumus
luas_permukaan = str( 2 * phi * r *(r + t))
volume = str(phi * r * r * t)
keliling_alas = str(2 * phi * r) 
#Hasil
print("-----------------hasil------------------")
print('luas permukaan tabung adalah: ' + luas_permukaan +'cm²')
print('volume tabung adalah        : ' + volume +'Cm³')
print('keliling alas tabung adalah : ' + keliling_alas +'cm²')