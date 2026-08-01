def hitung_total_sewa(harga_per_jam, jam_sewa):
    total = harga_per_jam * jam_sewa
    if jam_sewa >= 4:
        dapat_diskon = "Diskon 25%"
        return total - (total * 0.25)

    else:
        dapat_diskon = "Tidak Dapat Diskon"
        return total

nama_studio = input("Nama Studio:")
banyak_booking = int(input("Banyak Booking:"))
total_biaya = []    

for i in range(0, banyak_booking):
    nama_pemesan = input("Nama Pemesan:")
    jam_sewa = int(input("Jam Sewa:"))
    harga_sewa_per_jam = int(input("Harga Sewa Per Jam:"))
    total_biaya_sewa = hitung_total_sewa(harga_sewa_per_jam, jam_sewa)
    if total_biaya_sewa >= 800000:
        status_booking = "Premium"
    elif total_biaya_sewa >= 300000 and total_biaya_sewa <= 799999:
        status_booking = "Standart"
    else:
        status_booking = "Ekonomis"
    print(nama_pemesan, "- Total Tagihan: Rp", total_biaya_sewa, "(", status_booking, ")")
    total_biaya.append(total_biaya_sewa)

print("Total Studio Musik: Rp", sum(total_biaya))
print("Tagihan Tertinggi: Rp", max(total_biaya))    


laporan = input("Cetak Laporan Booking:(y/n)")

while laporan != "y" and laporan != "n":
    print("Jawaban tidak valid")
    laporan = input("Cetak Laporan Booking:(y/n)")