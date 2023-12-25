# INICIO 
print()
print('=== PAGO DE LA COLEGIATURA ===')
print('==============================')
print()

# LECTURA
CantM=int(input('INGRESE LA CANTIDAD DE MATERIAS A LLEVAR >>> '))
Promedio=int(input('INGRESE SU PROMEDIO OBTENIDO >>> ')) 

# VALIDACION
if(Promedio>0 and Promedio<=20):

    #PROCESO
    Pago=CantM*150
    if(Promedio>=17):
        Desc=Pago*0.30
        PagoTotal=Pago-Desc
        D=30
        print()
        print('EL PAGO POR TODAS LAS MATERIAS ES DE >>> S/.', Pago, 'soles')
        print(f'EL DESCUENTO ES {D} %                 >>> S/.', Pago*(D/100),'soles')
        print('EL PAGO TOTAL ES                     >>> S/.', PagoTotal,'soles')
        print()
    else:
        print()
        print('EL PAGO TOTAL ES S/.', Pago)
        print()
else:
    print()
    print('>>> ERROR ::: NOTA no valida !!!')
    print()
# FIN
