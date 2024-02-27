def jumlah_hari(bulan):
    bulan = bulan.lower()  
    
    if bulan == "januari" or bulan == "maret" or bulan == "mei" or bulan == "juli" or bulan == "agustus" or bulan == "oktober" or bulan == "desember":
        return 31
    elif bulan == "april" or bulan == "juni" or bulan == "september" or bulan == "november":
        return 30
    elif bulan == "februari":
        return 29 
    else:
        return "Bulan yang dimasukkan tidak valid."

bulan_input = input("Masukkan nama bulan (Contoh: Januari): ")

print("Jumlah hari dalam bulan", bulan_input, "adalah:", jumlah_hari(bulan_input))
