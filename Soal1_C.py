try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    angka3 = float(input("Masukkan angka ketiga: "))

    hasil = angka1 + angka2 + angka3
    print("Hasil penjumlahan ketiga angka:", hasil)

except ValueError:
    print("Input yang dimasukkan harus berupa angka.")
