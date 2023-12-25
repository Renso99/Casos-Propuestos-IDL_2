# INICIO 
print()
print('=== DETERMINAR SI EL TRIANGULO ES - "EQUILATERO" - "ISOSCELES" - "ESCALENO" ===')
print('===============================================================================')
print()

# LECTURA
A=int(input('INGRESE LADO A >>> '))
B=int(input('INGRESE LADO B >>> '))
C=int(input('INGRESE LADO C >>> '))

# VALIDACION
if(((A+B)>C and (A+C)>B and (B+C)>A)):

    #PROCESO
    S=(A+B+C)/2
    if(A==B==C):
        Area=round((S*(S-A)*(S-B)*(S-C)**(1/2)),2)
        print()
        print('>>> ES UN TRIANGULO ::: EQUILATERO <<<')
        print('>>>     Y SU AREA ES >>>', Area , '<<<')
        print()
    elif(A>B>C or A<B<C):
        Per=A+B+C
        print('>>>  ES UN TRIANGULO ::: ESCALENO  <<<')
        print('>>> Y SUS PERIMETO ES :::', Per , '<<<')
        print()
    else:
        if(A==B and A!=C):
            print('>>>  ES UN TRIANGULO ::: ISOSCELES  <<<')
            print('>>> Y SUS LADOS IGUALES SON ::: A y B <<<')
        elif(B==C):
            print('>>>  ES UN TRIANGULO ::: ISOSCELES  <<<')
            print('>>>  Y SUS LADOS IGUALES SON ::: B y C <<<')
        else:
            print('>>>  ES UN TRIANGULO ::: ISOSCELES  <<<')
            print('>>>  Y SUS LADOS IGUALES SON ::: A y C <<<')
else:
    print()
    print('>>> LOS LADOS NO CORRESPPONDEN A NINGUN TRIANGULO <<<')
    print()
# FIN
