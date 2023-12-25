# INICIO 
print()
print('=== UTILIDADES DE UN TRABAJADOR ===')
print('============')
print()

# LECTURA
Salario=int(input('SALARIO MENSUAL >>> '))
TiempoServ=int(input('CUANTOS AÑOS DE SERVICIO:::\n Opcion 1 = Menos de 1 año,\n Opcion 2 = 1 a 2 años,\n Opcion 3 = 2 a 5 años,\n Opcion 4 = 5 a 10 años,\n Opcion 5 = 10 años a mas>>> '))

# VALIDACION
if(TiempoServ==1 or TiempoServ==2 or TiempoServ==3 or TiempoServ==4 or TiempoServ==5):

    #PROCESO
    if(TiempoServ==1):
        print('>>> TE CORRESPONDE UN ADICIONAL DEL 5 % ')
        NuevoValor=Salario*0.05
        Utilidades=Salario*NuevoValor
        print('>>> LA UTILIDAD ANUAL DEL TRABAJOR SERA DE :::S/.', Utilidades,'soles')
    if(TiempoServ==2):
        print('>>> TE CORRESPONDE UN ADICIONAL DEL 7 % ')
        NuevoValor=Salario*0.07
        Utilidades=Salario*NuevoValor
        print('>>> LA UTILIDAD ANUAL DEL TRABAJOR SERA DE :::S/.', Utilidades,'soles')
    if(TiempoServ==3):
        print('>>> TE CORRESPONDE UN ADICIONAL DEL 10 % ')
        NuevoValor=Salario*0.1
        Utilidades=Salario*NuevoValor
        print('>>> LA UTILIDAD ANUAL DEL TRABAJOR SERA DE :::S/.', Utilidades,'soles')
    if(TiempoServ==4):
        print('>>> TE CORRESPONDE UN ADICIONAL DEL 15 % ')
        NuevoValor=Salario*0.15
        Utilidades=Salario*NuevoValor
        print('>>> LA UTILIDAD ANUAL DEL TRABAJOR SERA DE :::S/.', Utilidades,'soles')
    if(TiempoServ==5):
        print('>>> TE CORRESPONDE UN ADICIONAL DE 20 % ')
        NuevoValor=Salario*0.2
        Utilidades=Salario*NuevoValor,2
        print('>>> LA UTILIDAD ANUAL DEL TRABAJOR SERA DE :::S/.', Utilidades,'soles')
    
else:
    print()
    print('>>> ERROR ::: OPCION incorrecta !!! <<<')
    print()
# FIN