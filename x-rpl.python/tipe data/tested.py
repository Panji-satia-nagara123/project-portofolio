#segitiga biasa
max = int(input("jumlah bintang: "))
for i in range(max):
    
    for s in range(max - i - 1):
        print(" ", end=" ")
    
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
#segitiga kanan
max = int(input("jumlah bintang: "))
for i in range(max):
    for s in range(i):
        print(" ", end=" ")
    for j in range(max - i):
        print("*", end=" ")
    print()