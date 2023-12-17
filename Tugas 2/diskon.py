harga = float(input("Masukan harga barang: "))
diskon = 0

# if harga > 75000:
#     diskon = harga * 0.5
#     if diskon > 50000:
#         diskon = 50000
# elif harga > 30000 and harga <= 75000:
#     diskon = harga * 0.3
#     if diskon > 30000:
#         diskon = 30000
# else:
#     diskon = 0
    
# print(f"Diskon: {diskon}")

if harga > 75000:
    diskon = harga * 0.5
    if diskon > 50000:
        diskon = 50000

if harga > 30000 and harga <= 75000:
    diskon = harga * 0.3
    if diskon > 30000:
        diskon = 30000

if harga < 30000:
    diskon = 0
    
print(f"Diskon: {diskon}")