tahun = int(input("masukkan tahun:"))
def kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False
    
if kabisat(tahun):
    print("tahun",tahun, "merupakan tahun kabisat.")
else:
    print("tahun",tahun,"bukan tahun kabisat.")
