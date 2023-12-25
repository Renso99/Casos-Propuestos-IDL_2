# INICIO 
print()
print('=== TRIBUTACION ===')
print('===================')
print()

# LECTURA
Edad=int(input('INGRESE SU EDAD >>> '))
Ingresos=float(input('INGRESE SU SALARIO MENSUAL s/.>>> '))

# VALIDACION
if(Edad>0 and Ingresos>0):

    #PROCESO
    if(Edad>=16 and Ingresos>=4000):
        print()
        print('>>> PAGA SUS TRIBUTOS <<<')
        print()
    else:
        print()
        print('>>> NO PAGA TRIBUTOS !!!')
        print()
else:
   print()
   print('>>> ERROR ::: DATOS no validos !!!')
   print()
    
# FIN
