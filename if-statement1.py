# input nama
nama = input("Masukan nama anda:bunga ")

# cek nama (misal nama pendek yang benar: "bunga")
if nama == "bunga":
    print("Selamat datang", nama)
else:
    print("Program selesai")

# input umur
umur = int(input("Masukan umur anda: 18 "))

# percabangan umur
if umur <= 0:
    print("Anda belum lahir")
elif umur < 18:
    print("Anda belum cukup umur")
elif umur >= 18 and umur <= 60:
    print("Anda cukup umur")
else:  # umur > 60
    print("Banyakin ibadah, bentar lagi mati")

print("Program selesai")