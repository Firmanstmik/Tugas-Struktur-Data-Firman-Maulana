print(18*" ", 27*"=")
print(18*" ", "|| TUGAS 3 STRUKTUR DATA ||")
print(18*" ", "|| NAMA : FIRMAN MAULANA ||")
print(18*" ", 27*"=")
print("\n")

mahasiswa1 = {
    'nama':'Firman Maulana',
    'prodi':'Teknik Informatika',
    'nim':'TI19220003',
    'semester':'2',
    'asal':'Taliwang, KSB',
    'nilai akumulasi':90
}

mahasiswa2 = {
    'nama':'Nora Ananda Putri',
    'prodi':'Teknik Informatika',
    'nim':'TI19220015',
    'semester':'2',
    'asal':'Ganti, Pratim',
    'nilai akumulasi':85
}

mahasiswa3 = {
    'nama':'Siti Yulistira',
    'prodi':'Teknik Informatika',
    'nim':'TI19220025',
    'semester':'2',
    'asal':'pringgarata',
    'nilai akumulasi':83
}

mahasiswa4 = {
    'nama':'Yasmin Rosana',
    'prodi':'Teknik Informatika',
    'nim':'TI19220023',
    'semester':'2',
    'asal':'Sembalun',
    'nilai akumulasi':79
}

mahasiswa5 = {
    'nama':'Melinda',
    'prodi':'Teknik Informatika',
    'nim':'TI19220016',
    'semester':'2',
    'asal':'Bodak',
    'nilai akumulasi':80
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3,
    'MAH004':mahasiswa4,
    'MAH005':mahasiswa5
}

print(f"{'KODE':<10} {'Nama':<20} {'Prodi':<20} {'Nim':^20} {'Semester':^15} {'Asal':<17} {'Akumulasi Nilai':^10}")
print("-"*125)

for mahasiswa in data_mahasiswa:

    KODE = mahasiswa

    NAMA = data_mahasiswa[KODE] ['nama']
    PRODI = data_mahasiswa[KODE] ['prodi']
    NIM = data_mahasiswa[KODE] ['nim']
    SEMESTER = data_mahasiswa[KODE] ['semester']
    ASAL = data_mahasiswa[KODE] ['asal']
    NILAI = data_mahasiswa[KODE] ['nilai akumulasi']

    print(f"{KODE:<10} {NAMA:<20} {PRODI:<20} {NIM:^20} {SEMESTER:^15} {ASAL:<17} {NILAI:^10}")