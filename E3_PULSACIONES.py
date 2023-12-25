# INICIO 
print()
print('=== PULSACIONES ===')
print('===================')
print()

# LECTURA
Genero=input('INGRESE SU GENERO (M/F) >>> ').upper()
Edad=int(input('INGRESE SU EDAD >>> '))

#PROCESO
if(Genero=="M" or Genero=="F"):
    if(Genero=="M"):
        Pulsaciones=(210-Edad)/10
        G='MASCULINO'
    else:
        Pulsaciones=(220-Edad)/10
        G='FMENINO'
    # SALIDA
    print()
    print(f'Las Pulsaciones del Genero {G} es de {Pulsaciones} por cada 10 Segundos')
    print()
else:
    print()
    print('>>> ERROR:::DATOS no validos !!!')
    print()
    
# FIN
