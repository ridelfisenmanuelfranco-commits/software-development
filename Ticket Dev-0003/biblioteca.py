# =============================================================================================================
#                                   SISTEMA DE GESTION DE BIBLIOTECA
# =============================================================================================================
import os
# =============================================================================================================
#                                           DATOS DEL SISTEMA
# =============================================================================================================
libros = [
    {
        "Codigo": "LIB-001",
        "Titulo": "Cien Años De Soledad",
        "Autor": "Gabriel García Márquez",
        "Editorial": "Sudamericana",
        "Anio": 1967,
        "Genero": "Realismo Mágico",
        "Cantidad": 8,
        "Estado": "Disponible"
    },
    {
        "Codigo": "LIB-002",
        "Titulo": "Don Quijote De La Mancha",
        "Autor": "Miguel De Cervantes",
        "Editorial": "Francisco De Robles",
        "Anio": 1605,
        "Genero": "Novela",
        "Cantidad": 5,
        "Estado": "Disponible"
    },
    {
        "Codigo": "LIB-003",
        "Titulo": "El Principito",
        "Autor": "Antoine De Saint-Exupéry",
        "Editorial": "Reynal & Hitchcock",
        "Anio": 1943,
        "Genero": "Infantil",
        "Cantidad": 12,
        "Estado": "Prestado"
    },
    {
        "Codigo": "LIB-004",
        "Titulo": "1984",
        "Autor": "George Orwell",
        "Editorial": "Secker & Warburg",
        "Anio": 1949,
        "Genero": "Ciencia Ficción",
        "Cantidad": 6,
        "Estado": "Prestado"
    },
    {
        "Codigo": "LIB-005",
        "Titulo": "Hábitos Atómicos",
        "Autor": "James Clear",
        "Editorial": "Penguin Random House",
        "Anio": 2018,
        "Genero": "Desarrollo Personal",
        "Cantidad": 15,
        "Estado": "Disponible"
    }
]
contador_libros = len(libros) + 1

# =============================================================================================================
#                                               MENU DEL SISTEMA
# =============================================================================================================
def mostrar_menu():
    print('''
    ===================================  
    | Biblioteca Instituto San Marcos |
    ===================================
    |               MENU              |
    ===================================
    [1] Registrar libro.
    [2] Mostrar libro.
    [3] Buscar libro por codigo.
    [4] Actualizar libro.
    [5] Eliminar libro.
    [6] Estadisticas
    [7] Salir
    ===================================
    ''')

# =============================================================================================================
#                                          GENERADOR DE CODIGO DEL LIBRO
# =============================================================================================================
def generar_codigo_libro():
    global contador_libros
    
    codigo_libro = f'LIB-{contador_libros:03}'
    contador_libros += 1
    
    return codigo_libro

# =============================================================================================================
#                                               OBTENER TEXTO
# =============================================================================================================
def obtener_texto(prompt):
    while True:
        dato = input(prompt).strip().title()
        
        if dato == 'Salir':
            return None
        
        if dato == "":
            print('\n[ El valor ingresado es invalido. ]\n')
            continue
        
        return dato

# =============================================================================================================
#                                           OBTENER ENTERO
# =============================================================================================================
def obtener_entero(prompt):
    while True:
        try:
            dato = int(input(prompt))
            
        except ValueError:
            print('\n[ El dato ingresado no es valido. ]\n')
            continue
        
        if dato <= 0:
            print('\n[ Valor del dato invalido. ]\n')
            continue
        
        return dato
        
# =============================================================================================================
#                                       CREAR ESTRUCTURA DEL LIBRO
# =============================================================================================================
def crear_libro(codigo_libro,
               titulo_libro,
               autor_libro,
               editorial_libro,
               anio_publicacion,
               genero_libro,
               cantidad_libro,
               estado_libro):
    return {
        'Codigo': codigo_libro,
        'Titulo': titulo_libro,
        'Autor': autor_libro,
        'Editorial': editorial_libro,
        'Anio': anio_publicacion,
        'Genero': genero_libro,
        'Cantidad': cantidad_libro,
        'Estado': estado_libro
    }

