jumlah = float(input('masukan jumlah barang :'))
if jumlah == 1:
    barang1 = float(input('masukan harga barang ke-1 :'))
    print('total belanjaan :',barang1)
elif jumlah == 2 : 
    barang1 = float(input('masukan harga barang ke-1 :'))
    barang2 = float(input('masukan harga barang ke-2 :'))
    print('total belanjaan :',barang1 + barang2)
else :
    print('sorry max 2 barang')
