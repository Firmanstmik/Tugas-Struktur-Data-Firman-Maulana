print("||"+22*"="+"||")
print("|| Tugas Firman Maulana ||")
print(40*"-")
print("Menghitung luas segitiga dan persegi \nmenggunakan module")
print(40*"=")

def luas_segitiga(alas,tinggi):
    luas = (alas * tinggi)/2
    print("luas segitiga = 1/2 * alas * tinggi")
    return print("\t      = 1/2 *", alas, "*", tinggi, "=", luas)

def luas_persegi(panjang,lebar):
    luas = panjang * lebar
    print("luas persegi  = panjang * lebar")
    return print("\t      =", panjang, "*", lebar, "=", luas)