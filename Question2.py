Data = ('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')

nim = []
for num in Data[1]:
    nim.append(num)
nim = tuple(nim)

name = Data[0].split()
initial = name[0]

alpha = []
for i in range(1, len(initial)):
    alpha.append(initial[i])
alpha = tuple(alpha)

name.reverse()
rever = tuple(name)

print(f"{Data}\n")
print(f"NIM\t:\t{Data[1]}")
print(f"NAMA\t:\t{Data[0]}")
print(f"ALAMAT\t:\t{Data[2]}\n")
print(f"NIM:\t{nim}\n")
print(f"NAMA DEPAN:\t{alpha}\n")
print(f"NAMA TERBALIK:\t{rever}")