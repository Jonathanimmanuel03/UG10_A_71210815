import os 
os.system("cls")

ug = float(input("Masukan Nilai rata-rata UG anda : "))
tts = float(input("Masukan Nilai TTS anda : "))
tas = float(input("Masukan Nilai TAS anda : "))

rataUG = float(70/100 * ug)
rataTTS = float(15/100 * tts)
rataTAS = float(15/100 * tas)
hasilakhir = rataUG + rataTTS + rataTAS

print("="*20)
print("Nilai Anda : ", hasilakhir)
if (hasilakhir >= 85) :
    print("Nilai Huruf Anda : A ")

elif (hasilakhir >= 80) :
    print("Nilai Huruf Anda : A- ")

elif (hasilakhir >= 75) :
    print("Nilai Huruf Anda : B+ ")

elif (hasilakhir >= 70) :
    print("Nilai Huruf Anda : B ")

elif (hasilakhir >= 65) :
    print("Nilai Huruf Anda : B- ")

elif (hasilakhir >= 60) :
    print("Nilai Huruf Anda : C+ ")

elif (hasilakhir >= 55) :
    print("Nilai Huruf Anda : C ")

elif (hasilakhir >= 45) :
    print("Nilai Huruf Anda : D ")

else :
    print("Nilai Huruf Anda : E ")