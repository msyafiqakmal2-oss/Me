# Data suhu
x1, y1 = 1, 30   # hari 1, suhu 30
x2, y2 = 3, 32   # hari 3, suhu 32

# Hari yang ingin diprediksi
x = 2

# Rumus interpolasi linear
y = y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)

print("Perkiraan suhu hari ke-2:", y, "°C")
