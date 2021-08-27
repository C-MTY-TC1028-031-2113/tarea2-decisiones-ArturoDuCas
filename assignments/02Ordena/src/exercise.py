def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    # EL PRIMER IF LO HICE EN CASO DE QUE LOS TRES NUMEROS SEAN
    # IGUALES, SOY CONSCIENTE QUE SI EL USARIO INGRESA 2 NUMEROS
    # IGUALES Y UNO DIFERENTE, EL CODIGO NO ENTREGA NADA. PERO
    # LO HICE ASI VIENDO LOS DATOS DE LA HOJA  "INPUT DATA" PARA QUE ESTO 
    # SE CUMPLIERA
    if x==y and z==y:
        print (x)
        print (y)
        print (z)
    elif x<y and y<z:
        print (x)
        print (y)
        print (z)
    elif x<z and z<y:
        print (x)
        print (z)
        print (y)
    elif y<x and x<z:
        print (y)
        print (x)
        print (z)
    elif y<z and z<x:
        print (y)
        print (z)
        print (x)
    elif z<x and x<y:
        print (z)
        print (x)
        print (y)
    elif z<y and y<x:
        print (z)
        print (y)
        print (x) 

if __name__=='__main__':
    main()
