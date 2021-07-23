def exchanges(moneda, cantidad):
    result = 0
    #Moneda Euro
    if moneda == 1: 
        result = cantidad * 1.18
        print(f"{cantidad} euros equivalen a {result} dolares ")
    #Moneda Bitcoint
    elif moneda == 2:
        result = cantidad * 15635.60 
        print (f"{cantidad} bitcoins equivalen a {result} dolares ")
    #Moneda China
    elif moneda == 3:
        result = cantidad * 0.15
        print (f"{cantidad} yuanes equivalen a {result}" )
    #Otro
    else: 
        print("Ingresa solo un numero de la lista ")

    
if __name__ == "__main__" :
    try:
        moneda = int(input("""
        Ingresa el inidice de la moneda que quieres converir a dolares:
            [1] Moneda euro a dolar
            [2] Moneda bitcoin a dolar
            [3] Moneda yuan a dolar
        Seleciona:"""))
        print("*************************")
        cantidad = int(input("Ingresa la cantidad que quieres convetir"))
        exchanges(moneda, cantidad)
    except:
        print("****ERROR****")
        print("Por favor, Ingrese solo valores numericos")
