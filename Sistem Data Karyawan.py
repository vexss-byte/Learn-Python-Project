def hitung_bonus_karyawan(gaji_pokok, tahun_kerja):
    if tahun_kerja >= 5:
        return gaji_pokok + (gaji_pokok * 0.15)
    else:
        return gaji_pokok


semua_karyawan = []
banyak_karyawan = int(input("Banyak Karyawan:"))

for i in range(0, banyak_karyawan):
    data = {}
    data["nama"] = input("Nama Karyawan:")
    data["gaji_pokok"] = int(input("Gaji Pokok:"))
    data["tahun_kerja"] = int(input("Berapa Tahun Kerja:"))
    data["gaji_akhir"] = hitung_bonus_karyawan(data["gaji_pokok"], data["tahun_kerja"])
    semua_karyawan.append(data)

for karyawan in semua_karyawan:
    print(karyawan["nama"], "-", karyawan["gaji_akhir"])

total_pengeluaran = 0
for karyawan in semua_karyawan:
    total_pengeluaran = total_pengeluaran + karyawan["gaji_akhir"]

print("Total Pengeluaran Gaji: Rp", total_pengeluaran)
