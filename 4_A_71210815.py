import os 
os.system("cls")

berita = input("Masukan artikel yang ingin dipindai : ")
nama_klub = input("Masukan nama klub favorit anda : ")
skor_bola = input("Masukan skor yang ingin dicari : ")

if skor_bola in berita and nama_klub in berita :
    print("Hasil Pencarian ditemukan ! ")
elif nama_klub in berita :
    print("Hanya kata {} yang ditemukan pada artikel ini ".format(nama_klub))
elif skor_bola in berita :
    print("Hanya skor {} yang ditemukan pada artikel ini ".format(skor_bola))
else :
    print("Hasil pencarian {} dan {} tidak ditemukan ! ".format(nama_klub,skor_bola))