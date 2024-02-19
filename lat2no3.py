#  Budi tertarik untuk melamar pekerjaan pada liburan semester yang akan berlangsung selama 5 minggu. Gaji yang diberikan adalah 
# gaji per jam. Total pajak yang harus budi
# bayarkan dari penghasilannya selama bekerja adalah 14%. Setelah membayar pajak, budi
# menghabiskan 10% dari pendapatan bersihnya untuk membeli baju dan aksesoris yang akan
# digunakan pada semester baru, dan 1% untuk membeli alat tulis. Setelah membeli baju, aksesoris dan alat tulis, 
# Budi menggunakan 25% dari sisa uangnya untuk disedekahkan. Setiap
# Rp.1000 yang Budi sedekahkan 30% nya akan diserahkan kepada anak yatim, dan sisanya akan
# diserahkan ke kaum dhuafa.
# Buatlah sebuah program, dengan input:
# 1. Gaji per jam yang anda inginkan
# 2. Jumlah jam kerja yang akan dilakukan dalam 1 minggu
# Output dari program adalah sebagai berikut :
# 1. Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak
# 2. Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak
# 3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris
# 4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis
# 5. Jumlah uang yang akan Budi sedekahkan
# 6. Jumlah uang yang akan diterima anak yatim
# 7. Jumlah uang yang akan diterima kaum dhuafa

gajiperjam = float (input("berapa gaji perjam kamu ="))
jumlahjamkerja = float (input("berapa jumlah jam kerja yang dilakukan dalam 1 minggu ="))

pdpsebelumpajak = gajiperjam * jumlahjamkerja *5
print("Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak adalah",pdpsebelumpajak)

pdpsetelahpajak = pdpsebelumpajak - (0.14 * pdpsebelumpajak)
print("Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak adalah",pdpsetelahpajak)

pdpbersih = pdpsetelahpajak 

buatbelibaju = pdpbersih * 0.1
print("Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris adalah",buatbelibaju)

buatbelialattulis = pdpbersih * 0.01
print("Jumlah uang yang akan Budi habiskan untuk membeli alat tulis adalah",buatbelialattulis)

sisauang = pdpbersih - buatbelibaju - buatbelialattulis
buatsedekah = sisauang -(sisauang * 0.25)

print("Jumlah uang yang akan Budi sedekahkan :",buatsedekah)

buatyatim = buatsedekah * 0.3
print("Jumlah uang yang akan diterima anak yatim",buatyatim)

buatdhuafa = buatsedekah - buatyatim
print("Jumlah uang yang akan diterima kaum dhuafa :",buatdhuafa)









