def Menu():
    print ("""
*********************
        Calculadora
*********************
    Operador
        1) Suma
        2) Resta
        3) Multiplicacion
        4) Division
        5) Salir""")

def suma ():
    n1 = float(input("Ingrese sumando 1 "))
    n2 = float(input("Ingrese sumando 2 "))
    res=n1+n2
    print ("Resultado: ", round(res,4))

def resta ():
    n1 = float(input("Ingrese minuendo "))
    n2 = float(input("Ingrese sustraendo "))
    res=n1-n2
    print ("Resultado: ", round((res),4))

def multiplica ():
    n1 = float(input("Ingrese multiplicando "))
    n2 = float(input("Ingrese multiplicador "))
    res=n1*n2
    print ("Resultado: ", round((res),4))

def divide ():
    n1 = float(input("Ingrese Dividendo "))
    n2 = float(input("Ingrese Divisor "))
    if n2==0:
        print("No se permite dividir entre cero")
    else:
        res=n1/n2
        print ("Resultado ", round((res),4))


def calculadora():
    Menu()
    opc=int(input("Seleccione Operador\n"))
    while (opc >0 and opc <5):
        if (opc==1):
            suma()
            opc=int(input("Seleccione Operador\n"))
        elif(opc==2):
            resta()
            opc=int(input("Seleccione Operador\n"))
        elif(opc==3):
            multiplica()
            opc=int(input("Seleccione Operador\n"))
        elif(opc==4):
            divide()
            opc=int(input("Seleccione Operador\n"))
            

calculadora()

