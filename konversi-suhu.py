# program konversi celcius ke satuan lain

# # reamur
# reamur = (4/5) * celcius

# # fahrenheit
# fahrenheit = ((9/5) * celcius) + 32

# # kelvin
# kelvin = celcius + 273

print("\nConvertion Program\n")

def convert_temperature(temp, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Reamur":
            return (4/5) * temp
        elif to_unit == "Fahrenheit":
            return ((9/5) * temp) + 32
        elif to_unit == "Kelvin":
            return temp + 273
    else:
        print("Conversion from {} to {} not supported.".format(from_unit, to_unit))
        return None

print("\nConvertion Program\n")

unit_options = ["Celsius", "Reamur", "Fahrenheit", "Kelvin"]

while True:
    celcius = float(input('Masukan suhu celcius : '))
    print("suhu adalah", celcius, "Celcius")

    print("Pilih satuan yang ingin dikonversi :")
    for i, unit in enumerate(unit_options):
        print("{}. {}".format(i+1, unit))
    choice = int(input("Masukkan pilihan: "))
    chosen_unit = unit_options[choice-1]
    if chosen_unit != "Celsius":
        print("suhu dalam {} adalah {:.2f} {}".format(chosen_unit, convert_temperature(celcius, "Celsius", chosen_unit), chosen_unit))
    else:
        print("Sudah dalam celcius")
