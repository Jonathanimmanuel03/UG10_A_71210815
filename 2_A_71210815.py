import os 
os.system("cls")

print("#"*30)
print("Kalkulator Advance Sederhana")
print("#"*30)

print("1. Menghitung sisa hasil bagi\n2. Membulatkan ke bawah hasil pembagian\n3. Mencari akar kubik sebuah bilangan ")
pilih = int(input("Masukan Menu Yang anda Pilih : "))
if pilih == 1 :
    a = float(input("masukan bilangan yang ingin dibagi : "))
    b = float(input("masukan bilangan pembagi : "))
    c = a % b
    print("Sisa hasil bagi",a,"dibagi dengan",b,"adalah",c)

elif pilih == 2 :
    a = float(input("masukan bilangan yang ingin dibagi : "))
    b = float(input("masukan bilangan pembagi : "))
    c = a // b
    print("Sisa hasil bagi",a,"dibagi dengan",b,"dibulatkan kebawah adalah",c)

elif pilih == 3 :
    a = float(input("masukan bilangan yang ingin dicari akar kubiknya : "))
    b = a ** (1/3)
    print("Akar kubik dari",a,"adalah",b)
