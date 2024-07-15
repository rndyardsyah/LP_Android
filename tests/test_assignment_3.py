input_angka = input("Input: ")
angka_list = input_angka.split()

ganjil = []
genap = []

for angka in angka_list:
    angka_int = int(angka)
    if angka_int % 2 == 0:
        genap.append(angka_int)
    else:
        ganjil.append(angka_int)

genap.sort(reverse=True)

output_array = genap + ganjil

print("Output:", output_array)