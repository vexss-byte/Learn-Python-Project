nama_kelas = input("Nama Kelas:")
jumlah_siswa = int(input("Jumlah Siswa:"))

def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    nilai_akhir = (nilai_tugas * 0.2) + (nilai_uts * 0.3) + (nilai_uas * 0.5)
    return nilai_akhir

def tentukan_predikat(nilai_akhir):
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 70 and nilai_akhir <= 84:
        return "B"
    elif nilai_akhir >= 60 and nilai_akhir <= 69:
        return "C"
    else:
        return "D"

def cek_kelulusan(nilai_akhir, nilai_uts, nilai_uas):
    if nilai_akhir < 60 or nilai_uts < 50 or nilai_uas < 50:
        return "Tidak Lulus"
    else:
        return "Lulus"

semua_siswa = []

for i in range(0, jumlah_siswa):
    data = {}
    data["nama"] = input("Nama Siswa:")
    data["nilai_tugas"] = int(input("Nilai Tugas:"))
    data["nilai_uts"] = int(input("Nilai Uts:"))
    data["nilai_uas"] = int(input("Nilai Uas:"))
    data["nilai_akhir"] = hitung_nilai_akhir(data["nilai_tugas"], data["nilai_uts"], data["nilai_uas"])
    data["predikat"] = tentukan_predikat(data["nilai_akhir"])
    data["status"] = cek_kelulusan(data["nilai_akhir"], data["nilai_uts"], data["nilai_uas"])
    semua_siswa.append(data)

daftar_nilai_akhir = []
for siswa in semua_siswa:
    daftar_nilai_akhir.append(siswa["nilai_akhir"])

print("Nilai Tertinggi:", max(daftar_nilai_akhir))
print("Total Nilai:", sum(daftar_nilai_akhir))
print("Rata-Rata Skor:", sum(daftar_nilai_akhir) / len(daftar_nilai_akhir))

jumlah_tidak_lulus = 0
for siswa in semua_siswa:
    if siswa["status"] == "Tidak Lulus":
        jumlah_tidak_lulus += 1

siswa_nilai_tertinggi = {}
nilai_tertinggi = 0
for siswa in semua_siswa:
    if siswa["nilai_akhir"] > nilai_tertinggi:
        nilai_tertinggi = siswa["nilai_akhir"]
        siswa_nilai_tertinggi = siswa


    
laporan = input("Cetak rapor kelas? (ya/tidak)")

while laporan != "ya" and laporan != "tidak":
    print("Jawaban tidak valid")
    laporan = input("Cetak laporan Harian:(ya/tidak)")

print("===== LAPORAN NILAI =====")
print("Nama Kelas:", nama_kelas)
print("Jumlah Siswa:", jumlah_siswa)
print("Nilai Tertinggi:", siswa_nilai_tertinggi["nama"], "-", nilai_tertinggi)
print("Rata-Rata Nilai Kelas:", sum(daftar_nilai_akhir) / len(daftar_nilai_akhir))
print("Jumlah Siswa Tidak Lulus:", jumlah_tidak_lulus)