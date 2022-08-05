# Membaca file hello.txt dengan fungsi readlines()
import requests
print(">>> Membaca file hello.txt dengan fungsi readlines()")
file = open("hello.txt", "r")
all_lines = file.readlines()
file.close()
print(all_lines)
# Membaca file hello.txt dengan menerapkan looping
print(">>> Membaca file hello.txt dengan menerapkan looping")
file = open("hello.txt", "r")
for line in file:
    print(line)

# dibawah ini update 2022
url = "https://storage.googleapis.com/dqlab-dataset/hello.txt"
response = requests.get(url)
# Cetak kode status dari response
print(response)
# Cetak isi file hello.txt menggunakan atribut response.text
print("\n>> Cetak isi file hello.txt menggunakan atribut response.text:")
print(response.text)