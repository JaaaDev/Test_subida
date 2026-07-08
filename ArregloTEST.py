
def unidades_tipo(t_arreglo, t_bodega):
    
    tipo_buscado = input("Ingrese el tipo de arreglo a buscar : ").strip().lower()
    contador_tipo = 0
    for cod_arreglo, valor_arreglo in t_arreglo.items():
        if valor_arreglo[1] == tipo_buscado:
            for cod_bodega, valor_bodega in t_bodega.items():
                if cod_bodega == cod_arreglo:
                    contador_tipo +=valor_bodega[1]
                    break
    if contador_tipo >0:
        print(f"Los productos encontrados de {tipo_buscado}, son {contador_tipo}")
    else:
        print(f"No hay stock del tipo buscado")
def busqueda_precio(p_min, p_max, p_arreglo, p_bodega):

    lista_por_precio = []
    for cod_bodega, valor_bodega in p_bodega.items():
        if valor_bodega[0] >= p_min and valor_bodega[0]<= p_max and valor_bodega[1] != 0:
            for cod_arreglo, valor_arreglo in p_arreglo.items():
                if cod_arreglo == cod_bodega:
                    lista_por_precio.append(f"{cod_arreglo} : Nombre : {valor_arreglo[0]}. Tipo : {valor_arreglo[1]}. Valor : {valor_bodega[0]}. Cantidad {valor_bodega[1]}" )
                    break
    lista_por_precio.sort()

    if lista_por_precio:
        for lista in lista_por_precio:
            print(lista)
    else:
        print("No se han encontrado arreglos en el rango de precio")
def buscar_codigo(cod,b_bodega):
    
    for cod_bodega, valor_bodega in b_bodega.items():
        if cod_bodega == cod:
            return True
    return False

def actualizar_precio(cod, nuevo_precio, a_bodega):
    
    revisa_cod = buscar_codigo(cod,a_bodega)

    if revisa_cod == True:
        for cod_bodega, valor_bodega in a_bodega.items():
            if cod_bodega == cod:
                valor_bodega[0] = nuevo_precio
                return True
    else:
        return False


def leer_opcion():
    while True:    
        try:
            print("========== MENÚ PRINCIPAL ==========")
            print("1. Unidades por tipo de arreglo")
            print("2. Búsqueda de arreglos por rango de precio")
            print("3. Actualizar precio de arreglo")
            print("4. Agregar arreglo")
            print("5. Eliminar arreglo")
            print("6. Salir")
            print("=====================================")

            if 0<(opcion:=int(input("Ingrese una opción valida : "))) <=6:
                return opcion
            else:
                print("La opción ingresada no es valida, intente nuevamente")


        except ValueError:
            print("Ingrese una opción valida")
#Pruebas de subida
def main():

    #DICCIONARIO DE ARREGLOS FLORALES
    arreglos = {
        'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True,'primavera'],
        'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todoaño'],
        'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
        'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
        'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
        'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno']
    }
    bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6]
    }

    while True:
        opciones_menu = leer_opcion()

        if opciones_menu == 1:
            unidades_tipo(arreglos,bodega)
        elif opciones_menu == 2:
            while True:
                try:
                    precio_min = int(input("Ingrese el valor minimo : "))
                    precio_max = int(input("Ingrese el valor maximo : "))

                    if precio_min >0 and precio_min < precio_max:
                        busqueda_precio(precio_min,precio_max,arreglos,bodega)
                    else:
                        print(f"El precio minimo no debe ser menor a 0 o superior a precio  maximo")
                except ValueError:
                    print("Los precios ingresados son incorrectos")
        elif opciones_menu == 3:

            cod_update = input("Ingrese el codigo : ").strip().upper()
            while True:
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio : "))
                    if nuevo_precio > 0:
                        break
                    else:
                        print("Debe ingresar valores enteros positivos")
                except ValueError:
                    print("El nuevo precio ingresado es incorrecto")

            actualizar_precio(cod_update,nuevo_precio,bodega)
        elif opciones_menu == 4:
            pass
        elif opciones_menu == 5:
            pass
        elif opciones_menu == 6:
            pass


#MAIN DE ARREGLOS FLORALES


if __name__ == "__main__":
    main()