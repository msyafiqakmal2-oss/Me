import random

angka_rahasia = random.randint(1, 10)
percobaan = 0
print ("Game Tebak Angka")
print("Tebak Angka Dari 1 - 10")

while True:
    tebakan = int(input("Masukkan Tebakanmu : "))
    percobaan += 1
    if tebakan < angka_rahasia:
        print("Terlalu Kecil ! Silahkan Coba Lagi ?")
    elif tebakan > angka_rahasia:
        print("Terlalu Besar ! Silahkan Coba Lagi ?")
    else:
        print(f" Benar !! Angka Nya {angka_rahasia}")
        print(f" Kamu Menebak {percobaan} kali "  )  
        break  
    