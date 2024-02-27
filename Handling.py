while True:
    try:
        angka = int(input("Masukkan sebuah angka bulat: "))
        print("Angka yang dimasukkan:", angka)
        break 
    except ValueError:
        print("Input yang dimasukkan bukan angka bulat. Silakan coba lagi.")

print("Terima kasih!")
