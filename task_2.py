people = int(input("Odamlar sonini kiriting: "))
odam = 5

def car(people, odam):
        result = people // odam
        print(f"{result} moshina {people} odamga kerak")


car(people=people, odam=odam)