def jenis_segitiga(sisi1, sisi2, sisi3):
    if sisi1 == sisi2 == sisi3:
        return "Segitiga sama sisi"
    elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
        return "Segitiga sama kaki"
    else:
        return "Segitiga sembarang"

try:
    sisi1 = float(input("Masukkan panjang sisi pertama: "))
    sisi2 = float(input("Masukkan panjang sisi kedua: "))
    sisi3 = float(input("Masukkan panjang sisi ketiga: "))

    if sisi1 + sisi2 > sisi3 and sisi1 + sisi3 > sisi2 and sisi2 + sisi3 > sisi1:
        print("Segitiga dengan panjang sisi-sisi yang diberikan adalah", jenis_segitiga(sisi1, sisi2, sisi3))
    else:
        print("Panjang sisi-sisi yang dimasukkan tidak membentuk segitiga.")

except ValueError:
    print("Panjang sisi harus berupa bilangan.")
