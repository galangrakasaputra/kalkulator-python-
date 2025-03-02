# Program Kalkulator BMI
print("Kalkulator BMI")
print("--------------")

beratBadan = float(input("Msaukkan Berat Badan (KG) : "))
print(f"Berat Badan {beratBadan} KG")
tinggi = float(input("Masukan Tinngi Badan (M) : "))
print(f"Tinggi Badan {tinggi} M")

bmi = beratBadan/(tinggi**2)

print(f"BMI : {bmi:.2f} Kg/M^2")