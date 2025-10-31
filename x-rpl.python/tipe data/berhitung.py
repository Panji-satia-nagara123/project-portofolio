a = int(input("masukan angka pertama: "))
b = int(input("masukan angka kedua: "))
operator = input("masukan operator(+,-,*,/): ")

match operator:
    case "+":
        hasil = a + b
        print(f"hasil dari {a} + {b}= {hasil}")
    case "-":
        hasil= a-b
        print(f"hasil dari {a} - {b}= {hasil}")
    case "*":
        hasil= a*b
        print(f"hasil dari {a} * {b}= {hasil}") 
    case "/":
        if b !=0:
            hasil = a/b
            print(f"hasil dari {a} / {b}= {hasil}")
        else:
            print("error: pembagian dengan nol tidak bisa")
    case _ :
        print("operator tidak di kenal")