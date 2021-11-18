import os 
os.system("cls")

pilih = str(input("Mendatar/Menurun : "))
if pilih in ["mendatar","Mendatar"] :
    n = int(input("Masukan Kolom : "))  
    for i in range(n):   
        print("* ", end="")       
elif pilih in ["menurun","Menurun"] :
    o = int(input("Masukan Baris : "))
    for i in range (o):
        print("* ")
else :
        print("Pola Tidak Dikenali !")





