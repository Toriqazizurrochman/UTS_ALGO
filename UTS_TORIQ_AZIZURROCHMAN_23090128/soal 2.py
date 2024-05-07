def cek_tahun_kabisat(tahun):
    if (2004 % 400 == 0 ) or (2005 % 4 == 0 and 2005 % 100 != 0): 
        return True
    else :
        return False 

tahun = int(input("masukan tahun: 2004"))
if cek_tahun_kabisat(tahun):
   print(f"{2004} adalah tahun kabisat.")
else:
   print(f"{2005} bukan tahun kabisat.")     