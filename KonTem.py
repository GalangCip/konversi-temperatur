# Fungsi untuk mengonversi Celsius ke Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Meminta pengguna untuk memasukkan suhu dalam derajat Celsius
celsius = float(input("Masukkan suhu dalam derajat Celsius: "))

# Mengonversi suhu ke Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Mencetak hasil konversi
print(f"Suhu dalam derajat Fahrenheit: {fahrenheit:.2f} °F")