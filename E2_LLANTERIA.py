# INICIO 
print()
print('=== OFERTA DE LLANTAS ===')
print('=========================')
print()

# LECTURA
Cant=float(input('INGRESE LA CANTIDAD DE LLANTAS >>> '))

#PROCESO
if(Cant>=5):
    Precio=Cant*120
    print()
    print('EL PRECIO A PAGAR ES S/.', Precio,'Soles' )
    print()
if(Cant<5):
    Precio=Cant*150
    print()
    print('EL PRECIO A PAGAR ES S/.', Precio, 'Soles')
    print()
# FIN
