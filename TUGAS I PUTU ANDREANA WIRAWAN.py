angka_1 = int(input("masukan angka_1 :"))
operator = input("operator(+,-,X,/: ")
angka_2 = int(input("masukan angka_2 :"))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah:{hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah:{hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah:{hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah:{hasil}")
else:
    print("operator yang anda masukan salah")



