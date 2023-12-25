# INICIO 
print()
print('=== HORA ===')
print('============')
print()

# LECTURA
Hora=int(input('INGRESE LA HORA >>> '))
Minutos=int(input('INGRESE LOS MINUTOS >>> '))
Segundos=int(input('INGRESE LOS SEGUNDOS>>> '))

# VALIDACION
if(Hora>=0  and  Hora<=23  and  Minutos>=0  and  Minutos<=59 and Segundos>=0 and Segundos<=59):

    #PROCESO
    Segundos=Segundos+1
    if(Segundos == 60):
        Segundos = 0
        Minutos = Minutos + 1
        
        if(Minutos == 60):
            Minutos = 0
            Hora = Hora + 1
            
            if(Hora==24):
                Hora = 0
    print(f'UN SEGUNDO DESPUES DE LA HORA INGRESADA ES ::: {Hora} : {Minutos} : {Segundos}')
    print()
        
else:
    print()
    print('>>> ERROR ::: HORA incorrecta !!! <<<')
    print()
# FIN