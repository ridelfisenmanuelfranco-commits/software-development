import os
from pyfiglet import Figlet

fig = Figlet(font="slant")
# ======================================================================================
# SISTEMA DE GESTION DE FARMACIA (VERSION 1.0)
# Proyecto heredado - Desarrollador anterior
# ======================================================================================

medicamentos = []
contador = 1


#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def mostrar_menu():
    print('=====================================================')
    print(fig.renderText("FARMACIA \nSAN MIGUEL"))
    print("""=====================================================
    [1] Registrar medicamento
    [2] Mostrar medicamentos
    [3] Buscar medicamento
    [4] Actualizar stock
    [5] Eliminar medicamento
    [6] Salir
=====================================================""")
    
    
#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def mostrar_categorias():
    print('''
    =======================================
                    CATEGORIAS
    =======================================
    [1] Analgesico.
    [2] Antibiotico.
    [3] Antiinflamatorio.
    [4] Vitamina.
    [5] Antialergico.
    [6] Otro.
    =======================================
    ''')

#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def obtener_categoria():
    while True:
        mostrar_categorias()
        
        try: 
            categoria = int(input('Elije una categoria: '))
        except ValueError:
            print('\n[ Categoria invalida. ]\n')
            continue
        
        os.system('clear')
        
        match categoria:
            case 1:
                return 'Analgesico'
            
            case 2:
                return 'Antibiotico'
            
            case 3: 
                return 'Antiinflamatorio'
            
            case 4:
                return 'Vitamina'
            
            case 5:
                return 'Antialergico'
            
            case 6: 
                return 'Otro'
            
            case _:
                print('\n[ Opcion invalida. ]\n')
    
                
#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def generar_codigo():
    global contador
    codigo = f"MED-{contador:03}"
    contador += 1
    return codigo



#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def obtener_texto(prompt):
    while True:
        dato = input(prompt).strip().title()
        if dato == "Salir":
            return None
        
        if dato == "":
            print('\n[ Valor invalido. ]\n')
            continue
        
        return dato
    
    
#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def obtener_dato_entero(prompt):
    while True:
        try:
            dato = int(input(prompt))
        except ValueError:
            print('\n[ Valor del dato ingresado invaliod ]\n')
            continue
        
        if dato <= 0:
            print('\n[ Valor invalido. ]\n')
            continue
        
        return dato
   
    
#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def obtener_dato_decimal(prompt):
    while True:
        try:
            dato = float(input(prompt))
        except ValueError:
            print('\n[ Valor del dato ingresado invaliod ]\n')
            continue
        
        if dato <= 0:
            print('\n[ Valor invalido. ]\n')
            continue
        
        return dato
    
    
#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def crear_medicamento(codigo,nombre,categoria,laboratorio,precio,stock,fecha_vencimiento):
    return {
        "Codigo": codigo,
        "Nombre": nombre,
        "Categoria": categoria,
        "Laboratorio": laboratorio,
        "Precio": precio,
        "Stock": stock,
        "Fecha": fecha_vencimiento
    }
    
    
#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def registrar_medicamento():
    existe = False
    nombre = obtener_texto("Nombre: ")
    if nombre is None:
        return
    
    laboratorio = obtener_texto("Laboratorio: ")
    if laboratorio is None:
        return 
    
    for medicamento in medicamentos:
        if medicamento['Nombre'] == nombre and medicamento['Laboratorio'] == laboratorio:
            existe = True
            break
        
    if existe:
        print(f'\n[ El medicamento [ {nombre} ] ya existe ]\n')
        return 
    
    
    categoria = obtener_categoria()
    stock = obtener_dato_entero('Ingrese la cantidad: ')

    precio = obtener_dato_decimal('Ingrese el precio: ')
    fecha = obtener_texto('Fecha de vencimiento: ')
    if fecha is None:
        return 
    
    medicamento = crear_medicamento(
        generar_codigo(),
        nombre,
        categoria,
        laboratorio,
        precio,
        stock,
        fecha
    )

    medicamentos.append(medicamento)
    print("\n[ Medicamento registrado. ]\n")


#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def mostrar_medicamento(i, m):
        print(f"""
        -----------------------------------
        {i+1}
        -----------------------------------
        Código      : {m['Codigo']}
        Nombre      : {m['Nombre']}
        Categoria   : {m['Categoria']}
        Laboratorio : {m['Laboratorio']}
        Precio      : {m['Precio']}
        Stock       : {m['Stock']}
        Fecha       : {m['Fecha']}
        -----------------------------------
        """)
        
        
#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def mostrar_medicamentos():
    if medicamentos:
        print('\n[ Listado de medicamentos. ]\n')
        for i, m in enumerate(medicamentos):
            mostrar_medicamento(i, m)
        
        if len(medicamentos) > 1:
            print(f'[ Hay {len(medicamentos)} medicamentos registrados. ]')
        
        else:
            print(f'[ Hay {len(medicamentos)} medicamento registrado. ]') 
        
    else:
        print('\n[ No hay medicamentos registrados. ]\n')
        
        
#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def buscar_codigo(codigo):
    for i,m in enumerate(medicamentos):
        if m["Codigo"] == codigo:
            return i, m
    return None,None

#----------------------------------------------------------------------------------
def buscar_medicamento():
    codigo = input("Código: ").strip().upper()
    i, m = buscar_codigo(codigo)
    
    if m:
        mostrar_medicamento(i, m)
        
    else:
        print("\n[ No encontrado. ]\n")
#----------------------------------------------------------------------------------
def actualizar_stock():
    codigo=input("Código: ").strip().upper()
    i,m =buscar_codigo (codigo)
    
    if m:
        mostrar_medicamento(i, m)
        cantidad = obtener_dato_entero("Nuevo stock: ")
        
    else:
        print("\n[ No encontrado. ]\n")
        return

    m["Stock"] = cantidad
    print("\n[ Stock actualizado. ]\n")


#---------------------------------------------------------------------------------------
def eliminar_medicamento():
    codigo=input("Código: ").strip().upper()
    i,m=buscar_codigo(codigo)
    if m:
        mostrar_medicamento(i, m)
        print('''
        =============================
            Esta seguro de 
            eliminar el medicamento
        =============================
        ''')
        respuesta = obtener_texto('(Si/No): ')
        if respuesta is None:
            return
        
        if respuesta == 'Si':
            medicamentos.remove(m)
            print("\n[ Eliminado. ]\n")
        elif respuesta == 'No':
            print('\n[ El medicamento no sera eliminado. ]\n')
            return 
        
        else:
            print('\n[ Dato invalido. ]\n')
            
    else:
        print("\n[ No encontrado. ]\n")
        
        
#---------------------------------------------------------------------------------------
while True:
    mostrar_menu()
    try:
        opcion = int(input("Elije una opcion: "))
    except ValueError:
        print('\n[ El valor invresado es invalido. ]\n')
        continue
    
    os.system('clear')
    if opcion == 1:
        registrar_medicamento()
        
    elif opcion == 2:
        mostrar_medicamentos()
        
    elif opcion == 3:
        buscar_medicamento()
        
    elif opcion == 4:
        actualizar_stock()
        
    elif opcion == 5:
        eliminar_medicamento()
        
    elif opcion == 6:
        print("\n[ Hasta luego. ]\n")
        break

    else:
        print('\n [ Opcion invalida. ]\n')