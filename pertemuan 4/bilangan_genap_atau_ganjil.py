bilangan = int(input("masukkan angka: "))

hasil = bilangan % 2
if hasil == 0 :
    print(f"Angka {bilangan} merupakan angka genap")
elif hasil == 1 :
    print(f"Angka {bilangan} merupakan angka ganjil")
else:
    print('Angka ga jelas')
