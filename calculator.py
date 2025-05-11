def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        raise ValueError("Tidak dapat membagi dengan nol")
    return a / b

def pangkat(a, b):
    return a ** b

def main():
    print("Kalkulator Sederhana")
    print("====================")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    if pilihan == '1':
        print(f"{angka1} + {angka2} = {tambah(angka1, angka2)}")
    elif pilihan == '2':
        print(f"{angka1} - {angka2} = {kurang(angka1, angka2)}")
    elif pilihan == '3':
        print(f"{angka1} * {angka2} = {kali(angka1, angka2)}")
    elif pilihan == '4':
        try:
            print(f"{angka1} / {angka2} = {bagi(angka1, angka2)}")
        except ValueError as e:
            print(e)
    elif pilihan == '5':
        print(f"{angka1} ^ {angka2} = {pangkat(angka1, angka2)}")

    else:
        print("Pilihan tidak valid")

    

if __name__ == "__main__":
    main()