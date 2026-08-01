def hitung_skor(skor, waktu_menit):
    if waktu_menit <= 10:
        return skor + (skor * 0.20)
    else:
        return skor

    
nama_turnament = input("Nama Turnament:")
banyak_pemain = int(input("Banyak Pemain:"))
skor_akhir = []

for i in range(0, banyak_pemain):
    nama_pemain = input("Nama Pemain:")
    skor = int(input("Masukan Skor:"))
    waktu_menit = int(input("Berapa Lama Waktunya:"))
    skor_setelah_bonus = hitung_skor(skor, waktu_menit)
    if skor_setelah_bonus >= 150:
        status = "Juara"
    elif skor_setelah_bonus >= 100 and skor_setelah_bonus <= 149:
        status = "Runner Up"
    else:
        status = "Peserta"

    print(nama_pemain, skor_setelah_bonus, status)
    skor_akhir.append(skor_setelah_bonus)

print(max(skor_akhir))
print("Rata-Rata Skor:", sum(skor_akhir) / len(skor_akhir))

laporan = input("Tampilkan Papan Peringkat:(y/n)")


while laporan != "y" and laporan != "n":
    print("Jawaban tidak valid")
    laporan = input("Cetak laporan Harian:(y/n)")
