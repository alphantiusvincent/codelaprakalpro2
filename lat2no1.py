# Latihan 2.1 Buatlah program yang dapat menghitung berat badan yang diperlukan, jika diketahui tinggi badan dan nilai Body Mass Index (BMI) yang diharapkan! Body Mass Index
# dihitung dengan cara: BMI =
# berat/ tinggi
# . Perhatikan, berat badan dalam satuan kilogram (kg) dan
# tinggi badan dalam satuan meter (m).

bb = float(input ("berapa berat badankamu (kg): "))
tb = float(input ("berapa Tinggi badan kamu(m) : "))
bmi = bb / ( tb ** 2)
print("jadi bmi kamu adalah:%.2f" %bmi)