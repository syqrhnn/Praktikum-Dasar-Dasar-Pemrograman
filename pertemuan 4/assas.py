# Fungsi untuk penjumlahan
def tambah(x, y):
    return x + y

# Fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    if y == 0:
        return "Error! Pembagian dengan 0 tidak diperbolehkan."
    else:
        return x / y

# Fungsi untuk perpangkatan
def pangkat(x, y):
    return x ** y

# Menampilkan menu kalkulator
def kalkulator():
    print("Pilih operasi yang ingin dilakukan:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")

    # Input pilihan operasi
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    # Memastikan input valid
    if pilihan in ['1', '2', '3', '4', '5']:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))

        # Menentukan operasi berdasarkan pilihan pengguna
        if pilihan == '1':
            print(f"{num1} + {num2} = {tambah(num1, num2)}")
        elif pilihan == '2':
            print(f"{num1} - {num2} = {kurang(num1, num2)}")
        elif pilihan == '3':
            print(f"{num1} * {num2} = {kali(num1, num2)}")
        elif pilihan == '4':
            print(f"{num1} / {num2} = {bagi(num1, num2)}")
        elif pilihan == '5':
            print(f"{num1} ^ {num2} = {pangkat(num1, num2)}")
    else:
        print("Pilihan tidak valid!")

# Menjalankan program kalkulator
while True:
    kalkulator()
    lagi = input("Apakah Anda ingin melakukan operasi lagi? (ya/tidak): ").lower()
    if lagi != 'ya':
        print("Terima kasih telah menggunakan kalkulator.")
        break
