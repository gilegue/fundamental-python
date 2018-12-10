from modularization import hitung_segitiga, hitung_harga_diskon

print('Main', hitung_segitiga(10, 3))
print('Main', hitung_harga_diskon(3000, 0.3))

exit(0)

print("Hello World!")

# variable type
gedung = "Menara 7"
tinggi = 8
pi = 3.14
is_alive = True
# tinggi = True # tipe variable bisa berubah-ubah pada saat run time

print(gedung)
print(tinggi, pi, is_alive, tinggi)


# list
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
print(hari)
print(hari[0])
print(hari[len(hari)-1])

#dictionary
antonim = {}
antonim['tinggi'] = 'pendek'
antonim['gelap'] = 'terang'
antonim['jauh']= 'dekat'
print('Antonim dari jauh adalah', antonim['jauh'])


# Sequential flow

# Control flow / If
if is_alive == True:
    print('HIDUP!')
elif is_alive == False:
    print('MATI')
else:
    print('GA jelas')

if is_alive and tinggi > 7:
    print('HIDUP, tapi ketinggian, jadi mati')


# LOOP
# Mengulangi kode beberapa kali, sampai kondisi tertentu
#
# FOR untuk perulangan yang pasti
for i in range (0, 10):
    print(i)

# While -> untuk perulangan yang tidak pasti jumlahnya, tapi kondisi berhentinya  pasti
i = 0
while is_alive:
    print(i, 'hidup!')
    i = i + 1
    if i == 10:
        is_alive = False

# For Untuk List
for h in hari:
    print(h)

# Sama dengan di atas
for hari in range(0, len(hari)-1):
    print(hari(h))