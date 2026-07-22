import os
# ==============================================================================================
#                               SISTEMA DE GESTION DE PELICULAS  
# ==============================================================================================

# ==============================================================================================
#                                            DATOS            
# ==============================================================================================
peliculas = []
contador_pelicula = len(peliculas) + 1

# ==============================================================================================
#                                           MOSTRAR MENU            
# ==============================================================================================
def mostrar_menu():
    print('''
    ===============================
         SISTEMA DE PELICULAS
    ===============================
    [1]  Registrar Pelicula.
    [2]  Mostrar Peliculas.
    [3]  Buscar Pelicula.
    [4]  Actualizar Pelicula.
    [5]  Eliminar Pelicula.
    [6]  Mostrar Estadisticas.
    [7]  Salir.
    ===============================
    ''')
    
    
    
# ==============================================================================================
#                                    OBTENER CODIGO DE LA PELICULA            
# ==============================================================================================
def obtener_codigo_pelicula():
    global contador_pelicula
    
    codigo_pelicula = f'PEL-{contador_pelicula:03}'
    contador_pelicula += 1
    
    return codigo_pelicula

# ==============================================================================================
#                                           OBTENER DATO            
# ==============================================================================================
def obtener_dato(dato):

    if dato == 'Salir':
        return None
        
    if dato == "":
        print('Titulo de la pelicula invalido.')
        return False
    
    return dato

# ==============================================================================================
#                                  OBTENER TITULO DE LA PELICULA                   
# ==============================================================================================
def obtener_titulo_pelicula():
    while True:
        titulo_pelicula = input('Titulo de la pelicula: ').strip().title()
        resultado = obtener_dato(titulo_pelicula)
        
        if resultado is False:
            continue
        
        return resultado
    
# ==============================================================================================
#                                  OBTENER GENERO DE LA PELICULA                   
# ==============================================================================================
def obtener_genero_pelicula():
    while True:
        genero_pelicula = input('Genero de la pelicula: ').strip().title()
        resultado = obtener_dato(genero_pelicula)
        
        if resultado is False:
            continue
        
        return resultado



# ==============================================================================================
#                                  OBTENER ANIO DE LA PELICULA                   
# ==============================================================================================
def obtener_anio_pelicula():
    while True:
        try:
            anio_pelicula = int(input('Anio de la pelicula: '))
        
        except ValueError:
            print('Dato invalido.')
            continue
        
        if anio_pelicula < 1900:
            print('\nEl anio de la pelicula es incorrecto\n')
            continue
        
        return anio_pelicula
# ==============================================================================================
#                                  OBTENER CANTIDAD DE LA PELICULA                   
# ==============================================================================================
def obtener_cantidad_pelicula():
    while True:
        try:
            cantidad_pelicula = int(input('Cantidad de la pelicula: '))
        
        except ValueError:
            print('\nLa cantidad de la pelicula es invalida.\n')
            continue
        if cantidad_pelicula > 0:
            return cantidad_pelicula
        
        else:
            print('\nCantidad invalida.\n')
            continue
        
# ==============================================================================================
#                                           CREAR PELICULA                   
# ==============================================================================================
def crear_pelicula(codigo_pelicula,
                   titulo_pelicula,
                   genero_pelicula,
                   anio_pelicula,
                   cantidad_pelicula):
    return {
        'Codigo': codigo_pelicula,
        'Titulo': titulo_pelicula,
        'Genero': genero_pelicula,
        'Anio': anio_pelicula,
        'Cantidad': cantidad_pelicula
    }
    

# ==============================================================================================
#                                          AGREGAR PELICULA                   
# ==============================================================================================
def agregar_pelicula():
    print('\nAgregando Pelicula.\n')
    existe = False
    
    codigo_pelicula = obtener_codigo_pelicula()
    for pelicula in peliculas:
        if pelicula['Codigo'] == codigo_pelicula:
            existe = True
            break
        
    if existe:
        print('\nLa pelicula ya existe en la cartelera.\n')
        return
    
    titulo_pelicula = obtener_titulo_pelicula()
    if titulo_pelicula is None:
        return
    
    for pelicula in peliculas:
        if pelicula['Titulo'] == titulo_pelicula:
            existe = True
            break
        
    if existe:
        print('\nLa pelicula ya existe en la cartelera.\n')
        return
    genero_pelicula = obtener_genero_pelicula()
    if genero_pelicula is None:
        return
    
    anio_pelicula = obtener_anio_pelicula()
    cantidad_pelicula = obtener_cantidad_pelicula()

    pelicula = crear_pelicula(codigo_pelicula,
                              titulo_pelicula,
                              genero_pelicula,
                              anio_pelicula,
                              cantidad_pelicula)
    
    peliculas.append(pelicula)
    print('\nPelicula agregada correctamente.\n')


# ==============================================================================================
#                                       MOSTRAR PELICULA                   
# ==============================================================================================
def mostrar_pelicula(i, pelicula):
    print(f'''
    
    ========================================
                Pelicula        {i+1}
    ========================================
    Codigo     :   {pelicula['Codigo']}
    Titulo     :   {pelicula['Titulo']}
    Genero     :   {pelicula['Genero']}
    Anio       :   {pelicula['Anio']}
    Cantidad   :   {pelicula['Cantidad']}
    ========================================
    ''')


# ==============================================================================================
#                                  MOSTRAR PELICULAS                   
# ==============================================================================================
def mostrar_peliculas():
    if peliculas:
        for i, pelicula in enumerate(peliculas):
            mostrar_pelicula(i, pelicula)
            
        print(f'Tenemos {len(peliculas)} peliculas en caltelera.\n')   
        
    else:
        print('\nNo hay peliculas registradas\n')

        
