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
#                               MOSTRAR MENU
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
#                                       MOSTRAR CATEGORIAS
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
#                                  OBTENER CATEGORIA
#---------------------------------------------------------------------------------------
def obtener_categoria():
    while True:
        mostrar_categorias()
        
        try: 
            categoria = int(input('Elije una categoria: '))
        except ValueError:
            print('\n[ Categoria invalida. ]\n')
            continue
        
        os.system("cls") 
        
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
#                           OBTENER CODIGO DEL MEDICAMENTO
#---------------------------------------------------------------------------------------
def generar_codigo():
    global contador
    codigo = f"MED-{contador:03}"
    contador += 1
    return codigo



#---------------------------------------------------------------------------------------
#                                   OBTENER DATO DE TIPO TEXTO
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
#                       OBTENER DATO DE SI ES CON RECETA MEDICA
#---------------------------------------------------------------------------------------
def con_receta_medica():
    while True:
        con_receta = obtener_texto('Necesita receta medica para despachar: ')

        if con_receta != 'Si' and con_receta != 'No':
            print('\n[ Dato ingresado invalido. ]\n')
            continue

        return con_receta
    
#---------------------------------------------------------------------------------------
#                                   OBTENER DATO DE TIPO ENTERO
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
#                       OBTENER DATO DE TIPO FLOAT
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
#                                   CREAR MEDICAMENTO
#---------------------------------------------------------------------------------------
def crear_medicamento(codigo,nombre,categoria,laboratorio,receta,precio,stock,fecha_vencimiento):
    return {
        "Codigo": codigo,
        "Nombre": nombre,
        "Categoria": categoria,
        "Laboratorio": laboratorio,
        "Receta" : receta,
        "Precio": precio,
        "Stock": stock,
        "Fecha": fecha_vencimiento
    }
    
    
#---------------------------------------------------------------------------------------
#                                REGISTRAR UN MEDICAMENTO
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
    
    receta = con_receta_medica()

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
        receta,
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
        Receta      : {m['Receta']}
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
#                           BUSCAR MEDICAMENTO POR CODIGO
#---------------------------------------------------------------------------------------
def buscar_codigo_nombre(dato):
    for i,m in enumerate(medicamentos):
        if m["Codigo"] == dato or  m["Nombre"] == dato:
            return i, m
    return None,None

#---------------------------------------------------------------------------------------
#                          MOSTRAR SUBMENU PARA BUSCAR MEDICAMENTO
#---------------------------------------------------------------------------------------
def mostrar_submenu():
    print('''
    ==============================
          BUSCAR MEDICAMENTOS
    ==============================
    [1] Codigo.
    [2] Nombre.
    [3] Salir.
    ==============================
    ''')
#---------------------------------------------------------------------------------------
#                               BUSCAR MEDICAMENTO
#---------------------------------------------------------------------------------------
def buscar_medicamento():
    while True:
        mostrar_submenu()

        try:
            opcion = int(input('Elija una opcion: '))

        except ValueError:
            print('\n[ EL DATO INGRESADO ES INVALIDO. ]\n')
            continue

        os.system("cls")

        if opcion == 1:
            codigo = input("Código: ").strip().upper()
            i, m = buscar_codigo_nombre(codigo)
            
            if m:
                mostrar_medicamento(i, m)
            else:
                print("\n[ No encontrado. ]\n")

        elif opcion == 2:
            nombre = input("Nombre: ").strip().title()
            i, m = buscar_codigo_nombre(nombre)
                        
            if m:
                mostrar_medicamento(i, m)
            else:
                print("\n[ No encontrado. ]\n")

        elif opcion == 3:
            print('\n[ SALIENDO DE LA OPCION BUSCAR MEDICAMENTO. ]\n')
            break

        else:
            print('\n[ OPCION INVALIDA. ]\n')

#---------------------------------------------------------------------------------------
#                                   ACTUALIZAR STOCK
#---------------------------------------------------------------------------------------
def actualizar_stock():
    codigo=input("Código: ").strip().upper()
    i,m = buscar_codigo_nombre(codigo)
    
    if m:
        mostrar_medicamento(i, m)
        cantidad = obtener_dato_entero("Nuevo stock: ")
        
    else:
        print("\n[ No encontrado. ]\n")
        return

    m["Stock"] = cantidad
    print("\n[ Stock actualizado. ]\n")


#---------------------------------------------------------------------------------------
# 
#---------------------------------------------------------------------------------------
def eliminar_medicamento():
    codigo=input("Código: ").strip().upper()
    i, m= buscar_codigo_nombre(codigo)
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
        
        
#-------------------#---------------------------------------------------------------------------------------
# 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    mostrar_menu()
    try:
        opcion = int(input("Elije una opcion: "))
    except ValueError:
        print('\n[ El valor invresado es invalido. ]\n')
        continue
    
    os.system("cls")
    
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