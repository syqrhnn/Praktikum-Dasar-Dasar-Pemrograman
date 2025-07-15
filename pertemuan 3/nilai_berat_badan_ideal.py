print('Mencari nilai berat badan ideal')
#Diketahui
tinggi = int(input('masukkan tinggi badanmu: '))
#Rumus
berat_badan_ideal = (tinggi - 100) - ((tinggi - 100) * 15/100)
#Hasil
print("------------hasil-------------")
print('tinggi badan         :', tinggi,'cm')
print('berat badan idealnya :', berat_badan_ideal,'kg')