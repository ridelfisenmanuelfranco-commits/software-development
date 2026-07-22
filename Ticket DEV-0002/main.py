#===========================================================================================================================================================================
#                                                                      SISTEMA DE GESTION DE MASCOTAS
#===========================================================================================================================================================================

#===========================================================================================================================================================================
#                                                                               DATOS
#===========================================================================================================================================================================
mascotas = []
contador_codigo = len(mascotas) + 1
#===========================================================================================================================================================================
#                                                                      MOSTRAR MENU DEL SISTEMA
#===========================================================================================================================================================================
def mostrar_menu():
    print('''
    =======================================
            VETERIANARIA OBAMA MARLON
    =======================================
    1 -> Registrar mascota.
    2 -> Mostrar mascotas.
    3 -> Buscar por codigo.
    4 -> Actualizar mascota.
    5 -> Eliminar mascota.
    6 -> Estadisticas.
    7 -> Salir.
    =======================================
    ''')


#===========================================================================================================================================================================
#                                                                           OBTENER DATO
#===========================================================================================================================================================================
def obtener_texto(prompt):
    while True:
        dato = input(prompt).strip().title()
        if dato == 'Salir':
            return None
        
        if dato == "":
            print('\nDato invalido.\n')
            continue
        
        return dato


#===========================================================================================================================================================================
#                                                                       OBTENER NOMBRE DE LA MASCOTA
#===========================================================================================================================================================================
def obtener_nombre_mascota():
    return obtener_texto('Nombre de la mascota: ')



#===========================================================================================================================================================================
#                                                                      OBTENER ESPECIE DE LA MASCOTA
#===========================================================================================================================================================================
def obtener_especie_mascota():
    while True:
        especie = obtener_texto('Especie de la mascota: ')
        
        if especie not in ['Perro', 'Gato', 'Ave', 'Reptil', 'Conejo']:
            print('\nEsta especie no es permitida.\n')
            continue
        
        return especie


#===========================================================================================================================================================================
#                                                                       OBTENER RAZA DE DE LA MASCOTA
#===========================================================================================================================================================================
def obtener_raza_mascota():
    return obtener_texto('Raza de la mascota: ')


#===========================================================================================================================================================================
#                                                                       OBTENER PROPIETARIO DE LA MASCOTA
#===========================================================================================================================================================================
def obtener_propietario_mascota():
    return obtener_texto('Nombre del propietario: ')



#===========================================================================================================================================================================
#                                                                         OBTENER VALOR ENTERO
#===========================================================================================================================================================================
def obtener_entero(prompt):
    while True:
        try:
            dato = int(input(prompt))
        except ValueError:
            print('\nDato invalido.\n')
            continue
        
        if dato <= 0:
            print('\nDato incorrecto.\n')
            continue
        
        return dato


#===========================================================================================================================================================================
#                                                                       OBTENER VALOR DECIMAL
#===========================================================================================================================================================================
def obtener_decimal(prompt):
    while True:
        try:
            dato = float(input(prompt))
        except ValueError:
            print('\nDato invalido.\n')
            continue
        
        if dato <= 0:
            print('\nDato incorrecto.\n')
            continue
        
        return round(dato, 2)
    
    
    
#===========================================================================================================================================================================
#                                                                       OBTENER EDAD DE LA MASCOTA
#===========================================================================================================================================================================
def obtener_edad_mascota():
    return obtener_entero('Edad de la mascota: ')


#===========================================================================================================================================================================
#                                                                       OBTENER PESO DE LA MASCOTA
#===========================================================================================================================================================================
def obtener_peso_mascota():
    return obtener_decimal('Peso de la mascota: ')

#===========================================================================================================================================================================
#                                                                       SABER SI ESTA VACUNADO
#===========================================================================================================================================================================
def obtener_estado_vacunacion():
    while True:
        vacunado = obtener_texto('Esta vacunado?: ')

        if vacunado != 'Si' and vacunado != 'No':
            print('\nDato invalido.\n')
            continue
        
        return vacunado

#===========================================================================================================================================================================
#                                                                    GENERAR CODIGO DE LA MASCOTA
#===========================================================================================================================================================================
def generar_codigo_mascota():
    global contador_codigo
    codigo_mascota = f'MAS-{contador_codigo:03}'
    contador_codigo += 1
    
    return codigo_mascota


