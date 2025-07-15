#Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius.
#Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
#print(celcius_ke_fahrenheit(0))    # Output: 32.0
#print(celcius_ke_fahrenheit(100))  # Output: 212.0


print ('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32  # mengkonversi suhu dari celcius ke fahrenheit
    return fahrenheit  # mengembalikan nilai fahrenheit

suhu_celcius1 = 0 
suhu_celcius2 = 100

#cetak 0 celcius ke 32 fahrenheit
suhu_fahrenheit1 = celcius_ke_fahrenheit(suhu_celcius1)

#cetak 100 celcius ke 212 fahrenheit
suhu_fahrenheit2 = celcius_ke_fahrenheit(suhu_celcius2)

print('Suhu celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)
print('Suhu celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)


#Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat.
#Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
#print(is_genap(4))  # Output: True
#print(is_genap(7))  # Output: False

print()
print('## Nomor 2 ##')
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0  # membentuk bilangan ganjil atau genap 
    return hitung   # mengembalikan nilai hitung

angka1 = 4
hasil1 = genap_ganjil(angka1)  # mendefinisikan bilangan
print(f"bilangan {angka1} bernilai {hasil1}")  # memanggil fungsi

angka2 = 7
hasil2 = genap_ganjil(angka2)
print(f"bilangan {angka2} bernilai {hasil2}")


#Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
#nilai (80) #lulus
#nilai(60) #gagal

print()
print('## Nomor 3 ##')
def cek_kelulusan(nilai):
    if nilai > 60 :
        return 'lulus'
    else :
        return 'gagal'
    
nilai_kamu1 = 80  # mendefinisikan nilai 
status1 = cek_kelulusan(nilai_kamu1)  # memanggil fungsi dan parameter
print(f"Nilai: {nilai_kamu1}")
print(f"status: {status1}")

nilai_kamu2 = 60  # mendefinisikan nilai 
status2 = cek_kelulusan(nilai_kamu2)  # memanggil fungsi dan parameter
print(f"Nilai: {nilai_kamu2}")
print(f"status: {status2}")


#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
##bilangan(20) # 1,3,5,7,9,11,13,15,17,19


print()
print('## Nomor 4 ##')
def bilangan_ganjil(bilangan):
    for i in range(1, bilangan + 1):
        if i % 2 == 1:
            print(i)

bilangan_ganjil(20)