# =============================================================================================================
#                                             REGISTRAR LIBRO
# =============================================================================================================
def registrar_libro():
    print('\n[ Registro de libro en proceso. ]\n')
    existe = False
    
    titulo_libro = obtener_texto('Ingresa el titulo del libro: ')
    if titulo_libro is None:
        return 
    
    for libro in libros:
        if libro['Titulo'] == titulo_libro:
            existe = True
            break
        
    if existe:
        print(f'\nEl libro: {titulo_libro}, ya existe en la biblioteca.\n')
        return 
    
    autor_libro = obtener_texto('Ingrese el autor del libro: ')

    if autor_libro is None:
        return 
    
    editorial_libro = obtener_texto('Ingrese el editorial del libro: ')
    if editorial_libro is None:
        return 
    
    anio_publicacion = obtener_entero('Ingrese el anio de publicacion del libro: ')
    
    genero_libro = obtener_texto('Ingrese el genero del libro: ')
    if genero_libro is None:
        return
    
    cantidad_libro = obtener_entero('Ingrese la cantidad disponible del libro: ')

    codigo_libro = generar_codigo_libro()
    
    libro = crear_libro(codigo_libro,
                        titulo_libro,
                        autor_libro,
                        editorial_libro,
                        anio_publicacion,
                        genero_libro,
                        cantidad_libro,
                        estado_libro = 'Disponible')
    
    libros.append(libro)
    print('\n[ Libro registrado correctamente. ]\n')

# =============================================================================================================
#                                               MOSTRAR LIBRO
# =============================================================================================================
def mostrar_libro(i, libro):
    print(f'''
    {i + 1}
    ======================================
    |                LIBRO               |
    ======================================
    Codigo      :   {libro['Codigo']}
    Titulo      :   {libro['Titulo']}
    Autor       :   {libro['Autor']}
    Editorial   :   {libro['Editorial']}
    Anio        :   {libro['Anio']}
    Genero      :   {libro['Genero']}
    Cantidad    :   {libro['Cantidad']}
    Estado      :   {libro['Estado']}
    ======================================
    ''')


# =============================================================================================================
#                                           MOSTRAR LIBROS
# =============================================================================================================
def mostrar_libros():
    if libros:
        print('\n[ Listado de libros. ]\n')
        for i, libro in enumerate(libros):
            mostrar_libro(i, libro)
        
        if len(libros) > 1:
            print(f'[ Hay {len(libros)} libros registrados. ]')
        
        else:
            print(f'[ Hay {len(libros)} libro registrado. ]') 
        
    else:
        print('\n[ No hay libros registrados. ]\n')

# =============================================================================================================
#                                               BUSCAR CODIGO
# =============================================================================================================
def buscar_codigo(codigo):
    for i, libro in enumerate(libros):
        if libro['Codigo'] == codigo:
            return i, libro
    
    return None, None

# =============================================================================================================
#                                       BUSCAR LIBRO POR EL CODIGO
# =============================================================================================================
def buscar_libro_codigo():
    codigo_libro = input('Ingrese el codigo del libro a buscar: ').strip().upper()
    i, libro = buscar_codigo(codigo_libro)
    
    if libro:
        mostrar_libro(i, libro)
    
    else:
        print('\n[ El libro no existe ]\n')


# =============================================================================================================
#                                ACTUALIZACION DE INFORMACION DE LIBROS
# =============================================================================================================
def actualizar_libro():
    print('\n[Actualizacion de datos del libro.]\n')
    codigo_libro = input('Ingrese el codigo del libro a buscar: ').strip().upper()
    i, libro = buscar_codigo(codigo_libro)
    
    if libro:
        mostrar_libro(i, libro)
        while True:
            print('''
            =====================================
            |  BIBLIOTECA INSTITUTO SAN MARCOS  |
            =====================================
            |  ->   Que desea actualizar   <-   |
            =====================================
            [1] Editorial del libro.
            [2] Genero del libro.
            [3] Cantidad disponible.
            [4] Salir
            =====================================
            ''')
            try:
                opcion = int(input('Elije una opcion: '))
            
            except ValueError:
                print('\n[Tipo de dato invalido]\n')
                continue
            
            os.system('clear')
            match opcion:
                
                case 1:
                    print('\n[Actualizando editorial del libro]\n')
                    nuevo_editorial_libro = obtener_texto('Ingrese el nuevo editorial del libro: ')
                    if nuevo_editorial_libro is None:
                        return 
                    
                    libro['Editorial'] = nuevo_editorial_libro
                    break
                
                case 2:
                    print('\n[Actualizando genero del libro]\n')
                    nuevo_genero_libro = obtener_texto('Ingrese el nuevo genero del libro: ')
                    if nuevo_genero_libro is None:
                        return 
                    
                    libro['Genero'] = nuevo_genero_libro
                    break
                
                case 3:
                    print('\n[Actualizando Cantidad del libro]\n')
                    nueva_cantidad_libro = obtener_entero('Ingrese la nuevo cantidad del libro: ')
                    
                    if nueva_cantidad_libro is None:
                        return 
                    
                    libro['Cantidad'] = nueva_cantidad_libro
                    break
                
                case _:
                    print('\nOpcion invalida.\n')
    else:
        print('\n[El libro no existe.]\n')
