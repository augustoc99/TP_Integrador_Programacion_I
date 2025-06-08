import time

# Lista fija de tareas domésticas con campos: nombre, prioridad y responsable
tareas = [
    {"nombre": "Lavar los platos",      "prioridad": 3, "responsable": "Juan"},
    {"nombre": "Sacar la basura",       "prioridad": 1, "responsable": "Ana"},
    {"nombre": "Tender la cama",        "prioridad": 4, "responsable": "Luis"},
    {"nombre": "Preparar el almuerzo",  "prioridad": 2, "responsable": "Carlos"}
]

def bubble_sort_tareas(lista):
    """
    Ordena la lista de tareas por prioridad usando el algoritmo Bubble Sort.
    Retorna la lista ordenada (en el mismo objeto lista recibido).
    Complejidad: O(n²) en el peor caso.
    """
    # n = número de elementos en la lista
    n = len(lista)

    # Recorremos la lista n veces (o hasta que no haya más intercambios)
    for i in range(n):
        # En cada pasada, el elemento de mayor prioridad "burbujea" hacia el final
        # El índice j va de 0 hasta n - i - 2, ya que después de i pasadas,
        # los últimos i elementos están en su posición correcta
        for j in range(0, n - i - 1):
            # Comparamos la prioridad de la tarea en posición j y la siguiente
            if lista[j]["prioridad"] > lista[j + 1]["prioridad"]:
                # Si la prioridad actual es mayor (número mayor = menos urgente),
                # intercambiamos las dos posiciones
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    # Devolvemos la lista ya ordenada
    return lista

def sort_nativo(lista):
    """
    Ordena la lista de tareas por prioridad usando la función sorted() de Python.
    Internamente, sorted() utiliza el algoritmo Timsort (O(n log n) peor caso).
    Retorna una nueva lista ordenada, sin modificar la original.
    """
    # La clave key=lambda tarea: tarea["prioridad"] indica que se compare
    # cada diccionario según el valor del campo "prioridad"
    return sorted(lista, key=lambda tarea: tarea["prioridad"])

def medir_tiempo(funcion, lista):
    """
    Mide el tiempo que tarda en ejecutarse la función ordenadora sobre una copia de la lista.
    - funcion: la función de ordenamiento (bubble_sort_tareas o sort_nativo).
    - lista: la lista original de tareas.
    Retorna una tupla (resultado, tiempo_en_segundos).
    """
    # Guardamos en 'inicio' el valor actual del contador de alta precisión
    inicio = time.perf_counter()

    # Ejecutamos la función sobre una copia de la lista original
    # para no modificar 'tareas' y garantizar igualdad de condiciones
    resultado = funcion(lista.copy())

    # Guardamos en 'fin' el valor del contador luego de la ordenación
    fin = time.perf_counter()

    # Devolvemos la lista ordenada y la diferencia de tiempo
    return resultado, fin - inicio

def imprimir_tabla(lista_tareas):
    """
    Imprime en consola una tabla ASCII con las columnas:
    Nombre, Prioridad y Responsable, para la lista de tareas dada.
    """
    # Encabezado de la tabla con bordes
    print("+------------------------+-----------+-------------+")
    print("| Nombre                 | Prioridad | Responsable |")
    print("+------------------------+-----------+-------------+")
    
    # Para cada tarea, formateamos los campos con ancho fijo
    for tarea in lista_tareas:
        nombre = tarea["nombre"].ljust(24)       # Justifica a la izquierda en 24 caracteres
        prioridad = str(tarea["prioridad"]).center(9)  # Centra en 9 caracteres
        responsable = tarea["responsable"].center(13)  # Centra en 13 caracteres
        print(f"| {nombre}| {prioridad}| {responsable}|")
    
    # Pie de la tabla con bordes
    print("+------------------------+-----------+-------------+")

# --------------------- Bloque de Ejecución ---------------------

# 1) Medición usando Bubble Sort
print("Medición de rendimiento con Bubble Sort:")
resultado_bubble, tiempo_bubble = medir_tiempo(bubble_sort_tareas, tareas)
imprimir_tabla(resultado_bubble)  # Imprime la tabla de tareas ya ordenadas
print(f"Tiempo de ejecución (Bubble Sort): {tiempo_bubble:.8f} segundos\n")

# 2) Medición usando sorted() (Timsort)
print("Medición de rendimiento con sorted():")
resultado_sorted, tiempo_sorted = medir_tiempo(sort_nativo, tareas)
imprimir_tabla(resultado_sorted)  # Imprime la misma tabla, ordenada con sorted()
print(f"Tiempo de ejecución (sorted()): {tiempo_sorted:.8f} segundos")
