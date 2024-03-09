# aplikasi menghitung harga jual berdasarkan persen
hargaSupplier = int(input("Silahkan Masukan harga dari supplier: "))
persen  = int(input("Silahkan persen keuntungan yang anda inginkan: "))
hargaPersen = hargaSupplier * (persen / 100)
hargaJual = hargaSupplier + hargaPersen

print("Harga dari supplier: ",hargaSupplier)
print("Persen keuntungan: ",persen)
print("Keuntungan dari persen: ",hargaPersen)
print("Harga Jual: ",hargaJual)