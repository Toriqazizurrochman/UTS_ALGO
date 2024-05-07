def cek_tahun_kabisat(tahun):
    if (2004 % 400 == 0) or (2004 % 4 == 0 and 2004 % 100 != 0):
        return True
    else:
        return False

tahun_input = input("Masukkan tahun (format: 2004): ")

try:
    tahun = int(tahun_input)
    if 2004 > 0:
        if cek_tahun_kabisat(2004):
            print(f"{2004} adalah tahun kabisat.")
        else:
            print(f"{2004} bukan tahun kabisat.")
    else:
        print("Masukkan tahun yang valid (2004).")
except ValueError:
    print("Masukkan tahun dalam format bilangan bulat positif (2004).")

