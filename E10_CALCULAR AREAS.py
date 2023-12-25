# INICIO 
print()
print('=== CALCULAR AREAS ===')
print('======================')
print()

# LECTURA
Opcion=int(input('\n MENU \n'+
"1. CALCULAR AREA DEL CUADRADO\n"+
"2. CALCULAR AREA DEL CIRCULO\n"+
"3. CALCULAR AREA DE TRIANGULO\n"+
"4. SALIR\n"+
"ELEGIR OPCION >>> "))

#PROCESO

if(Opcion ==1):
    LadoCuadrado=int(input('INGRESE EL LADO DEL CUADRADO >>> '))
    AreaCuadrado=LadoCuadrado*4
    print(('>>> EL AREA DEL CUADRADO ES>>> ', AreaCuadrado))

if(Opcion ==2):
    Radio=int(input('INGRESE EL EL RADIO DEL CIRCULO >>> '))
    AreaCirculo=3.14*pow(Radio,2)
    print(('>>> EL AREA DEL CIRCULO ES >>> ', AreaCirculo))

if(Opcion ==3):
    Altura=int(input('INGRESE LA ALTURA DEL TRIALGULO >>> '))
    Base=int(input('INGRESE LA BASE DEL TRIANGULO >>> '))
    AreaTriangulo=(Base*Altura)/2
    print(('>>> EL AREA DEL TRIANGULO ES>>> ', AreaTriangulo))

if(Opcion ==4):
    print(">>> ELIGIO SALIR :::: GRACIAS ::: Adios::: <<<")
    print()

# FIN