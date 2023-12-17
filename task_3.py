inp = int(input("Son kiriting: "))
massiv = [10, 7, 3, 5]
massiv2 = []

def procent(input, msv1, msv2):
    for num in msv1:
        result = input / 100 * num
        msv2.append(result)

    print(msv2)


procent(input=inp, msv1=massiv, msv2=massiv2)