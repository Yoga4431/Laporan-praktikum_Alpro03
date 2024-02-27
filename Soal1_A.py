try:
    nilai = int(input("Masukkan nilai anda: "))
    if nilai >= 50:
        print("Anda sudah lulus.")
    else:
        print("Anda tidak lulus.")
except ValueError:
    print("Gunakan angka sebagai input.")
