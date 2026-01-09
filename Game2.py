import random

pilihan = ["Batu", "Gunting", "Kertas"]

print(" Game Batu Gunting Kertas ")

user = input("Pilih (batu/gunting/kertas) : ").lower()
komputer = random.choice(pilihan)

print("Komputer Memilih :", komputer)

if user == komputer:
    print("Hasil = Seri")
elif ( user == "batu" and komputer == "gunting") or \
     ( user == "gunting" and komputer == "kertas") or \
     ( user == "kertas" and komputer == "batu"):
    print("Kamu Menang !!")
else:
    print("Kamu Kalah !")
    