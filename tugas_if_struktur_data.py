print(18*" ", 27*"=")
print(18*" ", "|| TUGAS 1 STRUKTUR DATA ||")
print(18*" ", "|| NAMA : FIRMAN MAULANA ||")
print(18*" ", 27*"=")

daftar_nilai = [25,90,40,95,35,70,50,20,80,65]
nilai_terbesar = daftar_nilai[0] # asumsikan bahwa nilai pada index pertama adalah nilai terbesar
nilai_terkecil = daftar_nilai[0] # asumsikan bahwa nilai pada index pertama adalah nilai terkecil

for nilai in daftar_nilai:
  # Jika nilai yang diperiksa lebih besar dari nilai terbesar sementara
  if nilai_terbesar < nilai: 
    nilai_terbesar = nilai
  # Jika nilai yang diperiksa lebih kecil dari nilai terkecil sementara
  elif nilai_terkecil > nilai:
    nilai_terkecil = nilai

print(65*"-")
print("Daftar nilai mahasiswa: ", daftar_nilai)
print(65*"-")
print("Nilai terbesar mahasiswa: ",nilai_terbesar)
print(30*"-")
print("Nilai terkecil mahasiswa: ",nilai_terkecil)
print(30*"-")