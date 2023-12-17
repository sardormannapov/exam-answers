lst = [10, 5, 3, 4, 2, 8, 6, 9, 1]
lst2 = []

def search(massiv1, massiv2):
    for num in range(1, 11):
        if num not in massiv1:
            massiv2.append(num)
            print(massiv2)


search(massiv1=lst, massiv2=lst2)
