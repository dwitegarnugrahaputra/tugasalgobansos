kuota = ["10 GB", "20 GB"]
pelajar = ["Pelajar","pelajar"]
user = str(input("Kategori Pendapat Kuota (Pelajar/Mahasiswa) : "))
print("Masukkan data diri")
nama = str(input("Nama : "))
sekolah = str(input("Nama sekolah/kampus : "))
if user in pelajar:
    print(f"Anda mendapat " + kuota[0])
else:
    print(f"Anda mendapat " + kuota[1])