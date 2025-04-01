# types of number

def inputValues():
    entero = input("Numero entero: ")
    if(type(entero) == str):
        print("error")
    decimal = input("Numero flotante: ")
    sum(entero,decimal)


def sum(entero,decimal):
    result = int(entero) + float(decimal)
    print("->",result)
    if(type(result) == float):
        print("Es un flotante!")
    elif(type(result) == int):
        print("Es un entero!")
    else:
        print("No es un numero!")
        return
    
inputValues()

