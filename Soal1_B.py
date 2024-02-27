try:
    panjang = float(input("Masukkan panjang (dalam meter): "))
    lebar = float(input("Masukkan lebar (dalam meter): "))
    
    if panjang <= 0 or lebar <= 0:
        raise ValueError("Panjang dan lebar harus lebih besar dari nol.")
    
    luas = panjang * lebar
    print("Luas persegi panjang adalah:", luas, "meter persegi.")
    
except ValueError as e:
    print("Error:", e)
