print(18*" ", 27*"=")
print(18*" ", "|| TUGAS 3 STRUKTUR DATA ||")
print(18*" ", "|| NAMA : FIRMAN MAULANA ||")
print(18*" ", 27*"=")

list_nilai = [1,2,3,4,5,6,7,8,9,10]
print(f"\n1.) list nilai = {list_nilai}")

jumlah_index = len(list_nilai)
print(f"2.) jumlah index = {jumlah_index}")

jumlah_nilai = list_nilai.count(3)
print(f"3.) jumlah angka 3 = {jumlah_nilai}")

list_nilai.append(11)
print(f"4.) tambah nilai 11 pada list= {list_nilai}")

list_nilai.insert(4,97)
print(f"5.) tambah nilai 97 setelah angka 4 dan sebelum angka 5 = {list_nilai}")

item_paling_akhir = list_nilai[-1]
print(f"6.) lihat item akhir = {item_paling_akhir}")
nilai2_terakhir = list_nilai[-2]
print(f"\tlihat item 2 terakhir = {nilai2_terakhir}")
nilai3_terakhir = list_nilai[-3]
print(f"\tlihat item 3 terakhir = {nilai3_terakhir}")

list_for_if = [i for i in list_nilai if i > 2]
print(f"7.) menampilkan list nilai kecuali nilai 1 & 2 = {list_for_if}")


item7_terakhir = list_nilai[-7]
print(f"8.) lihat item 7 terakhir = {item7_terakhir}")