#===========================================================================================================================================================================
#                                                                       CREAR ESTRUCTURA DE LA MASCOTA
#===========================================================================================================================================================================
def crear_mascota(codigo_mascota,
                nombre_mascota,
                especie_mascota,
                raza_mascota,
                edad_mascota,
                peso_mascota,
                propietario_mascota,
                vacunado):
    return {
        'Codigo': codigo_mascota,
        'Nombre': nombre_mascota,
        'Especie': especie_mascota,
        'Raza': raza_mascota,
        'Edad': edad_mascota,
        'Peso': peso_mascota,
        'Propietario': propietario_mascota,
        'Vacunado': vacunado
    }
    
    
#===========================================================================================================================================================================
#                                                                                REGISTRAR MASCOTA
#===========================================================================================================================================================================
def registrar_mascota():
    existe = False
    nombre_mascota = obtener_nombre_mascota()
    
    if nombre_mascota is None:
        return
    
    propietario_mascota = obtener_propietario_mascota()
    if propietario_mascota is None:
        return
    
    for mascota in mascotas:
        if (mascota['Nombre'] == nombre_mascota 
        and mascota['Propietario'] == propietario_mascota):
            
            existe = True
            break
        
    if existe:
        print('\nYa existe esta mascota en el registro.\n')
        return
            
    especie_mascota = obtener_especie_mascota()
    if especie_mascota is None:
        return
    
    raza_mascota = obtener_raza_mascota()
    if raza_mascota is None:
        return
    
    edad_mascota = obtener_edad_mascota()
    peso_mascota = obtener_peso_mascota()
    vacunado = obtener_estado_vacunacion()
    if vacunado is None:
        return
    
    codigo_mascota = generar_codigo_mascota()
    
    mascota = crear_mascota(codigo_mascota,
                            nombre_mascota,
                            especie_mascota,
                            raza_mascota,
                            edad_mascota,
                            peso_mascota,
                            propietario_mascota,
                            vacunado)
    
    mascotas.append(mascota)
    print('\nMascota agregada correctamente.\n')    
    

#===========================================================================================================================================================================
#                                                                           MOSTRAR MASCOTA
#===========================================================================================================================================================================
def mostrar_mascota(i, mascota):
    print(f'''
    =========================================
    Mascota                    {i + 1}
    =========================================
    Codigo         :   {mascota['Codigo']}
    Nombre         :   {mascota['Nombre']}
    Especie        :   {mascota['Especie']}
    Raza           :   {mascota['Raza']}
    Edad           :   {mascota['Edad']} Años
    Peso           :   {mascota['Peso']} Kg
    Propietario    :   {mascota['Propietario']}
    Esta Vacunado  :   {mascota['Vacunado']}
    =========================================
    ''')

#===========================================================================================================================================================================
#                                                                               MOSTRAR MASCOTAS
#===========================================================================================================================================================================
def mostrar_mascotas():
    if mascotas:
        for i, mascota in enumerate(mascotas):
            mostrar_mascota(i, mascota)
        
        print(f'\nTenemos {len(mascotas)} mascotas en la veterinaria.\n')
    
    else:
        print('\nNo hay mascotas registradas.\n')


#===========================================================================================================================================================================
#                                                                       BUSCAR UNA MASCOTA POR SU CODIGO
#===========================================================================================================================================================================
def buscar_por_codigo(codigo):
    for i, mascota in enumerate(mascotas):
        if mascota['Codigo'] == codigo:
               return i,mascota
            
    return None, None
        


#===========================================================================================================================================================================
#                                                                       OBTENER MASCOTA POR CODIGO
#===========================================================================================================================================================================
def obtener_mascota_por_codigo():
    codigo = input('Codigo de la mascota a buscar: ').strip().upper()
    i, mascota = buscar_por_codigo(codigo)
    if mascota:
        mostrar_mascota(i, mascota)
    
    else:
        print('\nLa mascota no existe.\n')
        
        

#===========================================================================================================================================================================
#                                                                          ACTUALIZAR MASCOTA
#===========================================================================================================================================================================
def actualizar_mascota():
    codigo = input('Codigo de la mascota a buscar: ').strip().upper()
    i, mascota = buscar_por_codigo(codigo)
    if mascota:
        mostrar_mascota(i, mascota)
        while True:
            print('''
            ==================================
                Que desea actualizar:
            ==================================
            1 -> Edad.
            2 -> Peso.
            3 -> Estado vacuna.
            ==================================
            ''')
            try:
                modificar = int(input('Que deseas modificar: '))
            except ValueError:
                print('\nDato invalido.\n')
                continue
            
            match modificar:
                case  1:
                    nueva_edad = obtener_edad_mascota()
                    mascota['Edad'] = nueva_edad
                    print('\nEdad de la mascota actualizada correctamente.\n')
                    break
                
                case 2:
                    nuevo_peso = obtener_peso_mascota()
                    mascota['Peso'] = nuevo_peso
                    print('\nPeso de la mascota actualizada correctamente.\n')
                    break
                
                case 3:
                    vacunado = obtener_estado_vacunacion()
                    
                    if vacunado is None:
                        return
                    
                    mascota['Vacunado'] = vacunado
                    print('\nEstado de la vacuna de la mascota actualizada correctamente.\n')
                    break

                case _:
                    print('\nOpcion invalida.\n')
    else:
        print('\nLa mascota no existe.\n')
        

