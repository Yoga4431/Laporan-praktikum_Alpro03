try:
    angka = float(input("Masukkan sebuah angka: "))
    
    status = "positif" if angka > 0 else "negatif" if angka < 0 else "nol"
    
    print("Angka yang dimasukkan adalah", status)
    
except ValueError:
    print("Input yang dimasukkan harus berupa angka.")