# ==============================================================================================
#                                  BUSCAR PELICULA POR CODIGO                 
# ==============================================================================================
def buscar_pelicula_por_codigo():
    if peliculas:
        print('\nBuscador de pelicula.\n')
        encontrada = False
        codigo = input('Codigo de la pelicula: ').strip().upper()
        
        for i, pelicula in enumerate(peliculas):
            if pelicula['Codigo'] == codigo:
                encontrada = True
                print('\nPelicula encontrada.\n')
                mostrar_pelicula(i, pelicula)
                break
        if not encontrada:
            print('\nPelicula no encontrada.\n')
    else:
        print('\nNo hay peliculas registradas.\n')
   

    

# ==============================================================================================
#                                  ACTUALIZAR CANTIDAD DE PELICULA                   
# ==============================================================================================
def actualizar_pelicula():
    if peliculas:
        print('\nActualizador de datos de peliculas\n')
        codigo = input('Codigo de la pelicula a buscar: ').strip().upper()
        for i, pelicula in enumerate(peliculas):
            if pelicula['Codigo'] == codigo:
                mostrar_pelicula(i, pelicula)
                print('''
                ===================================
                        Actualizar pelicula
                ===================================
                1 -> agregar.
                2 -> disminuir.
                ===================================
                ''')
                try: 
                    actualizar = int(input('Elije una opcion: '))
                    
                except ValueError:
                    print('\nDato invalido.\n')
                    continue
                
                if actualizar == 1:
                    try:
                        cantidad = int(input('Cantidad a agregar: '))
                    except ValueError:
                        print('\nDato invalido.\n')
                        continue
                    if cantidad > 0:
                        pelicula['Cantidad'] += cantidad
                        print('\nPelicula actualizada correctamente.\n')
                        
                    else:
                        print('\nEsta cantidad es invalida.\n')
                        continue

                elif actualizar == 2:
                    try:
                        cantidad = int(input('Cantidad a agregar: '))
                    except ValueError:
                        print('\nDato invalido.\n')
                        continue
                    if cantidad >= 0 and cantidad <= pelicula['Cantidad']:
                        pelicula['Cantidad'] -= cantidad
                        print('\nPelicula actualizada correctamente.\n')
                        
                    else:
                        print('\nEsta cantidad es invalida.\n')
                        continue
    else:
        print('\nNo hay peliculas registradas.\n')


# ==============================================================================================
#                                       ELIMINAR PELICULA                   
# ==============================================================================================
def eliminar_pelicula_por_codigo():
    if peliculas:
        print('\nEliminador de pelicula.\n')
        encontrada = False
        codigo = input('Codigo de la pelicula: ').strip().upper()
        
        for i, pelicula in enumerate(peliculas):
            if pelicula['Codigo'] == codigo:
                encontrada = True
                print('\nPelicula encontrada.\n')
                mostrar_pelicula(i, pelicula)
                eliminar = input('Desea eliminar la pelicula-(si/no): ').strip().lower()
                if eliminar == 'si':
                    peliculas.remove(pelicula)
                    print('\nPelicula eliminada correctamente.')
                    break
                else:
                    print('\nLa pelicula no se va a eliminar.\n')
                    break
            
        if not encontrada:
            print('\nPelicula no encontrada.\n')
    else:
        print('\nNo hay peliculas registradas.\n')




# ==============================================================================================
#                                MOSTRAR ESTADISTICAS DE PELICULA                   
# ==============================================================================================
def mostrar_estadisticas():
    if peliculas:
        print('\nEstadisticas del sistema.\n')
        total_peliculas = len(peliculas)
        total_copias = 0
        pelicula_mayor = peliculas[0]
        pelicula_menor = peliculas[0]
        pelicula_mayor_5 = 0
        pelicula_menor_5 = 0
        
        for pelicula in peliculas:
            total_copias += pelicula['Cantidad']
            
            if pelicula['Cantidad'] > pelicula_mayor['Cantidad']:
                 pelicula_mayor = pelicula   
                 
            if pelicula['Cantidad'] < pelicula_menor['Cantidad']:
                pelicula_menor = pelicula
                
            if pelicula['Cantidad'] > 5:
                pelicula_mayor_5 += 1
                
            else:
                pelicula_menor_5 += 1
                
        print(f"""
        ========== ESTADÍSTICAS ==========
        Total de películas             : {total_peliculas}
        Total de copias                : {total_copias}
        Película con más copias        : {pelicula_mayor['Titulo']} ({pelicula_mayor['Cantidad']} copias)
        Película con menos copias      : {pelicula_menor['Titulo']} ({pelicula_menor['Cantidad']} copias)
        Películas con más de 5 copias  : {pelicula_mayor_5}
        Películas con 5 copias o menos : {pelicula_menor_5}
        =================================
        """)
    else:
        print('\nNo hay peliculas registradas.\n')


# ==============================================================================================
#                                           SISTEMA PRINCIPAL                  
# ==============================================================================================
while True:
    
    mostrar_menu()
    
    try:
        opcion = int(input('Elije una opcion: '))
        
    except ValueError:
        print('\nDato invalido.')
        continue
    
    os.system('clear')
    
    if opcion == 1:
        agregar_pelicula()
    
    elif opcion == 2:
        mostrar_peliculas()
    
    elif opcion == 3:
        buscar_pelicula_por_codigo()
    
    elif opcion == 4:
        actualizar_pelicula()
    
    elif opcion == 5:
        eliminar_pelicula_por_codigo()
        
    elif opcion == 6:
        mostrar_estadisticas()
        
        
    elif opcion == 7:
        os.system('clear')
        print('\nSaliendo del sistema.\n')   
        break