tinggi = 10
alas = 5

# Satu segitiga
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)


# Segitiga kedua
tinggi2 = 7
alas2 = 8
luas_segitiga_2 = alas2 * tinggi2 / 2
print(luas_segitiga_2)

def hitung_segitiga(alas, tinggi):
    return alas * tinggi / 2

segitiga1 = hitung_segitiga(10, 5)
segitiga2 = hitung_segitiga(7, 8)

print(segitiga1, segitiga2)

# TUGAS: FUNGSI PENGHITUNG DISKON.
# Parameter: total harga dan nilai diskon.
# Hasil fungsi: mengembalikan harga yang sudah didiskon
# Cetak hasilnya.

# discount in 0.x
def hitung_harga_diskon(total_harga, nilai_diskon):
    return total_harga - (total_harga * nilai_diskon)

kembalian = hitung_harga_diskon(2000, 0.25)
print('Kembaliannya adalah', kembalian)