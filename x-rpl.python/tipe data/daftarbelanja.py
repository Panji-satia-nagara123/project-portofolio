print("===Program Daftar Belanja===")

#1
barang=["sampo","sabun","sabun muka"]
barang.append("odol")
print(barang)

#2
barang=["sampo","sabun","sabun muka"]
barang.pop(1)
print(barang)

#3
barang=["sampo","sabun","sabun muka"]
barang.sort()
print(barang)

barang=["sampo","sabun","sabun muka"]
barang.sort(reverse=True)
print(barang)

#4
barang=["sampo","sabun","sabun muka"]
barang.remove("sabun muka")
print(barang)

#5
barang=["sampo","sabun","sabun muka"]
barang.clear()
print(barang)
