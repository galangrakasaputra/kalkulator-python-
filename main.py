# Program Kalkulator BMI
print("Kalkulator BMI")
print("--------------")

beratBadan = float(input("Msaukkan Berat Badan (KG) : "))
print(f"Berat Badan {beratBadan} KG")
tinggi = float(input("Masukan Tinngi Badan (M) : "))
print(f"Tinggi Badan {tinggi} M")

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi**2)
berat_badan_ideal['atas'] = 25*(tinggi**2)

bmi = beratBadan/(tinggi**2)

if bmi < 5:
    kategori = "kurang berat badan"
elif bmi < 25:
    kategori = "berat badan normal"
elif bmi < 30:
    kategori = "kelebihan berat badan"
else:
    kategori = "Obesitas"

print(f"BMI : {bmi:.2f} Kg/M^2")
print(f"Berat badan ideal (bawah - atas) : {berat_badan_ideal['bawah']:.2f} - {berat_badan_ideal['atas']:.2f} Kg/M^2")
print(f" {kategori}")