#===========================================================================================================================================================================
#                                                                           ELIMINAR MASCOTA
#===========================================================================================================================================================================
def eliminar_mascota():
    codigo = input('Codigo de la mascota a buscar: ').strip().upper()
    i, mascota = buscar_por_codigo(codigo)
    if mascota:
        mostrar_mascota(i, mascota)
        print('Desea eliminar la mascota?')
        respuesta = input('(Si/No): ').strip().title()
        if respuesta == 'Si':
            mascotas.remove(mascota)
            print('\nMascota eliminada correctamente.\n')
            
        elif respuesta == 'No':
            print('\nLa mascota no ha sido eliminada.\n')

        else:
            print('\nDato invalido.\n')
        
    else:
        print('\nMascota no encontrada.\n')

#===========================================================================================================================================================================
#                                                                       ESTADADISTICAS
#===========================================================================================================================================================================

def estadisticas():
    if mascotas:
        
        # total
        total = len(mascotas)
        
        # Promedio de edad
        suma_edades = 0

        #  Promedio de peso
        suma_peso = 0 

        # Mas joven 
        mas_joven = mascotas[0]
        mas_vieja = mascotas[0]
        
        #  contar Perros, Gatos y Otras especiea
        cantidad_perros = 0
        cantidad_gatos = 0
        otra_especie = 0 

        for mascota in mascotas:
            suma_peso += mascota['Peso']
            suma_edades += mascota['Edad']
            
            if mascota['Edad'] < mas_joven['Edad']:
                mas_joven = mascota

            if mascota['Edad'] > mas_vieja['Edad']:
                mas_vieja = mascota
                
            if mascota['Especie'] == 'Perro':
                cantidad_perros += 1
            
            elif mascota['Especie'] == 'Gato':
                cantidad_gatos += 1
            else:
                otra_especie += 1   
        
        
        promedio_edad = suma_edades / total
        promedio_peso = suma_peso / total
        
        print(f'''
        =========================================
                ESTADISTICAS GENERALES
        =========================================
        Total de mascotas      : {total}

        Promedio de edad       : {promedio_edad:.2f} años
        Promedio de peso       : {promedio_peso:.2f} kg

        Mascota más joven      : {mas_joven['Nombre']} ({mas_joven['Edad']} años)
        Mascota más vieja      : {mas_vieja['Nombre']} ({mas_vieja['Edad']} años)

        Cantidad de perros     : {cantidad_perros}
        Cantidad de gatos      : {cantidad_gatos}
        Otras especies         : {otra_especie}
        =========================================
        ''')
    else:
        print('\nNo hay mascotas registradas.\n')


#===========================================================================================================================================================================
#                                                                       SISTEMA PRINCIPAL
#===========================================================================================================================================================================
while True:
    mostrar_menu()
    
    try:
        opcion = int(input('Elije una opcion: '))
    
    except ValueError:
        print('\nDato invalido.\n')
        continue
    
    if opcion == 1:
        registrar_mascota()
        
    elif opcion == 2:
        mostrar_mascotas()
        
    elif opcion == 3:
        obtener_mascota_por_codigo()
    
    elif opcion == 4:
        actualizar_mascota()
        
    elif opcion == 5:
        eliminar_mascota()
        
    elif opcion == 6:
        estadisticas()
        
    elif opcion == 7:
        print('\nSaliendo del sistema.\n')
        break
    
    else:
        print('\nOpcion invalida.\n')



'''
case 3:
                    nuevo_propietario = obtener_propietario_mascota()
                    mascota['Propietario'] = nuevo_propietario
                    print('\nPropietario de la mascota actualizada correctamente.\n')
                    break
                
                case 4:
                    nueva_edad = obtener_edad_mascota()
                    nuevo_peso = obtener_peso_mascota()
                    nuevo_propietario = obtener_propietario_mascota()
                    mascota['Edad'] = nueva_edad   
                    mascota['Peso'] = nuevo_peso
                    mascota['Propietario'] = nuevo_propietario
                    print('\nMascota actualizada correctamente.\n')
                    break
                    '''