# =============================================================================================================
#                                               ELIMINAR LIBRO
# =============================================================================================================
def eliminar_libro():
    print('\n[Eliminacion de  libro.]\n')
    codigo_libro = input('Codigo del libro a buscar: ').strip().upper()
    
    i, libro = buscar_codigo(codigo_libro)
    
    if libro:
        mostrar_libro(i, libro)
        if libro['Estado'] == 'Prestado':
            print(f'\n[El libro: [ {libro["Titulo"]} ] esta prestado, no se puede eliminar.]\n')
            return
        
        else:
            libros.remove(libro)
            print(f'\n[El libro [ {libro["Titulo"]} ] ha sido eliminado correctamente.]\n')
            
    else:
        print('\n[El libro no existe.]\n')
        
# =============================================================================================================
#                                   ESTADISTICAS DE LA BIBLIOTEACA
# =============================================================================================================
def estadisticas():
    if libros:
        total = len(libros)
        total_ejemplares = 0
        libros_disponibles = 0
        libros_prestados = 0
        generos = {}
        
        for libro in libros:
            total_ejemplares += libro['Cantidad']
            
            if libro['Estado'] == 'Disponible':
                libros_disponibles += 1
                
            else:
                libros_prestados += 1
            
            genero = libro['Genero']
            
            if genero not in generos:
                generos[genero] = 1
            
            else:
                generos[genero] += 1
        
        mayor = 0
        genero_mayor = ''
        
        for genero, cantidad in generos.items():
            if cantidad > mayor:
                mayor = cantidad
                genero_mayor = genero
        
        print(f'''
        ============================================
        |       ESTADISTICAS DE LA BIBLIOTECA      |
        ============================================
        Total de libros        :   {total}
        Total de ejemplares    :   {total_ejemplares}
        Libros disponibles     :   {libros_disponibles}
        Libros prestados       :   {libros_prestados}
        Género con más libros  :   {genero_mayor}
        ============================================
        ''')
    
    else:
        print('\n[No hay libros registrados]\n')

# =============================================================================================================
# 
# =============================================================================================================
while True:
    mostrar_menu()
    
    try:
        opcion = int(input('Elije una opcion: '))
    
    except ValueError:
        print('\n[ Dato invalido. ]\n')
        continue
    
    os.system('clear')
    
    match opcion:
        case 1:
            registrar_libro()
        
        case 2:
            mostrar_libros()
            
        case 3:
            buscar_libro_codigo()
            
        case 4:
            actualizar_libro()
        
        case 5:
            eliminar_libro()
        
        case 6:
            estadisticas()
             
        case 7:
            print('\n[ Saliendo del sistema. ]\n')
            break

        case _:
            print('\nOpcion invalida.\n')





# =============================================================================================================
# 
# =============================================================================================================
# print('''
#     ===================================  
#     | Biblioteca Instituto San Marcos |
#     ===================================
#     |               MENU              |
#     ===================================
#     [6] Registrar prestamo.
#     [7] Registrar devolucion.

#     ===================================
#     ''')





# =============================================================================================================
# 
# =============================================================================================================





# =============================================================================================================
# 
# =============================================================================================================






# =============================================================================================================
# 
# =============================================================================================================





# =============================================================================================================
# 
# =============================================================================================================





# =============================================================================================================
# 
# =============================================================================================================






